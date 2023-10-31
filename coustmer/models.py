from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class TemplatesName(models.Model):
    templatename = models.CharField(max_length=50)
    templateimage = models.ImageField()
    class Meta:
        verbose_name_plural = "Templates"
    def __str__(self):
        return self.templatename


class CoustmerDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forpdf  = models.FileField(max_length=100)
    image = models.ImageField()
    title = models.CharField(max_length=50)
    companyname = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=10)
    proposalsummary = models.TextField()
    projectplanning = models.TextField()
    financing = models.TextField()
    created_at = models.DateField(auto_now=True,editable=True)
    additionalcustomsections = models.TextField()
    templatesdetail = models.ForeignKey(TemplatesName, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Title"
    def __str__(self):
        return self.title


