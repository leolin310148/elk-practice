import logging
import logstash
import sys
import random
import time

host = 'logstash'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
# test_logger.addHandler(logstash.LogstashHandler(host, 50000, version=1))
test_logger.addHandler(logstash.TCPLogstashHandler(host, 50000, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')


taiwan_cities = ['Taipei', 'New Taipei', 'Taoyuan', 'Taichung', 'Tainan']

# Generate and send random data every second
while True:
    # Generate some random data
    data = {'temperature': random.randint(0, 100),
            'humidity': random.randint(0, 100),
              'city': random.choice(taiwan_cities)}


    # Send data to Logstash
    test_logger.info('random_data', extra=data)

    print('loop')
    time.sleep(5)