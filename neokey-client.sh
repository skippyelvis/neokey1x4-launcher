#!/bin/bash
cmd="python3 /usr/bin/neokey-client.py ${1} > /dev/null &"
name="neokeyClient"
pkill -f $name
bash -c "exec -a ${name} ${cmd}"
