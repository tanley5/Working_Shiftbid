# When the response is given for a particular shift, we encode that response with the agent email provided
# We then get the seniority with the same email address and change the status of that seniority to finished
# When the background task sees that the status of this seniority is finished, the background task will skip this seniority for the next seniority in line

from shiftbid.models import Shift, Seniority, Shiftbid

def handle_response_submission(shift_chosen, email, sb_pk):
    sb = Shiftbid.objects.get(pk = sb_pk)
    shift = Shift.objects.get(pk=shift_chosen)
    shift.agent_email = email
    seniority = Seniority.objects.get(agent_email = email, shiftbid = sb)
    seniority.seniority_status = 'f'
    shift.save()
    # for s in shift:
    #     s.save()
    # seniority.save()
    seniority.save()