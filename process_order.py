import os
import json
# our framework
from simpleevent.dispatcher import dispatcher
from simpleevent import condition, action
# user defination of event
from event import Event


def input_reader(filepath):
    '''Read json input from file
    '''
    with open(filepath) as f:
        records = json.load(f)
    return records


if __name__ == '__main__':

    # user defining what actions to take when a condition is met.
    condition_action_map = [
        (condition.Check('location', 'Pune'), [action.send_alert]),
        (condition.MatchCount('location', 'Banglore', 2), [action.send_alerts, action.print_events])
    ]
    
    # reading input from file
    dir = os.path.dirname(__file__)
    input_records = input_reader(os.path.join(dir, 'input.json'))

    # to simulate a stream of records comming into the system
    for record in input_records:
        print('-'*10)
        print('New record: ', record)
        dispatcher(Event(**record), condition_action_map)
