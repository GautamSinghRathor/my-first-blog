from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
#post is object name
#model.Model is a django model so model knows it should save in database
#models.CharField : defines char with limited number
#models.TextField : this is for long text without a limit
#models.DateTimeField : for date and time
#mdoels.ForeignKey : this is a link to another field

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title