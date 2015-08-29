elogging
========

Extension for Logging.

This repo is an inspiration that logging system could do more than "logging". When using statistical information aggregation service, like [Riemann](http://riemann.io/), I experienced some inconvenience to integrate its client to my system, which will be described later. Then I came up with the idea to embed the client in a customized log handler. So in this way, statistical sampling is integrated with logging, and thus it can utilize many elegant and flexible machanism in logging system.

<img src="/doc/images/logger_schema.jpg"/>

At this point, I made a Riemann client as a customized log handler "RiemannHandler", which is esstianlly a wrapper on another Riemann client [Bernhard](https://github.com/banjiewen/bernhard). Hope you also feel that it does reduce the work of introducing aggregation service to system. Besides, welcome any kind of contribution, which may include:

- Discuss API design;
- Implement handlers for other stats aggregation systems;
- Other inspirations that logging system could do more than "logging".

Motivation
----------

As a common example, we're gonna stats some API services in our system using Riemann. The code snippet on the left is the original implementation of `get_user_profile` service, while the right is that with stats added.

<img src="/doc/images/user_profile_stats.jpg"/>

This is quite straightforward, however, when we permanently/temporarily decided not to care some services, say the APIs in specific modules/levels, we need to do some work manually, which could be either commenting or adding flag as below. Since the number of these services could be large, the effort is not that pleasant. If we're going to change stats service from Riemann to some its counterpart, the scenario would be worse.

<img src="/doc/images/user_profile_stats_remove.jpg"/>

Now assume there's a log handler which treats log message as stats data(i.e. event in Riemann) and sends it to Riemann, then we can simply do this, where logger in `app.py` issues two logs, one for local file and the other for remote Riemann.

<img src="/doc/images/user_profile_stats_logger.jpg"/>

At this point, we have a global control of stats through `config.py` as logging. For example, we can turn on/off specific log and stats by just changing the level of corresponding logger. Besides, if we're changing Riemann to other implementation, we just need to change the type of handler. 

The full example is in [examples/riemann](/examples/riemann/).

