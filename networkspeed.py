import psutil as ps
import time
import sys

last_down = 0
last_up = 0
new_down = 0
new_up = 0

try:
    time_stop = float(sys.argv[1])
except:
    print("Enter an argument for time example: python3 networkspeed.py 5 ")
    exit(0)

def down():
    network = ps.net_io_counters()
    down = network.bytes_sent
    return down


def up():
    network = ps.net_io_counters()
    up = network.bytes_recv
    return up


while True:
    if last_down == 0:
        new_down = 0
    else:
        new_down = round((down() - last_down) / 1000, 1)

    if last_up == 0:
        new_up = 0
    else:
        new_up = round((up() - last_up) / 1000, 1)

    last_down = down()
    last_up = up()

    print("Down:{} KiB/s Up:{} Kib/s".format(new_down, new_up))
    time.sleep(time_stop)
