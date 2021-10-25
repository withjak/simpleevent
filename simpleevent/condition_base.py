from functools import wraps
import inspect
from abc import ABC, abstractmethod

def monitor(method):
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.already_occured:
            return []
        rv = method(self, *args, **kwargs)
        if rv:
            self.already_occured = True
        return rv
    return wrapper


class mytype(type):
    def __call__(cls, *args, **kwargs):
        cls_obj_obj = super().__call__(*args, **kwargs)
        
        # track if multi event condition has already been stasfyied
        # to avaoid triggering again and again on recieveing new events.
        cls_obj_obj.already_occured = False
        
        if cls_obj_obj in cls.instances:
            return [obj for obj in cls.instances if obj == cls_obj_obj ][0]
        cls.instances.append(cls_obj_obj)
        
        return cls_obj_obj

class MultiEventCondition(metaclass=mytype):
    '''Base class for all conditions evaluating a group of events.
    '''
    instances = []
    
    def __eq__(self, other):
        sig = inspect.signature(self.__init__)
        for param in sig.parameters.keys():
            if getattr(self, param) != getattr(other, param):
                return False
        return True
    
    # called when sub-call is created. NOT when object of sub-call is created
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)    
        
        evaluate_method = getattr(cls, 'evaluate', None)
        if evaluate_method:
            setattr(cls, 'evaluate', monitor(evaluate_method))
        else:
            raise NotImplementedError(f'Expected method: evaluate(self, events)')


class SingleEventCondition(ABC):
    '''Base class for all condition dealing with evaluating single event.
    '''
    @abstractmethod
    def evaluate(self, event):
        pass
