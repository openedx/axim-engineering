from example import traffic_lights

def test_traffic_lights_green():
    assert traffic_lights('green') == "go"

def test_traffic_lights_yellow():
    assert (
        traffic_lights('yellow') == "slow")
