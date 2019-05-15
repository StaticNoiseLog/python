import math


k = 0.081 * -5 - 2.673

print("Pi in scientific notation: %f" % math.pi)')



while True:
    wind_speed_kmh = float(input("Wind speed km/h: "))
    wind_speed_ms = wind_speed_kmh/3.6
    felt_temperature = 33 + (5.49 * math.sqrt(wind_speed_ms) + 5.81 - 0.56*wind_speed_ms)*(0.081 * -5 - 2.673)
    print('Felt temperature: ', felt_temperature)



