from shiftbid.models import Shiftbid,Seniority,Shift

# The purpose of this file is to hold the function that will run in the background
# 1. We give the condition to stop the task
# 2. We give the last task on closing
# 3. We then determine the condition to start
# 4. We give the task to run when the task is not closed

# main runner function
def BackgroundTaskFunction():
    shiftbids = Shiftbid.objects.filter(shift_status = 's')
    # The line below is for testing only. Use the line above for production
    #shiftbids = Shiftbid.objects.filter(shift_status = 'c')
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
    # switch shiftbid status to "completed"
    # shiftbid.shift_status = 'c'
    # shiftbid.save()
    pass

# The starting condition
def ShiftbidStartingProcedure(shifts,seniorities,shiftbid):
    # get all started/running shiftbids
    # 
    pass
