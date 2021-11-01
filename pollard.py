import random
import math
import time
import helpers


def pollard_find(N):
	x = y = 2 + random.randint(2, 100)
	d = 1
	a = 1
	while d == 1:
		x = (x * x + a) % N
		y = (y * y + a) % N
		y = (y * y + a) % N
		d = math.gcd(N, abs(x - y))
	if d == N:
		return 0
	return d
#


def pollard_factor(N):
	if helpers.probably_prime(N):
		print(N)
		return
	if N < 1000000:
		helpers.trial_factor(N)
		return
	d_1 = 0
	while True:
		d_1 = pollard_find(N)
		if d_1:
			break
	d_2 = N // d_1
	pollard_factor(d_1)
	pollard_factor(d_2)
#	


N = int(input())
print("-------------------------------------------")
start_time = time.time()
pollard_factor(N)
print("Time %s" % (time.time() - start_time))
input()
