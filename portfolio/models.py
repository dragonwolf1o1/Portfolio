from django.db import models


class SiteText(models.Model):
    key = models.SlugField(max_length=120, unique=True)
    label = models.CharField(max_length=160)
    value = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["key"]
        verbose_name = "Site text"
        verbose_name_plural = "Site text"

    def __str__(self):
        return self.label


class OrderedContent(models.Model):
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class Statistic(OrderedContent):
    value = models.CharField(max_length=80)
    label = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.value} {self.label}"


class Service(OrderedContent):
    title = models.CharField(max_length=160)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skill(OrderedContent):
    name = models.CharField(max_length=160)
    percentage = models.PositiveSmallIntegerField(default=80)

    def __str__(self):
        return self.name


class Experience(OrderedContent):
    date_range = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    organization = models.CharField(max_length=180)
    location = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return self.title


class ExperienceBullet(OrderedContent):
    experience = models.ForeignKey(Experience, related_name="bullets", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


class InfoCard(OrderedContent):
    eyebrow = models.CharField(max_length=120)
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title


class InfoBullet(OrderedContent):
    info_card = models.ForeignKey(InfoCard, related_name="bullets", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:80]


class Project(OrderedContent):
    eyebrow = models.CharField(max_length=180)
    title = models.CharField(max_length=180)
    description = models.TextField()
    extra_description = models.TextField(blank=True)
    image_url = models.URLField(max_length=600)
    image_alt = models.CharField(max_length=160)
    repo_url = models.URLField(max_length=255, blank=True, unique=True, null=True)
    live_url = models.URLField(max_length=600, blank=True)
    source = models.CharField(max_length=80, blank=True)
    languages_used = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def language_list(self):
        return [language.strip() for language in self.languages_used.split(",") if language.strip()]


class ContactDetail(OrderedContent):
    label = models.CharField(max_length=80)
    value = models.CharField(max_length=240)
    href = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.label


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
