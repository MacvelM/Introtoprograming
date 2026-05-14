# Hurricane Category Calculator

wind_speed = int(input("Enter the hurricane wind speed in MPH: "))

if wind_speed < 74:
    print("Tropical Storm")

elif wind_speed < 96:
    print("Category 1")

elif wind_speed < 111:
    print("Category 2")

elif wind_speed < 130:
    print("Category 3")

elif wind_speed < 157:
    print("Category 4")

else:
    print("Category 5")