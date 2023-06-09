from django.db import models

class NovelModel(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    chapters = models.IntegerField(default=0,)
    views = models.IntegerField(default=0, blank=True, db_index=True)
    cover_url = models.CharField(max_length=10000, default="")
    info = models.JSONField()
    data = models.JSONField()
    last_edited = models.CharField(max_length=1000, default=0)

    def __str__(self):
        return self.name
