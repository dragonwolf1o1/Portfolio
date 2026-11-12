from django.db import migrations, models


def seed_case_studies(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    case_studies = {
        "Credit Risk Analysis & Scoring System": {
            "challenge": "Loan risk decisions depended on fragmented data and manual review, making scoring less consistent and rejection handling difficult to audit.",
            "solution": "Built an end-to-end Python and MySQL pipeline across five tables, engineered more than four business features, and applied logistic regression with automated risk-band scoring. Added validation rules and a daemon-based workflow for real-time database updates.",
            "business_impact": "The resume reports an estimated 30-40% reduction in scoring errors and complete rejection logging, improving consistency and auditability of loan assessments.",
        },
        "Sports Analytics: Olympic Games Analysis": {
            "challenge": "More than a century of Olympic results needed a consistent structure for comparing participation, sports, events, and medal trends across eras.",
            "solution": "Designed a normalized relational warehouse spanning 11 tables, consolidated the historical dataset, wrote 17 advanced SQL analytics queries, and built an interactive Power BI dashboard for multidimensional exploration.",
            "business_impact": "Enabled analysis across 268K+ records, 128K+ athletes, 66 sports, and 757 events, surfacing demographic outliers and medal trends across 120 years of data.",
        },
    }
    for title, details in case_studies.items():
        Project.objects.filter(title=title).update(**details)


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0012_seed_resume_page_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="challenge",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="solution",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="implementation_time",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="project",
            name="business_impact",
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("client_name", models.CharField(max_length=160)),
                ("client_role", models.CharField(blank=True, max_length=180)),
                ("company", models.CharField(blank=True, max_length=180)),
                ("quote", models.TextField()),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.RunPython(seed_case_studies, migrations.RunPython.noop),
    ]
