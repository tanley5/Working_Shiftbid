from django.db import models

class Shfitbid(models.Model):
    SHIFTSTATUS = (
        ('c','created'),
        ('s','started'),
        ('e','stopped')
    )
    
    shiftbid_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    shift_status = models.CharField(max_length=1,choices=SHIFTSTATUS, default='c')

    def __str__(self):
        return f"Shiftbid: {self.shiftbid_name}"
