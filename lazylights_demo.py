import lazylights
import time

bulbs = lazylights.find_bulbs(expected_bulbs=2)

lazylights.set_power(bulbs, True)
lazylights.set_power(bulbs, False)
time.sleep(2)
lazylights.set_power(bulbs, True)