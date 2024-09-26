from shared import message_header

def daily_digest(team):
    return [
        *message_header("Daily Digest", team),
    ]