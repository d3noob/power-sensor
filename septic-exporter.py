import prometheus_client
import time

UPDATE_PERIOD = 15

current = prometheus_client.Gauge('septic_current_milliamps',
          'Value relating to current flow with zero being effectivly nil.')

if __name__ == '__main__':
  prometheus_client.start_http_server(9999)
  
while True:
  with open('/home/pi/current.txt', 'r') as f:
    current_value = f.readline()
    try:
      float(current_value)
      current.set(float(current_value))
    except: pass

  time.sleep(UPDATE_PERIOD)
