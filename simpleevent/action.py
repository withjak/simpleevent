# single event actions
def send_alert(event):
    print('    send_alert :', event)


def print_event(event):
    print('    print_event: ', event)


# multi event actions
def send_alerts(events):
    for event in events:
        send_alert(event)


def print_events(events):
    for event in events:
        print_event(event)