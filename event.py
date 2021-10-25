class Event:
    valid_actions = ('purchase', 'order_return')

    def __init__(self, user, action, location):

        # basic checks
        if not isinstance(user, str):
            raise TypeError(f'Expected user of type str instead got {type(user)}')
        if action not in self.valid_actions:
            raise ValueError(f'action must be in {self.valid_actions!r}')
        if not isinstance(location, str):
            raise TypeError(f'Expected location of type str instead got {type(location)}')
        
        self.user = user
        self.action = action
        self.location = location
    
    def __str__(self):
        return f'{self.__class__.__name__}' \
               f'({self.user!r}, {self.action!r}, {self.location!r})'
