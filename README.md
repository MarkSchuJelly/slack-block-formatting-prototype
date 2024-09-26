# Format Slack Blocks for Jellyfish Alerts

We are currently working on sending Slack messages to Jellyfish users. Using the Slack Block Kit, you can give these messages style and structure. This is a proof-of-concept repo for showing how you might do that. 

## Preview 
You can create a surface and pass it to `open_in_block_kit_builder` in `preview.py`. When you run `python ./preview.py`, it will open the Slack Block Kit Builder and display the surface as if it were in Slack so you can see it for yourself. 

## Explanation and Examples

The `prototype_v1.py` file includes code that gives the basic idea. It's basically a first draft. 

The `surfaces` folder shows how you might structure the code in a directory. 

### Example 1

The following surface corresponds to the following code:

#### In Slack

<img width="480" alt="Screenshot 2024-09-26 at 3 54 05 PM" src="https://github.com/user-attachments/assets/0044cf08-5dc8-4b4e-bc67-adcbc782016d">

#### In Code
```python
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
```

### Example 2

The following surface corresponds to the following code:

#### In Slack

<img width="481" alt="Screenshot 2024-09-26 at 3 52 58 PM" src="https://github.com/user-attachments/assets/3630f600-e14a-4539-a70d-958f33395252">

#### In Code

```python
def monday_team_jumpstart(team):
    return [
        *message_header("Monday Team Jumpstart", team),
        *awesome_work_last_week(),
        divider(),
        *ready_for_review(),
        divider(),
        *get_focused()
    ]      
```

