from shiftbid.models import Shift

def handle_response_submission(shift_chosen, email):
    shift = Shift.objects.get(pk=shift_chosen)
    shift.agent_email = email
    shift.save()