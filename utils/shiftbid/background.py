from re import sub
from shiftbid.models import Shiftbid,Seniority,Shift
from django.db.models import Min
from django.core.mail import send_mail
from django.conf import settings

# The purpose of this file is to hold the function that will run in the background
# 1. We give the condition to stop the task
# 2. We give the last task on closing
# 3. We then determine the condition to start
# 4. We give the task to run when the task is not closed

# main runner function
def BackgroundTaskFunction():
    # shiftbids = Shiftbid.objects.filter(shift_status = 's')
    # The line below is for testing only. Use the line above for production
    shiftbids = Shiftbid.objects.filter(shift_status = 'c')
    if len(shiftbids) == 0:
        print("No Shiftbids")
        return
    else:
        for sb in shiftbids:
            print(GroupingObjectsToShiftbid(sb))

# Grouping objects to the Shiftbid
def GroupingObjectsToShiftbid(sb):
    shifts = Shift.objects.filter(shiftbid = sb)
    seniorities = Seniority.objects.filter(shiftbid = sb)
    WorkingFunction(shifts=shifts,seniorities=seniorities,shiftbid=sb)
    return f"{sb.shiftbid_name} Grouping Complete"

# Knowing when to end the tasks by seeing if the length of seniorit is equals to the length of shifts with "not null" agent email
def WorkingFunction(shifts, seniorities, shiftbid):
    seniority_length = len(seniorities)
    filled_shift_length = len([filled_sh_len for filled_sh_len in shifts if filled_sh_len.agent_email != None])
    if seniority_length == filled_shift_length:
        print("Complete")
        LastTaskPriorToClosing(shiftbid)
    else:
        ShiftbidStartingProcedure(shifts=shifts,seniorities=seniorities,shiftbid=shiftbid)
        print("Not Complete")

# The last task when a project has been completed
def LastTaskPriorToClosing(shiftbid):
    # send email with the file to Admin
    sb_name = shiftbid.shiftbid_name

    subject = f"{sb_name} Shiftbid Completed"
    send_mail(subject=subject, message="Shiftbid Complete. Check the following link.",from_email="admin@email.com", recipient_list=["recipient@email.com"])
    # switch shiftbid status to "completed"
    shiftbid.shift_status = 'c'
    shiftbid.save()
    pass

# The starting condition
def ShiftbidStartingProcedure(shifts,seniorities,shiftbid):
    # get all the seniority statuses
    # if there is seniority with 'sent' status, that means we are still waiting for a reply from the 'sent' person
    # if there are non witht he sent status, we will filter the 'unassigned_seniorities' to find the lowest seniority_number
    # We then get the object's email 
    # after sending the email with link we change the seniority_status to 'sent'
    unassigned_seniority = seniorities.filter(seniority_status = 'c')
    assigned_seniority = seniorities.filter(seniority_status = 'f')
    sent_seniority = seniorities.filter(seniority_status = 's')

    if len(sent_seniority) == 0:
        staged_seniority = unassigned_seniority.get(seniority_number = (unassigned_seniority.aggregate(Min('seniority_number'))['seniority_number__min']))
        staged_seniority_email = staged_seniority.agent_email
        # send email
        # Email Content Data
        sb_pk = shiftbid.id
        sb_name = shiftbid.shiftbid_name
        
        subject = f"{sb_name} Shiftbid"
        message = f"Please Access The Shiftbid On This Link: localhost:8000/sb/response/{sb_pk}"
        send_mail(subject = subject,message = message,from_email='admin@email.com',recipient_list=['test@email.com'],)
    
        # switch the staged_seniority to 'sent' status
        # staged_seniority.seniority_status = 's'
        # staged_seniority.save()
    else:
        pass
