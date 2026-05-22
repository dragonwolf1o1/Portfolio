from django.contrib import admin

from .models import (
    ContactDetail,
    ContactMessage,
    Experience,
    ExperienceBullet,
    InfoBullet,
    InfoCard,
    Project,
    Service,
    SiteText,
    Skill,
    Statistic,
)


admin.site.site_header = "Saurabh Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage portfolio content"


@admin.register(SiteText)
class SiteTextAdmin(admin.ModelAdmin):
    list_display = ("label", "key", "updated_at")
    search_fields = ("key", "label", "value")
    readonly_fields = ("updated_at",)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("value", "label")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "order", "is_active")
    list_editable = ("percentage", "order", "is_active")
    search_fields = ("name",)


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1
    fields = ("text", "order", "is_active")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "date_range", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "organization", "location")
    inlines = [ExperienceBulletInline]


class InfoBulletInline(admin.TabularInline):
    model = InfoBullet
    extra = 1
    fields = ("text", "order", "is_active")


@admin.register(InfoCard)
class InfoCardAdmin(admin.ModelAdmin):
    list_display = ("title", "eyebrow", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "eyebrow", "body")
    inlines = [InfoBulletInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "languages_used", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "eyebrow", "description", "extra_description", "repo_url", "live_url", "source", "languages_used")


@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("label", "value", "href")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)
