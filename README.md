# Format Slack Blocks for Jellyfish Alerts

We are currently working on sending Slack messages to Jellyfish users. Using the Slack Block Kit, you can give these messages style and structure. This is a proof-of-concept repo for showing how you might do that. 

## Explanation 

The file `prototype_v1.py` includes code that gives the basic idea. It's basically a first draft. 

The `surfaces` shows how you might structure the code in a folder. 

# Preview 
You can create a surface and pass it to `open_in_block_kit_builder` in `preview.py`. When you run `python ./preview.py`, it will open the Slack Block Kit Builder and display the surface as if it were in Slack so you can see it for yourself. 
