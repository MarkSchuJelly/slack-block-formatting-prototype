from surfaces.shared import message_header, divider
from surfaces.alerts.get_focused import get_focused
from surfaces.alerts.awesome_work_last_week import awesome_work_last_week
from surfaces.alerts.ready_for_review import ready_for_review

def monday_team_jumpstart(team):
    return [
        *message_header("Monday Team Jumpstart", team),
        *awesome_work_last_week(),
        divider(),
        *ready_for_review(),
        divider(),
        *get_focused()
    ]