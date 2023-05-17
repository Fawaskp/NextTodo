from django.db import models

class Tasks(models.Model):
    session_id = models.CharField(max_length=20)
    added_time = models.DateTimeField(auto_created=True)
    do_task = models.CharField(max_length=300)
