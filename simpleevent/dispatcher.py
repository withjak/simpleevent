from .condition_base import SingleEventCondition, MultiEventCondition


# Global variables are bad practice
# this is just to demonstrate the idea of a dispatcher
event_log = []

def dispatcher(event):
    '''
    Checks which single event condition evaluates to True for this event.
    Also checks which multi event conditions evaluates to True considering 
    all events till now
    '''
    event_log.append(event)

    for condn, actions in event.condn_actn_mapping:

        if isinstance(condn, SingleEventCondition):
            if condn.evaluate(event):
                take_action(event, actions)
        
        elif isinstance(condn, MultiEventCondition):
            matching_events = condn.evaluate(event_log)
            if matching_events:
                take_action(matching_events, actions)


def take_action(event, actions):
    """Performs action on event
    """
    for action in actions:
        action(event)
