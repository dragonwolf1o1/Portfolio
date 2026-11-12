from django.db import migrations


TEXTS = [
    ("value_eyebrow", "Value proposition eyebrow", "Business-first analytics & development"),
    ("value_title", "Value proposition title", "Turn scattered data and manual reporting into decisions your team can trust."),
    ("value_description", "Value proposition description", "I combine Python and SQL to clean, validate, and model your data; Power BI and Excel to make performance visible; and Django to turn proven workflows into dependable internal tools. The goal is practical: less reporting friction, clearer risk signals, and a solution tied to an agreed business measure."),
    ("value_stack_label", "Technology stack accessible label", "Core technology stack"),
    ("method_eyebrow", "Methodology eyebrow", "How I solve problems"),
    ("method_title", "Methodology title", "A clear path from business question to measurable outcome."),
    ("method_intro", "Methodology intro", "Every engagement starts with the decision to improve, then moves through validated data and a solution your team can actually use."),
    ("testimonials_eyebrow", "Testimonials eyebrow", "Client feedback"),
    ("testimonials_title", "Testimonials title", "Trust is built through useful outcomes."),
    ("testimonials_intro", "Testimonials intro", "Feedback from collaborators will be published here with permission."),
    ("testimonials_empty", "Testimonials empty state", "Client testimonials are being collected. For now, explore the documented project outcomes or start a conversation about your challenge."),
    ("testimonials_cta", "Testimonials contact link", "Discuss a project"),
    ("home_hero_subtitle", "Home hero subtitle", "Data Analyst & Django Developer | Python, SQL, Power BI"),
    ("home_hero_title", "Home hero title", "I turn complex data into faster, clearer business decisions."),
    ("home_hero_description", "Home hero description", "From validated ETL pipelines and decision-ready dashboards to Django tools that reduce repetitive work, I build practical solutions around measurable business needs."),
]


def seed_conversion_content(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")
    for key, label, value in TEXTS:
        SiteText.objects.update_or_create(key=key, defaults={"label": label, "value": value})


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0013_case_studies_and_testimonials")]

    operations = [migrations.RunPython(seed_conversion_content, migrations.RunPython.noop)]
