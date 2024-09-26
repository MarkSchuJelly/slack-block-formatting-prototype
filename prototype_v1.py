import json
import requests
from datetime import date
from urllib.parse import quote
import webbrowser

# Questions 
"""
    1. where to query data? especially in the context of company/team variations
    2. where/how to account for variations
    3. is there some kind of send_message config we could create
    4. Figure out conventions, spacing
"""

# Test Utils
def open_in_block_kit_builder(blocks):
    blocks_json = json.dumps({"blocks": blocks})
    URI = quote(blocks_json, safe='~()*!.\'')
    webbrowser.open(f'https://app.slack.com/block-kit-builder/T145KNEH5#{URI}')

def chat_postMessage(channel, blocks): 
    print(blocks)

# Shared

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

# Alerts

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

def ready_for_review():

    def get_data(): 
        requests.get('https://w3schools.com')   # pretend async call for POC
        return [
            {
                "url": "https://slack.com",
                "name": "Super Amazing PR"
            },
            {
                "url": "https://slack.com",
                "name": "Slightly Cool PR"
            },
            {
                "url": "https://slack.com",
                "name": "Most Amazing PR you've ever seen"
            }
        ]
    
    pull_requests = get_data()

    return [
            alert_header(":eyes:  Ready for Review  :eyes:"),
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Our team has some PRs pending! Can you help?"
                }
            },
            *map(lambda pr: {
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
                                "url": pr["url"],
                                "text": pr["name"]
                            }
                        ]
                    }
                ]
            }, pull_requests)
        ]

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


# Messages

def daily_digest(team):
    return [
        *message_header("Daily Digest", team),
    ]

def monday_team_jumpstart(team):
    return [
        *message_header("Monday Team Jumpstart", team),
        *awesome_work_last_week(),
        divider(),
        *ready_for_review(),
        divider(),
        *get_focused()
    ]

# Try It!
open_in_block_kit_builder(
    monday_team_jumpstart('Champy')
)

