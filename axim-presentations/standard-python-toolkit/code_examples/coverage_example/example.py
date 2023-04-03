def traffic_lights(color):
    if color == "green":
        return "go"
    elif color == "yellow":
        return "slow down"
    elif color == "red":
        return "stop"
    else:
        raise Exception("Invalid color")