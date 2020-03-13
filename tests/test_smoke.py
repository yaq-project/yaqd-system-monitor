import time
import yaqc


def test_nothing():
    c = yaqc.Client(38000)
    c.measure()
    while c.busy():
        time.sleep(0.1)
    assert c.get_measured()
