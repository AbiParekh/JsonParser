import json

#Edited by: Abhishek Parekh

# Define a class to represent event objects
class Obj:
    def __init__(self, date, neutral, vis_team_name, vis_stats, home_team_name, home_stats, is_final):
        self.date = date
        self.neutral = neutral
        self.vis_team_name = vis_team_name
        self.vis_stats = vis_stats
        self.home_team_name = home_team_name
        self.home_stats = home_stats
        self.is_final = is_final

# Function to fetch values from a nested JSON structure
def fetch_json_vals(data, fetch):
    fetch_vals = fetch.split('.')
    result = data
    try:
        for item in fetch_vals:
            if isinstance(result, list):
                item = int(item)
            result = result[item]
        return result
    except (IndexError, KeyError, ValueError):
        return None

# Function to add new data to the JSON dataset
def add_data(data, event, updatedFile):
    data.append(event)
    # Write the updated data to a JSON file
    with open(updatedFile, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    # Load JSON data from the dataset
    with open('49ers.json') as json_file:
        data = json.load(json_file)

    obj_list = []

    # Iterate through each event object in the dataset
    for event in data:
        event_instance = Obj(
            date=event['date'],
            neutral=event['neutral'],
            vis_team_name=event['visTeamName'],
            vis_stats=event['visStats'],
            home_team_name=event['homeTeamName'],
            home_stats=event['homeStats'],
            is_final=event['isFinal']
        )
        obj_list.append(event_instance)

        # Print event information
        print("Game Date:", event['date'])
        print("Neutral:", event['neutral'])
        print("Visitor Team Name:", event['visTeamName'])
        print("Visitor Stats:", event['visStats'])
        print("Home Team Name:", event['homeTeamName'])
        print("Home Stats:", event['homeStats'])
        print("Is Final:", event['isFinal'])
        print("=" * 10)

    # Define new values to be added to the dataset
    new_vals = {
        "neutral": True,
        "visTeamName": "Iron Man",
        "visStats": {
            "statIdCode": "000000000000000",
            "gameCode": "49494949494994449",
            "teamCode": 888,
            "gameDate": "Aug 7th, 2023",
            # can add other values here
        },
        "homeTeamName": "Freedom Fighters",
        "homeStats": {
            "statIdCode": "12121234343445",
            "gameCode": "344534645677568678",
            "teamCode": 343,
            "gameDate": "Aug 7th, 2023",
            # can add other values here
        },
        "isFinal": False,
        "date": "2023-08-07"
    }

    updatedFile = "updatedData.json"
    add_data(data, new_vals, updatedFile)

    # convert from list of dict to JSON str
    json_data = json.dumps(data, indent=4)
    print(json_data)

    # querying JSON data
    fetch = "visTeamName"
    output = fetch_json_vals(data, fetch)
    print("Your results from query: ", output)

    fetch = "visStats.gameCode"
    output = fetch_json_vals(data, fetch)
    print("Your results from query: ", output)


if __name__ == "__main__":
    main()

