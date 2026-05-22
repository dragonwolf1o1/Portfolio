from django.db import migrations


def seed_content(apps, schema_editor):
    SiteText = apps.get_model("portfolio", "SiteText")
    Statistic = apps.get_model("portfolio", "Statistic")
    Service = apps.get_model("portfolio", "Service")
    Skill = apps.get_model("portfolio", "Skill")
    Experience = apps.get_model("portfolio", "Experience")
    ExperienceBullet = apps.get_model("portfolio", "ExperienceBullet")
    InfoCard = apps.get_model("portfolio", "InfoCard")
    InfoBullet = apps.get_model("portfolio", "InfoBullet")
    Project = apps.get_model("portfolio", "Project")
    ContactDetail = apps.get_model("portfolio", "ContactDetail")

    texts = [
        ("meta_default_title", "Default browser title", "Saurabh Gupta | Data Analyst | Developer"),
        ("meta_home_title", "Home browser title", "Saurabh Gupta | Data Analyst"),
        ("meta_about_title", "About browser title", "About | Saurabh Gupta"),
        ("meta_projects_title", "Projects browser title", "Projects | Saurabh Gupta"),
        ("meta_contact_title", "Contact browser title", "Contact | Saurabh Gupta"),
        ("site_logo_text", "Logo text", "Saurabh"),
        ("site_logo_accent", "Logo accent text", " Gupta"),
        ("nav_home", "Navigation home label", "Home"),
        ("nav_about", "Navigation about label", "About"),
        ("nav_projects", "Navigation projects label", "Projects"),
        ("nav_contact", "Navigation contact label", "Contact"),
        ("footer_text", "Footer text", "© 2026 Saurabh Gupta. All Rights Reserved."),
        ("home_hero_subtitle", "Home hero subtitle", "Data Analyst | Django Developer"),
        ("home_hero_title", "Home hero title", "Transforming data into insights with Django-driven analytics solutions."),
        ("home_hero_description", "Home hero description", "As a Data Analyst and Django Developer, I turn complex datasets into meaningful business insights by combining data analysis, visualization, and robust web application development."),
        ("home_primary_button", "Home primary button text", "View Projects"),
        ("home_secondary_button", "Home secondary button text", "Contact Me"),
        ("home_hero_image_url", "Home hero image URL", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop"),
        ("home_hero_image_alt", "Home hero image alt text", "Analytics dashboard"),
        ("home_services_eyebrow", "Home services eyebrow", "What I Do"),
        ("home_services_title", "Home services title", "Services"),
        ("about_banner_title", "About banner title", "About Me"),
        ("about_image_url", "About image URL", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop"),
        ("about_image_alt", "About image alt text", "Data analysis workspace"),
        ("about_subtitle", "About subtitle", "Data Analyst | Django Developer"),
        ("about_title", "About heading", "Building validated data pipelines and analytical Django solutions."),
        ("about_intro", "About first paragraph", "I specialize in building data-driven web and analytical solutions using Python, SQL, MySQL, Django, Power BI, Tableau, Advanced Excel, and ETL workflows.\nAs a Django Developer, I work on database-driven web applications, backend logic, structured data models, API-ready workflows, and scalable solutions that convert raw business data into reliable, actionable insights."),
        ("about_focus", "About second paragraph", "As a Data Analyst, I focus on data cleaning, exploratory analysis, statistical analysis, predictive modeling, KPI reporting, and interactive dashboard development."),
        ("about_django", "About third paragraph", "As a Django Developer, I work on database-driven web applications, backend logic, structured data models, API-ready workflows, and scalable solutions that convert raw business data into reliable, actionable insights."),
        ("experience_section_eyebrow", "Experience section eyebrow", "Experience"),
        ("experience_section_title", "Experience section title", "Professional Background"),
        ("foundation_section_eyebrow", "Foundation section eyebrow", "Education & Certifications"),
        ("foundation_section_title", "Foundation section title", "Foundation"),
        ("projects_banner_title", "Projects banner title", "Analytics Projects"),
        ("contact_banner_title", "Contact banner title", "Contact"),
        ("contact_subtitle", "Contact subtitle", "Available for data analytics opportunities"),
        ("contact_title", "Contact heading", "Let's Connect"),
        ("contact_intro", "Contact intro text", "Reach out for data analysis, BI dashboards, SQL reporting, ETL workflows,\nor analytics-focused project collaboration."),
        ("contact_form_name_placeholder", "Contact form name placeholder", "Your Name"),
        ("contact_form_email_placeholder", "Contact form email placeholder", "Your Email"),
        ("contact_form_message_placeholder", "Contact form message placeholder", "Your Message"),
        ("contact_form_button", "Contact form button text", "Send Message"),
        ("contact_success_message", "Contact success message", "Thanks, your message has been saved."),
        ("contact_error_message", "Contact error message", "Please enter your name and email."),
    ]

    for key, label, value in texts:
        SiteText.objects.update_or_create(key=key, defaults={"label": label, "value": value})

    stats = [
        ("268K+", "Records Modeled"),
        ("5+", "Power BI Dashboards"),
        ("40%", "Faster Reporting"),
    ]
    for order, (value, label) in enumerate(stats, start=1):
        Statistic.objects.update_or_create(value=value, label=label, defaults={"order": order, "is_active": True})

    services = [
        ("Business Intelligence", "Interactive dashboards and KPI reporting with Power BI, Tableau, Excel, and SQL."),
        ("Data Analysis & ETL", "Data cleaning, preprocessing, validation rules, and ETL workflows across multiple sources."),
        ("Predictive Modeling", "Statistical analysis, hypothesis testing, risk scoring, and machine learning workflows."),
    ]
    for order, (title, description) in enumerate(services, start=1):
        Service.objects.update_or_create(title=title, defaults={"description": description, "order": order, "is_active": True})

    skills = [
        ("Python, Pandas, NumPy", 92),
        ("SQL & MySQL", 90),
        ("Power BI, Tableau & Excel", 88),
        ("Statistics & Predictive Modeling", 84),
    ]
    for order, (name, percentage) in enumerate(skills, start=1):
        Skill.objects.update_or_create(name=name, defaults={"percentage": percentage, "order": order, "is_active": True})

    experience, _ = Experience.objects.update_or_create(
        title="Data Analyst Training",
        defaults={
            "date_range": "June 2022 - August 2022",
            "organization": "APTRON",
            "location": "Lucknow, Uttar Pradesh, India",
            "order": 1,
            "is_active": True,
        },
    )
    bullets = [
        "Analyzed large datasets using Python and SQL to identify trends and improve data accuracy by 25% through cleaning and preprocessing.",
        "Developed 5+ interactive Power BI dashboards for business metrics, reducing report generation time by 40%.",
        "Performed EDA on 50,000+ customer records to support marketing strategy and customer segmentation.",
        "Built automated Excel reports with advanced formulas and VBA for streamlined weekly reporting.",
        "Implemented ETL workflows to maintain data integrity across business intelligence platforms.",
    ]
    for order, text in enumerate(bullets, start=1):
        ExperienceBullet.objects.update_or_create(experience=experience, text=text, defaults={"order": order, "is_active": True})

    education, _ = InfoCard.objects.update_or_create(
        title="Bachelor of Technology in Computer Science",
        defaults={
            "eyebrow": "August 2019 - June 2023",
            "body": "Babu Banarsi Das University, Lucknow, Uttar Pradesh, India\nRelevant coursework: Data Structures & Algorithms, DBMS, Statistics for Data Science, Machine Learning, Computer Networks.",
            "order": 1,
            "is_active": True,
        },
    )
    certifications, _ = InfoCard.objects.update_or_create(
        title="Professional Learning",
        defaults={
            "eyebrow": "Certifications",
            "body": "",
            "order": 2,
            "is_active": True,
        },
    )
    cert_bullets = [
        "Python Programming: Basic and Advanced Certification",
        "Computer Networking Fundamentals: Network Architecture and Protocols",
    ]
    for order, text in enumerate(cert_bullets, start=1):
        InfoBullet.objects.update_or_create(info_card=certifications, text=text, defaults={"order": order, "is_active": True})

    projects = [
        (
            "Python, MySQL, scikit-learn, Power BI",
            "Credit Risk Analysis & Scoring System",
            "Developed an end-to-end credit risk pipeline across 5 MySQL tables with logistic regression and 4+ engineered business features for automated risk-band scoring.",
            "Implemented 10+ validation rules and a daemon-based workflow, reducing scoring errors by an estimated 30-40% with complete rejection logging and real-time database updates.",
            "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200&auto=format&fit=crop",
            "Credit risk analytics",
        ),
        (
            "MySQL, SQL, Power BI, Python",
            "Sports Analytics: Olympic Games Analysis",
            "Built a normalized Olympic analytics warehouse covering 120 years of data from 1896 to 2016 across 11 relational tables.",
            "Consolidated 268K+ records, 128K+ athletes, 66 sports, and 757 events, then created 17 advanced SQL queries and an interactive Power BI dashboard for medal and participation insights.",
            "https://images.unsplash.com/photo-1517649763962-0c623066013b?q=80&w=1200&auto=format&fit=crop",
            "Sports analytics",
        ),
        (
            "Python, Power BI, SQL",
            "Sales Performance Analytics Dashboard",
            "Built an analytics solution processing 100,000+ transaction records to visualize sales trends, regional performance, and revenue forecasts.",
            "Used Python for preprocessing and SQL optimization to improve query performance by 30%.",
            "https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=1200&auto=format&fit=crop",
            "Sales analytics dashboard",
        ),
        (
            "Python, Machine Learning, Statistical Analysis",
            "Customer Turnover Prediction Model",
            "Developed a predictive model using logistic regression and decision trees to identify at-risk customers with 82% accuracy.",
            "Performed feature engineering and hypothesis testing to find the key factors influencing customer turnover.",
            "https://images.unsplash.com/photo-1555949963-aa79dcee981c?q=80&w=1200&auto=format&fit=crop",
            "Predictive model",
        ),
    ]
    for order, (eyebrow, title, description, extra_description, image_url, image_alt) in enumerate(projects, start=1):
        Project.objects.update_or_create(
            title=title,
            defaults={
                "eyebrow": eyebrow,
                "description": description,
                "extra_description": extra_description,
                "image_url": image_url,
                "image_alt": image_alt,
                "order": order,
                "is_active": True,
            },
        )

    details = [
        ("Email", "saurabhguptagzpofficial@gmail.com", "mailto:saurabhguptagzpofficial@gmail.com"),
        ("Phone", "+91 6387870113", "tel:+916387870113"),
        ("Location", "Varanasi, Uttar Pradesh, India", ""),
        ("LinkedIn", "linkedin.com/in/saurabhguptaofficial", "https://www.linkedin.com/in/saurabhguptaofficial"),
    ]
    for order, (label, value, href) in enumerate(details, start=1):
        ContactDetail.objects.update_or_create(label=label, defaults={"value": value, "href": href, "order": order, "is_active": True})


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_contactdetail_experience_infocard_project_service_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_content, migrations.RunPython.noop),
    ]
