import psutil

battery = psutil.sensors_battery()
print("Battery Percentage:", battery.percent)
