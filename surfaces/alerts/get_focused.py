from surfaces.shared import alert_header

def get_focused():

    def get_data():
        return [
            {
                "name": "Build the Space Shuttle",
                "url": "https://slack.com"
            },
            {
                "name": "Design the Control Center",
                "url": "https://slack.com"
            },
        ]
    
    epics = get_data()

    return [
        alert_header(":dart: Get Focused :dart:"),
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": f"{len(epics)} epics have target dates this week:"
            }
        },
        *map(lambda epic: {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": [
                        {
                            "type": "text",
                            "text": " - "
                        },
                        {
                            "type": "link",
                            "url": epic["url"],
                            "text": epic["name"]
                        }
                    ]
                }
            ]
        }, epics),
        {
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": " " 
			}
		},
        {
			"type": "rich_text",
			"elements": [
				{
					"type": "rich_text_section",
					"elements": [
						{
							"type": "text",
							"text": "Try prioritizing these this week or"
						}
					]
				},
				{
					"type": "rich_text_section",
					"elements": [
						{
							"type": "text",
							"text": "Use Scenario Planner to make a new plan."
						}
					]
				}
			]
		}
    ]