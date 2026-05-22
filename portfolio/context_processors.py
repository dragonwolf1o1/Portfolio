from .models import SiteText


DEFAULT_CONTENT = {
    "meta_default_title": "Saurabh Gupta | Data Analyst | Developer",
    "site_logo_text": "Saurabh",
    "site_logo_accent": " Gupta",
    "nav_home": "Home",
    "nav_about": "About",
    "nav_projects": "Projects",
    "nav_contact": "Contact",
    "footer_text": "© 2026 Saurabh Gupta. All Rights Reserved.",
    "error_404_meta_title": "Page Not Found | Saurabh Gupta",
    "error_404_code": "404",
    "error_404_subtitle": "Page not found",
    "error_404_title": "This page is not available.",
    "error_404_description": "The page may have moved, been renamed, or no longer exists. You can return home or browse the project work.",
    "error_500_meta_title": "Server Error | Saurabh Gupta",
    "error_500_code": "500",
    "error_500_subtitle": "Something went wrong",
    "error_500_title": "The site hit an unexpected issue.",
    "error_500_description": "Please try again in a moment. If the issue continues, use the contact page to reach out.",
    "error_home_button": "Go Home",
    "error_projects_button": "View Projects",
    "error_contact_button": "Contact Me",
}


def site_content(request):
    content = DEFAULT_CONTENT.copy()

    try:
        content.update({item.key: item.value for item in SiteText.objects.all()})
    except Exception:
        pass

    return {"content": content}
