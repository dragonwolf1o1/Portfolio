from .models import SiteText


DEFAULT_CONTENT = {
    "meta_default_title": "Saurabh Gupta | Data Analyst | Developer",
    "site_logo_text": "Saurabh",
    "site_logo_accent": " Gupta",
    "nav_home": "Home",
    "nav_about": "About",
    "nav_resume": "Resume",
    "nav_projects": "Projects",
    "nav_contact": "Contact",
    "meta_resume_title": "Resume | Saurabh Gupta",
    "resume_banner_title": "Resume",
    "resume_subtitle": "Data Analyst Resume",
    "resume_title": "A practical analyst profile built around clean data, useful dashboards, and business-ready reporting.",
    "resume_summary": "Results-driven Data Analyst with expertise in transforming complex datasets into actionable business insights. Proficient in Python, SQL, Power BI, and Advanced Excel with strong foundations in statistical analysis and data visualization.",
    "resume_download_label": "Download Resume",
    "resume_contact_label": "Contact Me",
    "resume_metrics_eyebrow": "Measured Impact",
    "resume_metrics_title": "Resume Highlights",
    "resume_skills_eyebrow": "Technical Skills",
    "resume_skills_title": "Tools I Work With",
    "resume_projects_eyebrow": "Selected Work",
    "resume_projects_title": "Projects From My Resume",
    "resume_profile_eyebrow": "Professional Experience",
    "resume_profile_title": "Training & Applied Analytics",
    "resume_foundation_eyebrow": "Education & Certifications",
    "resume_foundation_title": "Academic Foundation",
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
