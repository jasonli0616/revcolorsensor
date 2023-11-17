import revcolorsensor

# pip3 install revcolorsensor
# sudo pigpiod

sensor = revcolorsensor.getColorSensor()

color = sensor.getColor()
proximity = sensor.getProximity() # 0 to 2047 range

print("Red: {}".format(color.red))
print("Blue: {}".format(color.blue))
print("Green: {}".format(color.green))
print("Proximity: {}".format(proximity))