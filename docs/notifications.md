# introduction

A notification library for sending notifications across a variety of deleivery channels.


## implement a notification.

via method returns an array of channel class names
to_<thing> method should return our message for the channel to send.

### included channels
- email (django)
- db (django)
- sms (twilio)
- push (?)

### signals
- canceled
- scheduled
- sending
- retrying
- sent
- failed

### queueing
 . drivers
    - django Q
    - celery
    - django db ???
 . features
    - Throttling
    - Scheduling
    - Retrys
    - Canceling
    - Batching.