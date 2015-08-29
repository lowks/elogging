
Service with Riemann Handler
============================

`api_service` is a demo service with riemann handler doing stats work. It serves a single API `get_user` which is defined in `app.py`. Setting for logging system is in `config.py`.

Setup Riemann
-------------

Setup riemann daemon as well as riemann dashboard, as described in http://riemann.io/quickstart.html.

```
$ bin/riemann etc/riemann.config
```

In another terminal,

```
$ gem install riemann-dash
$ riemann-dash
```

Use browser http://localhost:4567 to config the dashboard. Follow its instructions and turn the title to a time series view, which will show `get_user` service stats.

<img src="/doc/images/riemann_dash_config.jpg"/>


Run Demo
--------

```
$ cd api_service
$ pip install -r requirements.txt
$ python service.py
```

Then we can trigger API request [http://localhost:5000/user/1](http://localhost:5000/user/1) in browser multiple times. Then we will get this in dashboard.

<img src="/doc/images/riemann_dash_timeseries.jpg"/>

As we also configured a `RollingFileHandler` for the logger, we will also see this from `riemann_event.log`.

```
2015-08-29 12:15:03,607 [INFO] riemann: query user 1 {'host': 'mzhang.PK5001Z', 'metric': 1.2871589660644531, 'state': 'ok', 'service': 'get_user', 'time': 1440875703}
2015-08-29 12:15:07,377 [INFO] riemann: query user 1 {'host': 'mzhang.PK5001Z', 'metric': 2.096153974533081, 'state': 'ok', 'service': 'get_user', 'time': 1440875707}
2015-08-29 12:15:12,672 [INFO] riemann: query user 1 {'host': 'mzhang.PK5001Z', 'metric': 2.69396710395813, 'state': 'ok', 'service': 'get_user', 'time': 1440875712}
2015-08-29 12:15:16,086 [INFO] riemann: query user 1 {'host': 'mzhang.PK5001Z', 'metric': 1.7106781005859375, 'state': 'ok', 'service': 'get_user', 'time': 1440875716}
2015-08-29 12:15:20,322 [INFO] riemann: query user 1 {'host': 'mzhang.PK5001Z', 'metric': 1.496399164199829, 'state': 'ok', 'service': 'get_user', 'time': 1440875720}
```

