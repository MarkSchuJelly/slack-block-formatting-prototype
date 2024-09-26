from datetime import date

def divider():
    return {
        "type": "divider"
    } 

def message_header(title, team):
    
    today = date.today().strftime("%B %d, %Y")

    return [
        {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": title,
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
                    "text": f"*{today}*"
				},
				{
					"type": "mrkdwn",
					"text": "|"
				},
				{
					"type": "mrkdwn",
					"text": f"Team {team}"
				}
			]
		},
        divider()
    ]

def alert_header(title):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f'*{title}*'
        }
    }