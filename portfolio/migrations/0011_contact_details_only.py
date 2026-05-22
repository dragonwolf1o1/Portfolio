from django.db import migrations


CONTACT_DETAILS = [
    ("Phone", "+91 6387870113", "tel:+916387870113"),
    ("Email", "saurabhguptagzpofficial@gmail.com", "mailto:saurabhguptagzpofficial@gmail.com"),
    ("LinkedIn", "linkedin.com/in/saurabhguptaofficial", "https://www.linkedin.com/in/saurabhguptaofficial"),
    ("Address", "Varanasi, Uttar Pradesh, India", ""),
    ("GitHub", "github.com/dragonwolf1o1", "https://github.com/dragonwolf1o1"),
]


def seed_contact_details(apps, schema_editor):
    ContactDetail = apps.get_model("portfolio", "ContactDetail")

    ContactDetail.objects.filter(label="Location").update(label="Address")

    allowed_labels = [label for label, value, href in CONTACT_DETAILS]
    ContactDetail.objects.exclude(label__in=allowed_labels).update(is_active=False)

    for order, (label, value, href) in enumerate(CONTACT_DETAILS, start=1):
        ContactDetail.objects.update_or_create(
            label=label,
            defaults={
                "value": value,
                "href": href,
                "order": order,
                "is_active": True,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_seed_github_projects"),
    ]

    operations = [
        migrations.RunPython(seed_contact_details, migrations.RunPython.noop),
    ]
