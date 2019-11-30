import datetime

x = 2
count = 0
start = datetime.datetime.now()
primeNumber = 0

try:
	while True:
		prime = True
		for i in range(2, x+1):
			if(x % i == 0):
				if(not x == i):
					 prime = False
				else:
					if(prime):
						primeNumber = x
						count += 1
						now = datetime.datetime.now()
						try: latest
						except NameError: latest = now.timestamp() * 1000
						newest = now.timestamp() * 1000
						between = newest - latest
						latest = newest
						try: avg
						except NameError: avg = between
						avg = (avg + between) / 2
						hour = str(now.hour)
						minute = str(now.minute)
						second = str(now.second)
						if(len(str(hour)) == 1):
							hour = "0" + str(now.hour)
						if(len(str(minute)) == 1):
                                                        minute = "0" + str(now.minute)
						if(len(str(second)) == 1):
                                                        second = "0" + str(now.second)
						print("[" + hour + ":" + minute + ":" + second + "] " + str(x))
		x += 1
except:
	end = datetime.datetime.now()
	estimatedTime = end - start
	secondsRan = estimatedTime.total_seconds()
	seconds = secondsRan
	minutes = seconds / 60
	hours = minutes / 60
	days = hours / 24
	if(seconds <= 60):
		print("\rran for: " + str(int(seconds)) + " second(s)")
	if(seconds <= 3600 and seconds > 60):
		print("\rran for: " + str(int(minutes)) + " minute(s)")
	if(seconds <= 86400 and seconds > 3600):
		print("\rran for: " + str(int(hours)) + " hour(s)")
	if(seconds <= 315360000 and seconds > 86400):
		print("\rran for: " + str(int(days)) + " day(s)")
	print("amount: " + str(count) + ", highest: " + str(primeNumber) + ", last try (ms): " + str(int(between)) + ", average per try (ms): " + str(int(avg)))
	exit()
