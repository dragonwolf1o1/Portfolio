from django.shortcuts import render

from .models import ContactDetail, Experience, InfoCard, Project, Service, Skill, Statistic


CONTACT_LABELS = ["Phone", "Email", "LinkedIn", "Address", "GitHub"]


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
