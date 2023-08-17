import json

with open("./InputFiles/Templates/campaign_Nyanza_baseline_202301.json", "r") as file:
    json_str = file.read()
    campaign_json = json.loads(json_str)["Events"]

event_names = list(event["Event_Name"] for event in campaign_json if "Event_Name" in event)
print(event_names)
print(len(event_names))
print(len(set(event_names)))
print(list(event for event in campaign_json if not ("Event_Name" in event)))

event_counter = {}

def clean_filename(filename):
    for illegal_character in [" ","#","/","!"]:
        filename = filename.replace(illegal_character,"-")
    for illegal_character in ["?","*","$","|","=","\\",":"]:
        filename = filename.replace(illegal_character,"")
    return filename.replace("+","-or-")


for event in campaign_json:
    event_name = event["Event_Name"]
    event_name_file = clean_filename(event_name) + ".md"
    with open("../EMOD_Nyanza.wiki/" + event_name_file, "w") as file:
        file.write(f"""
```
{json.dumps(event, indent=4)}
```
""")
    with open("../EMOD_Nyanza.wiki/Model-Events-(campaign.json).md","+a") as campaign_page:
        campaign_page.write(f"- [{event_name}]({event_name_file[:-3]}) \n")
