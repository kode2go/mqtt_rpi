# mqtt_rpi

Websocket issues, blocked some firewalls.

## Hive

## EMQX

# local

`pip install paho-mqtt`

# rpi

`pip3 install paho-mqtt`

Install issue for client.py was empty, reinstalled using python3

`pip3 show paho-mqtt | grep Location`

`cd path_to_site_packages`

`rm -r ~/.local/lib/python3.9/site-packages/paho/mqtt`


## Debug

`ps aux | grep rpi_gpio_input.py`

`kill 23229`


Run in background:

```
nohup python3 rpi_gpio_input.py
```

