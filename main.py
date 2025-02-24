from pymavlink.dialects.v20 import ardupilotmega

def test(msg: ardupilotmega.MAVLink_ahrs3_message):
    print(msg.altitude)
