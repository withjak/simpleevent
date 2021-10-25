import os
import json
# our framework
from simpleevent.dispatcher import dispatcher
from simpleevent import condition, action
# user defination of event
from event import OrderEvent


def input_reader(filepath):
    '''Read json input from file
    '''
    with open(filepath) as f:
        records = json.load(f)
    return records


if __name__ == '__main__':

    # reading input from file
    dir = os.path.dirname(__file__)
    input_records = input_reader(os.path.join(dir, 'input.json'))

    # to simulate a stream of records comming into the system
    for record in input_records:
        print('-'*10)
        print('New record: ', record)
        dispatcher(OrderEvent(**record))
