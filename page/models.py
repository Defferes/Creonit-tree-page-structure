from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Page(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    url = models.SlugField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug.lower()
        if self.parent:
            self.url = f"{self.parent.get_full_url}{self.slug}/"
        else:
            self.url = f"/{self.slug}/" if self.slug else "/"
        super(Page, self).save(*args, **kwargs)

    @property
    def get_full_url(self):
        if self.parent:
            return f"{self.parent.get_full_url}{self.slug}/"
        return f"/{self.slug}/"
