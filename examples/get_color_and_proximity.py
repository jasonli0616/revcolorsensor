import revcolorsensor

# pip3 install revcolorsensor
# sudo pigpiod

sensor = revcolorsensor.get_color_sensor()

color = sensor.get_color()
proximity = sensor.get_proximity() # 0 to 2047 range

print("Red: {}".format(color.red))
print("Blue: {}".format(color.blue))
print("Green: {}".format(color.green))
print("Proximity: {}".format(proximity))