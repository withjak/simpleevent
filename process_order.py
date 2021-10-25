import os
import json
# our framework
from simpleevent.dispatcher import dispatcher
from simpleevent import condition, action
# user defination of event
from event import Event


def input_reader(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    input_records = input_reader(os.path.join(dir, 'input.json'))


    condition_action_map = [
        (condition.Check('location', 'Pune'), [action.send_alert]),
        (condition.MatchCount('location', 'Banglore', 2), [action.send_alerts, 
                                                           action.print_events])
    ]
    

    for record in input_records:
        print('-'*10)
        print('New record: ', record)
        dispatcher(Event(**record), condition_action_map)
