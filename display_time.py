# program to display time
# version 14.07.2021 at 21:39
# Author Alphonse Brandon

time_in_seconds = int(input("what is the number of seconds"))

hours = time_in_seconds // 3600

seconds_remaining = time_in_seconds % 3600

minutes = seconds_remaining // 60

seconds_left = seconds_remaining % 60

print(f"hrs: {hours} mins: {minutes} secs: {seconds_left}")

