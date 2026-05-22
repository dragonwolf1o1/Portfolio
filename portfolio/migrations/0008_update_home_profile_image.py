from django.db import migrations


def update_home_image(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")
    SiteText.objects.update_or_create(
        key="home_hero_image_url",
        defaults={
            "label": "Home hero image URL",
            "value": "https://avatars.githubusercontent.com/u/104382438?v=4",
        },
    )
    SiteText.objects.update_or_create(
        key="home_hero_image_alt",
        defaults={
            "label": "Home hero image alt text",
            "value": "Saurabh Gupta profile photo",
        },
    )


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0007_project_languages_used"),
    ]

    operations = [
        migrations.RunPython(update_home_image, migrations.RunPython.noop),
    ]
