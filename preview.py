import json
from urllib.parse import quote
import webbrowser
from surfaces.messages.monday_team_jumpstart import monday_team_jumpstart 

def open_in_block_kit_builder(blocks):
    blocks_json = json.dumps({"blocks": blocks})
    URI = quote(blocks_json, safe='~()*!.\'')
    webbrowser.open(f'https://app.slack.com/block-kit-builder/T145KNEH5#{URI}')

# Try It!
open_in_block_kit_builder(
    monday_team_jumpstart('Champy')
)