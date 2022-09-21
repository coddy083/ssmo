from django.db import models
from user.models import User

class HolliyDay(models.Model):
    HOURS_CHOICES = (
        ('데이', '데이'),
        ('이브닝', '이브닝'),
        ('시차', '시차'),
        ('휴일', '휴일'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.CharField(max_length=10, choices=HOURS_CHOICES)
    note = models.CharField(max_length=256, blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.user} | {self.date} | {self.hours} | ({self.note})'