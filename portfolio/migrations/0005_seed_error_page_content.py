from django.db import migrations


def seed_error_content(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")
    texts = [
        ("error_404_meta_title", "404 browser title", "Page Not Found | Saurabh Gupta"),
        ("error_404_code", "404 error code", "404"),
        ("error_404_subtitle", "404 subtitle", "Page not found"),
        ("error_404_title", "404 heading", "This page is not available."),
        ("error_404_description", "404 description", "The page may have moved, been renamed, or no longer exists. You can return home or browse the project work."),
        ("error_500_meta_title", "500 browser title", "Server Error | Saurabh Gupta"),
        ("error_500_code", "500 error code", "500"),
        ("error_500_subtitle", "500 subtitle", "Something went wrong"),
        ("error_500_title", "500 heading", "The site hit an unexpected issue."),
        ("error_500_description", "500 description", "Please try again in a moment. If the issue continues, use the contact page to reach out."),
        ("error_home_button", "Error page home button", "Go Home"),
        ("error_projects_button", "Error page projects button", "View Projects"),
        ("error_contact_button", "Error page contact button", "Contact Me"),
    ]

    for key, label, value in texts:
        SiteText.objects.update_or_create(key=key, defaults={"label": label, "value": value})


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0004_project_live_url_project_repo_url_project_source"),
    ]

    operations = [
        migrations.RunPython(seed_error_content, migrations.RunPython.noop),
    ]
