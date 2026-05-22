import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or update the deployment superuser from environment variables."

    def handle(self, *args, **options):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin@1o1rowc").strip()
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "").strip()
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "").strip()

        if not username:
            raise CommandError("DJANGO_SUPERUSER_USERNAME is required.")

        if not password:
            if os.getenv("VERCEL") or not settings.DEBUG:
                raise CommandError("DJANGO_SUPERUSER_PASSWORD is required for deployment.")
            self.stdout.write(self.style.WARNING("DJANGO_SUPERUSER_PASSWORD is not set; skipped superuser update."))
            return

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )
        user.email = email or user.email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        status = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Superuser {username} {status}."))
