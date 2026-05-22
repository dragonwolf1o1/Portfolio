from django.db import migrations


def move_profile_image_to_about(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")
    SiteText.objects.update_or_create(
        key="home_hero_image_url",
        defaults={
            "label": "Home hero image URL",
            "value": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop",
        },
    )
    SiteText.objects.update_or_create(
        key="home_hero_image_alt",
        defaults={
            "label": "Home hero image alt text",
            "value": "Analytics dashboard",
        },
    )
    SiteText.objects.update_or_create(
        key="about_image_url",
        defaults={
            "label": "About image URL",
            "value": "https://avatars.githubusercontent.com/u/104382438?v=4",
        },
    )
    SiteText.objects.update_or_create(
        key="about_image_alt",
        defaults={
            "label": "About image alt text",
            "value": "Saurabh Gupta profile photo",
        },
    )


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0008_update_home_profile_image"),
    ]

    operations = [
        migrations.RunPython(move_profile_image_to_about, migrations.RunPython.noop),
    ]
