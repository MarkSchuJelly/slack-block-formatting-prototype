from surfaces.shared import alert_header

def awesome_work_last_week():

    def get_data():
        return {
            "sprint_completion": 53, 
            "epic_completed": "Sketch the space shuttle"
        }
    
    sprint_completion, epic_completed = get_data().values()

    return [
        alert_header(":tada: Awesome Work Last Week  :tada:"),
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*{sprint_completion}%* of the sprint is complete."
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"_{epic_completed}_ *epic was completed!*"
			}
		}
    ]