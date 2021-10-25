# Simpleevent

Think of simpleevent as a framework. Where user defines:
- `Event`
- `Condition`
    - For evaluating a single event
    - For evaluating a group of events
- `Action`
- `condition-actions mapping`

The framework trys to do 2 things:
1. Evaluating `condition` as an `event` (or events) happen and then takes designated `actions` as specified in `condition-actions mapping`.
2. Provide a simple interface to define action and condition.

## Features

- Complete freedom to user to define what he means by a event. 
- User can define multiple types of event.

## TODO
- mechanism to evaluate whether condition-actions mapping makes sense or not.
- A way to associate event type with condition and actions

## How to use

Clone the repo
```
$ cd simpleevent
$ python process_order.py
```


## License

MIT

