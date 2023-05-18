from django.db import models

class Tasks(models.Model):
    user_id = models.CharField(max_length=20)
    added_time = models.DateTimeField(auto_now_add=True)
    do_task = models.CharField(max_length=300)
