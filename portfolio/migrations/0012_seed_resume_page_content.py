from django.db import migrations


RESUME_TEXTS = [
    ("nav_resume", "Navigation resume label", "Resume"),
    ("meta_resume_title", "Resume browser title", "Resume | Saurabh Gupta"),
    ("resume_banner_title", "Resume banner title", "Resume"),
    ("resume_subtitle", "Resume subtitle", "Data Analyst Resume"),
    (
        "resume_title",
        "Resume heading",
        "A practical analyst profile built around clean data, useful dashboards, and business-ready reporting.",
    ),
    (
        "resume_summary",
        "Resume summary",
        "Results-driven Data Analyst with expertise in transforming complex datasets into actionable business insights. Proficient in Python, SQL, Power BI, and Advanced Excel with strong foundations in statistical analysis and data visualization. Experienced in developing ETL pipelines, creating interactive dashboards, and implementing data-driven solutions.",
    ),
    ("resume_download_label", "Resume download button", "Download Resume"),
    ("resume_contact_label", "Resume contact button", "Contact Me"),
    ("resume_metrics_eyebrow", "Resume metrics eyebrow", "Measured Impact"),
    ("resume_metrics_title", "Resume metrics title", "Resume Highlights"),
    ("resume_skills_eyebrow", "Resume skills eyebrow", "Technical Skills"),
    ("resume_skills_title", "Resume skills title", "Tools I Work With"),
    ("resume_projects_eyebrow", "Resume projects eyebrow", "Selected Work"),
    ("resume_projects_title", "Resume projects title", "Projects From My Resume"),
    ("resume_profile_eyebrow", "Resume experience eyebrow", "Professional Experience"),
    ("resume_profile_title", "Resume experience title", "Training & Applied Analytics"),
    ("resume_foundation_eyebrow", "Resume foundation eyebrow", "Education & Certifications"),
    ("resume_foundation_title", "Resume foundation title", "Academic Foundation"),
]


def seed_resume_texts(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")

    for key, label, value in RESUME_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"label": label, "value": value},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0011_contact_details_only"),
    ]

    operations = [
        migrations.RunPython(seed_resume_texts, migrations.RunPython.noop),
    ]
