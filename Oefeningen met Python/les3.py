import time

current_time = time.localtime()

print(current_time.tm_hour,":",current_time.tm_min)
if current_time.tm_hour > 12 and current_time.tm_hour < 18:
    print(" Het is ochtend ")
elif current_time.tm_hour <= 12:
    print("Het is middig")
elif current_time.tm_hour >= 18 and current_time < 24:
    print("Het is avond")
    