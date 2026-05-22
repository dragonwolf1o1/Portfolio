import json
import urllib.request

from django.core.management.base import BaseCommand
from django.db import close_old_connections

from portfolio.models import ContactDetail, Project, SiteText


class Command(BaseCommand):
    help = "Import public GitHub repositories into portfolio projects."

    def add_arguments(self, parser):
        parser.add_argument("--username", default="dragonwolf1o1")
        parser.add_argument("--limit", type=int, default=100)

    def handle(self, *args, **options):
        username = options["username"]
        repos = self.fetch_repos(username, options["limit"])
        prepared = [self.prepare_repo(repo) for repo in repos]

        close_old_connections()
        existing = {
            project.repo_url: project
            for project in Project.objects.exclude(repo_url__isnull=True).exclude(repo_url="")
        }
        start_order = (Project.objects.order_by("-order").values_list("order", flat=True).first() or 0) + 1
        to_create = []
        to_update = []

        for offset, data in enumerate(prepared):
            repo_url = data.pop("repo_url")
            project = existing.get(repo_url)

            if project:
                for field, value in data.items():
                    setattr(project, field, value)
                to_update.append(project)
                continue

            to_create.append(Project(repo_url=repo_url, order=start_order + offset, **data))

        if to_create:
            Project.objects.bulk_create(to_create)

        if to_update:
            Project.objects.bulk_update(
                to_update,
                [
                    "eyebrow",
                    "title",
                    "description",
                    "extra_description",
                    "image_url",
                    "image_alt",
                    "live_url",
                    "source",
                    "languages_used",
                    "is_active",
                ],
            )

        ContactDetail.objects.update_or_create(
            label="GitHub",
            defaults={
                "value": f"github.com/{username}",
                "href": f"https://github.com/{username}",
                "order": 5,
                "is_active": True,
            },
        )
        SiteText.objects.update_or_create(
            key="projects_banner_title",
            defaults={"label": "Projects banner title", "value": "Projects"},
        )
        self.stdout.write(self.style.SUCCESS(f"Imported {len(prepared)} GitHub repositories."))

    def prepare_repo(self, repo):
        title = self.pretty_title(repo["name"])
        languages = self.fetch_languages(repo.get("languages_url"))
        if not languages and repo.get("language"):
            languages = [repo["language"]]
        primary_language = languages[0] if languages else repo.get("language") or "Repository"
        image_url, image_alt = self.image_for(repo["name"])

        return {
            "repo_url": repo["html_url"],
            "eyebrow": self.eyebrow_for(repo, languages, primary_language),
            "title": title,
            "description": self.description_for(repo, title, primary_language),
            "extra_description": self.extra_for(repo),
            "image_url": image_url,
            "image_alt": image_alt,
            "live_url": repo.get("homepage") or "",
            "source": "GitHub",
            "languages_used": ", ".join(languages),
            "is_active": True,
        }

    def fetch_repos(self, username, limit):
        url = f"https://api.github.com/users/{username}/repos?per_page={limit}&sort=updated"
        return self.fetch_json(url)

    def fetch_languages(self, url):
        if not url:
            return []

        data = self.fetch_json(url)
        return [
            language
            for language, byte_count in sorted(data.items(), key=lambda item: item[1], reverse=True)
            if byte_count > 0
        ]

    def fetch_json(self, url):
        request = urllib.request.Request(url, headers={"User-Agent": "portfolio-importer"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))

    def pretty_title(self, name):
        return name.replace("_", " ").replace("-", " ").strip().title()

    def description_for(self, repo, title, language):
        if repo.get("description"):
            return repo["description"]

        kind = "Forked GitHub repository" if repo.get("fork") else "GitHub project"
        if language == "Repository":
            return f"{kind} for {title}, available for review on GitHub."

        return f"{kind} for {title}, built around {language} and available for review on GitHub."

    def extra_for(self, repo):
        parts = []
        if repo.get("fork"):
            parts.append("Forked repository.")
        parts.append(f"Stars: {repo.get('stargazers_count', 0)}")
        parts.append(f"Forks: {repo.get('forks_count', 0)}")
        return " | ".join(parts)

    def eyebrow_for(self, repo, languages, primary_language):
        tags = languages.copy()
        if not tags and primary_language != "Repository":
            tags.append(primary_language)
        if repo.get("fork"):
            tags.append("Fork")
        tags.append("GitHub")
        return ", ".join(tags)

    def image_for(self, name):
        key = name.lower()

        if any(term in key for term in ["analytics", "analysis", "risk", "census", "movie", "sport"]):
            return (
                "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop",
                "Analytics project",
            )

        if any(term in key for term in ["hash", "password", "encryption", "security", "jammer", "wifi", "safe"]):
            return (
                "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&auto=format&fit=crop",
                "Security project",
            )

        if any(term in key for term in ["music", "stream", "social", "e-commerce", "chat", "blog"]):
            return (
                "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop",
                "Web application project",
            )

        if any(term in key for term in ["library", "banking", "customer", "management", "managment", "auth"]):
            return (
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&auto=format&fit=crop",
                "Database application project",
            )

        return (
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop",
            "GitHub project",
        )
