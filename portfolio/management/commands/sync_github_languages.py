import json
import urllib.request

from django.core.management.base import BaseCommand
from django.db import close_old_connections

from portfolio.models import Project


class Command(BaseCommand):
    help = "Sync project languages from GitHub language statistics."

    def add_arguments(self, parser):
        parser.add_argument("--username", default="dragonwolf1o1")
        parser.add_argument("--limit", type=int, default=100)

    def handle(self, *args, **options):
        username = options["username"]
        repos = self.fetch_json(f"https://api.github.com/users/{username}/repos?per_page={options['limit']}&sort=updated")
        updates = []

        for repo in repos:
            repo_url = repo["html_url"]
            languages = self.languages_from_repo(repo)
            if not languages:
                continue

            tags = languages.copy()
            if repo.get("fork"):
                tags.append("Fork")
            tags.append("GitHub")
            updates.append((repo_url, ", ".join(languages), ", ".join(tags)))

        close_old_connections()
        synced = 0
        for repo_url, languages_used, eyebrow in updates:
            synced += Project.objects.filter(repo_url=repo_url).update(
                languages_used=languages_used,
                eyebrow=eyebrow,
            )

        self.stdout.write(self.style.SUCCESS(f"Synced languages for {synced} GitHub projects."))

    def languages_from_repo(self, repo):
        languages_url = repo.get("languages_url")
        if not languages_url:
            return [repo["language"]] if repo.get("language") else []

        data = self.fetch_json(languages_url)
        languages = [
            language
            for language, byte_count in sorted(data.items(), key=lambda item: item[1], reverse=True)
            if byte_count > 0
        ]
        if languages:
            return languages

        return [repo["language"]] if repo.get("language") else []

    def fetch_json(self, url):
        request = urllib.request.Request(url, headers={"User-Agent": "portfolio-language-sync"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
