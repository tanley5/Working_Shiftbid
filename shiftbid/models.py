from django.db import models

class Shiftbid(models.Model):
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

class Seniority(models.Model):
    seniority_number = models.PositiveIntegerField()
    agent_name = models.CharField(max_length=50)
    agent_email = models.EmailField()

    shiftbid = models.ForeignKey(Shiftbid, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.agent_name} with seniority number {self.seniority_number}"

class Shift(models.Model):
    shift_description = models.CharField(max_length= 100)
    agent_email = models.EmailField(null=True)
    shiftbid = models.ForeignKey(Shiftbid, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shift_description}"