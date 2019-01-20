import tbapy
import config

tba = tbapy.TBA(config.TBA_TOKEN)

def check_valid_team(team_number):
    team = tba.team(team_number)
    if "Errors" in team:
        return False
    else:
        return True

def check_valid_event(event_id):
    event = tba.event(event_id)
    if "Errors" in event:
        return False
    else:
        return True
