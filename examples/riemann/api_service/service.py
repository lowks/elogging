
import logging
import random
import time
import config

from socket import gethostname
from flask import Flask 
from elogging.util import profile

app = Flask(__name__) 
logger = logging.getLogger('riemann')

@profile
def query_user_table(uid):
    time.sleep(random.uniform(1.0,3.0))
    return 'Bob'

@app.route("/")
def hello(): 
    return "Hello World!"

@app.route('/user/<uid>') 
def get_user(uid=None, methods=['GET']): 
    user = query_user_table(uid)
    logger.info('query user %s', uid,
                extra={'event':{'host': gethostname(),
                                'service': 'get_user',
                                'state': 'ok',
                                'time': int(time.time()),
                                'metric': query_user_table.stats()}})
    return user

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True) 

