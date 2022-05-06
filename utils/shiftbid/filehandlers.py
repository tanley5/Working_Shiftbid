from shiftbid.models import Shift, Seniority, Shiftbid
import pandas as pd

def handleShiftFile(shiftBid, file):
    #sb = Shiftbid.objects.get(shiftBid)
    shiftFile = pd.read_excel(file)

    for i, row in shiftFile.iterrows():
        shiftDescription = row["Shift Description"]
        shift = Shift.objects.create(shift_description = shiftDescription,shiftbid = shiftBid)
        shift.save()

def handleSeniorityFile(shiftBid, file):
    #sb = Shiftbid.objects.get(shiftBid)
    seniorityFile = pd.read_excel(file)

    for i, row in seniorityFile.iterrows():
        seniorityNumber = row["Seniority Number"]
        agentName = row["Agent Name"]
        agentEmail = row["Agent Email"]
        seniority = Seniority.objects.create(seniority_number = seniorityNumber, agent_name = agentName, agent_email = agentEmail, shiftbid = shiftBid)
        seniority.save()

