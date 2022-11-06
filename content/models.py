from django.db import models


class BaseModel(models.Model):
    user = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Content(BaseModel):
    title = models.CharField(max_length=50, blank=False, null=False)
    context = models.TextField(blank=False, null=False)


class Rate(BaseModel):
    rate = models.IntegerField(blank=False, null=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
