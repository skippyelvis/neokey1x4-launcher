### neokey1x4 launcher 
launch commands using the [neokey1x4](https://www.adafruit.com/product/4980?gclid=CjwKCAjwuYWSBhByEiwAKd_n_p3Im5-RyBdAVuJLlfFCdXDqdpttX_SAa8f3opPX1C1U_gNAjaz7nxoCfXAQAvD_BwE)

### setup
- clone this repo
- copy `py` files from `device/` onto your CircuitPython 7.X device
- refer to `device/libs.txt` for adafruit/community libraries to load onto device
- copy `neokey-client.py` to your `/usr/bin`
- copy `neokey-client.sh` somewhere on your `$PATH`
- close/re-open or re-source your terminal and run `neokey-client.sh`


### notes
- `neokey-client.sh` starts a process names `neokeyClient`
- confirm client is alive: `pidof neokeyClient` returns integer
- kill the client: `pkill -f neokeyClient`
