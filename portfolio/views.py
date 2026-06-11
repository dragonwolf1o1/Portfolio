from django.shortcuts import render

from .models import ContactDetail, Experience, InfoCard, Project, Service, Skill, Statistic


CONTACT_LABELS = ["Phone", "Email", "LinkedIn", "Address", "GitHub"]
RESUME_PROJECT_TITLES = [
    "Credit Risk Analysis & Scoring System",
    "Sports Analytics: Olympic Games Analysis",
]
RESUME_METRICS = [
    {"value": "25%", "label": "Data accuracy improvement through cleaning and preprocessing"},
    {"value": "5+", "label": "Interactive Power BI dashboards for business metrics"},
    {"value": "40%", "label": "Reduction in report generation time"},
    {"value": "268K+", "label": "Olympic records modeled for analytics"},
]
RESUME_SKILL_GROUPS = [
    {
        "eyebrow": "Programming",
        "title": "Python & SQL",
        "tools": "Pandas, NumPy, Matplotlib, Seaborn, MySQL",
    },
    {
        "eyebrow": "Visualization",
        "title": "BI Dashboards",
        "tools": "Power BI, Tableau, Advanced Microsoft Excel",
    },
    {
        "eyebrow": "Analytics",
        "title": "Statistics & Modeling",
        "tools": "Hypothesis testing, predictive modeling, data mining",
    },
    {
        "eyebrow": "Workflow",
        "title": "Tools & Delivery",
        "tools": "Git, Linux, Jupyter Notebook, ETL processes",
    },
]


def home(request):
    return render(
        request,
        "portfolio/index.html",
        {
            "stats": Statistic.objects.filter(is_active=True),
            "services": Service.objects.filter(is_active=True),
        },
    )


def about(request):
    return render(
        request,
        "portfolio/about.html",
        {
            "skills": Skill.objects.filter(is_active=True),
            "experiences": Experience.objects.filter(is_active=True).prefetch_related("bullets"),
            "info_cards": InfoCard.objects.filter(is_active=True).prefetch_related("bullets"),
        },
    )


def projects(request):
    return render(
        request,
        "portfolio/projects.html",
        {
            "projects": Project.objects.filter(is_active=True),
        },
    )


def resume(request):
    return render(
        request,
        "portfolio/resume.html",
        {
            "skills": Skill.objects.filter(is_active=True),
            "experiences": Experience.objects.filter(is_active=True).prefetch_related("bullets"),
            "info_cards": InfoCard.objects.filter(is_active=True).prefetch_related("bullets"),
            "featured_projects": Project.objects.filter(is_active=True, title__in=RESUME_PROJECT_TITLES),
            "resume_metrics": RESUME_METRICS,
            "resume_skill_groups": RESUME_SKILL_GROUPS,
        },
    )


def contact(request):
    return render(
        request,
        "portfolio/contact.html",
        {
            "contact_details": ContactDetail.objects.filter(is_active=True, label__in=CONTACT_LABELS),
        },
    )


def error_404(request, exception=None):
    return render(request, "errors/404.html", status=404)


def error_500(request):
    return render(request, "errors/500.html", status=500)
