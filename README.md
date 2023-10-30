# mqtt_rpi

Websocket issues, blocked some firewalls.

## Hive

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/90250e98-7693-4cc4-8c38-bd3213521bac)

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/0c826d90-5146-4931-9095-817e0fc92633)

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/d8c332aa-ca7a-4a4f-85b7-4aa11cf68ddf)

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/23f15ea9-9740-43d8-8fbf-73a81c841957)

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/6ae2b416-55fb-49d4-b3d4-9aa5c96f7d9e)






## EMQX

![image](https://github.com/kode2go/mqtt_rpi/assets/29664888/0bb31043-b236-4b97-9680-199e1bef07bf)


# local

`pip install paho-mqtt`

# rpi

Pin selection:
- Issue: pin 8 was going high on restart, needed to keep it low
-- Resolution: change to pin 10, default low on boot
-- Notes:
- RPi: pin14 on reboot, check all pins and their state:
https://roboticsbackend.com/raspberry-pi-gpios-default-state/
Pin14 - actually 8 so default high?

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

