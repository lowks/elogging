
import logging
import logging.config

log_config = {
        'version': 1,
        'formatters': {
            'standard': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},
            'riemann_event': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s %(event)s'}
            },
        'handlers': {
            'console': {'formatter': 'standard', 'class': 'logging.StreamHandler'},
            'riemann_local': {
                'level': 'INFO',
                'formatter': 'riemann_event',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'midnight',
                'backupCount': 10,
                'filename': 'riemann_event.log'
                },
            'riemann_handler': {
                'class': 'elogging.handlers.riemann.RiemannHandler',
                'host': 'localhost',
                'port': 5555
                }
            },
        'loggers': {
            'root': {'handlers': ['console'], 'level': 'INFO'},
            'riemann': {
                'handlers': ['riemann_local', 'riemann_handler'],
                'level': 'INFO'
                }
            }
        }

logging.config.dictConfig(log_config)
