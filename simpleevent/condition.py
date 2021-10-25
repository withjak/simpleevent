from .condition_base import SingleEventCondition, MultiEventCondition


class Check(SingleEventCondition):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def evaluate(self, event):
        if getattr(event, self.key) == self.value:
            print(f'satisfyied condition: check({self.key!r}, {self.value!r})')
            return True
        return False


class MatchCount(MultiEventCondition):
    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.count = count
    
    def evaluate(self, events):
        matching_events = [event for event in events 
                           if getattr(event, self.key) == self.value]
        
        if len(matching_events) == self.count:
            print(f'satisfyied condition: count({self.key!r}, {self.value!r}, {self.count!r})')
            return matching_events
        
        return []
