from .condition_base import SingleEventCondition


# Global variables are bad practice
# this is just to demonstrate the idea of a dispatcher
event_log = []
def dispatcher(event, condition_action_map):
    event_log.append(event)

    for condn, actions in condition_action_map:
        if isinstance(condn, SingleEventCondition):
            if condn.evaluate(event):
                take_action(event, actions)
        
        else:
            matching_events = condn.evaluate(event_log)
            if matching_events:
                take_action(matching_events, actions)


def take_action(event, actions):
    """Performs action on event
    """
    for action in actions:
        action(event)
