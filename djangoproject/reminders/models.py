# reminders/models.py
# from django.db import models
# from datetime import datetime

# class Reminder(models.Model):
#     date = models.DateField()
#     time = models.TimeField(auto_now_add=True)
#     current_time = datetime.now().strftime('%H:%M:%S')
#     message = models.TextField()
#     reminder_type = models.CharField(max_length=10, choices=[('SMS', 'SMS'), ('Email', 'Email')])
    

#     def __str__(self):
#         return self.message

from django.db import models

class Reminder(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=[('SMS', 'SMS'), ('Email', 'Email')])

    def __str__(self):
        return self.message
