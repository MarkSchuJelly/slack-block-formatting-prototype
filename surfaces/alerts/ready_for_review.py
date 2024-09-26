from surfaces.shared import alert_header

def get_open_and_unreviewed():
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

def get_accepted_and_unmerged():
    return []

def get_with_comments_and_no_approvals():
    return []


def get_data(flag):
    match flag:
        case 0:
            return get_accepted_and_unmerged()
        case 1:
            return get_with_comments_and_no_approvals()
        case _:
            return get_open_and_unreviewed()


def ready_for_review():

    pull_requests = get_data(flag = -1)

    if len(pull_requests) == 0:
        return []

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

