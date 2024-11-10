import json
from datetime import datetime, timedelta
import requests
import random

def load_connections():
    update()
    file = open('connections.json')
    connections = json.load(file)
    file.close()

    data = []

    for puzzle in connections:
        answers = puzzle['answers']
        groups = [] # {level: 0, group: group_name, [words]}
        words = []
        for group in answers:
            members = list(map(lambda x: x.lower(), group['members']))
            group_name = group['group']
            level = group['level']
            groups.append({
                "level": level,
                "group": group_name,
                "words": members
            })

            words += members

        random.shuffle(words)

        data.append([words, groups])

    return data

def update():

    file = open('connections.json')
    connections = json.load(file)
    file.close()

    delta = timedelta(days=1)
    date = connections[-1]["date"]
    id = connections[-1]["id"] + 1
    cur_date = datetime.today().date()

    date = datetime.strptime(date, '%Y-%m-%d').date() + delta

    while date <= cur_date:
        # https://github.com/Eyefyre/NYT-Connections-Answers/blob/main/update.py

        con_date = (date.strftime('%Y-%m-%d'))
        if connections[-1]["date"] == con_date:
            print(f"Connection #{id - 1} from {con_date} already exists in file, exiting")
            return

        URL = f"https://www.nytimes.com/svc/connections/v1/{con_date}.json"
        r = requests.get(URL)

        content = json.loads(r.content)
        print(f"Adding Connection #{id} from {con_date}")
        groups = []
        for group in content["groups"]:
            categ = {"level": content["groups"][group]["level"], "group": group,
                     "members": content["groups"][group]["members"]}
            groups.append(categ)

        con_item = {"id": int(id), "date": con_date, "answers": groups}
        connections.append(con_item)

        date += delta
        id += 1

    with open('connections.json', 'w') as f:
        json.dump(connections, f, indent=4)
        f.close()
