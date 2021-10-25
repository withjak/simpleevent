# user defined Event 
from simpleevent import condition as condn
from simpleevent import action as actn
from simpleevent.rules import rules


@rules(mapping = [
    (condn.Check('location', 'Pune'), [actn.send_alert]),
    (condn.MatchCount('location', 'Banglore', 2), [actn.send_alerts, actn.print_events])])
class OrderEvent():
    def __init__(self, user, action, location):
        self.user = user
        self.action = action
        self.location = location
    
    def __str__(self):
        return f'{self.__class__.__name__}' \
               f'({self.user!r}, {self.action!r}, {self.location!r})'
