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
2. Provide a simple interface to define `action` and `condition`.

## How to use

Clone the repo
```
$ cd simpleevent
$ python process_order.py
```

## Story
Whenever a shopper places an order (to purchase/return an item), you recieve 
a record containing following information:
- name : of the shopper
- action : that the shopper took. Which is either `purchase` or `return_order`
- location

Now as a developer you want to analyze these records both `individually` (was this record a purchase?) and as a `collection` (have we had our first 10,000 orders from Pune yet?).

So you come across of this framework called `sendevent` which can help you do the same. So you start using it.
1. You define what you mean by event (for you it is a record)
2. You can use the predefined actions or conditions OR 
3. Define your own conditions for handling single and multiple events
4. Similarly you define actions
5. Finally you provide a mapping between what actions to take when a condition is met.
6. Now, give this mapping to `dispatcher` function.

> You implemented the same in `process_order.py`.

## Features

- User can define multiple types of event.
- Multiple actions can be executed once a condition is met.
##### TODO
- mechanism to evaluate whether condition-actions mapping makes sense or not.
- A way to associate event type with condition and actions


## License

MIT

