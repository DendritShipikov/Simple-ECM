import random
import math
import time
import helpers



def add(x_p, z_p, x_q, z_q, x_r, z_r, m):
	u = (x_p - z_p) * (x_q + z_q)
	v = (x_p + z_p) * (x_q - z_q)
	uv = u + v
	x_pq = z_r * uv * uv % m
	uv = u - v
	z_pq = x_r * uv * uv % m
	return x_pq, z_pq
#


def dup(x_p, z_p, a, m):
	u = x_p * x_p 
	v = z_p * z_p
	w = x_p * z_p
	z_2p = 4 * w * (u + v + a * w) % m
	w = u - v
	x_2p = w * w % m
	return x_2p, z_2p
#


def mul(x_0, z_0, k, a, m):
	x_q, z_q = x_0, z_0
	x_p, z_p = dup(x_0, z_0, a, m)

	k_binary = bin(k)

	s = len(k_binary)
	for i in range(3, s):
		if k_binary[i] == '1':
			x_q, z_q = add(x_q, z_q, x_p, z_p, x_0, z_0, m)
			x_p, z_p = dup(x_p, z_p, a, m)
		else:
			x_p, z_p = add(x_q, z_q, x_p, z_p, x_0, z_0, m)
			x_q, z_q = dup(x_q, z_q, a, m)
	return x_q, z_q
#


def elliptic_find(N, B, M):
	primes = helpers.prime_sieve(M)
	k = 1
	B_log = math.log(B)
	p_B = 0
	for p in primes:
		if p < B:
			p_B += 1
			k *= pow(p, int(B_log / math.log(p)))
	for _ in range(0, 10000):	
		g = N
		while g == N:
			x, z = random.randint(0, N - 1), random.randint(0, N - 1)
			a = random.randint(0, N - 1)
			b = (x * x * x + a * x * x * z + x * z * z) % N
			g = math.gcd((a * a - 4) * b, N)
		if g > 1:
			return g
		x, z = mul(x, z, k, a, N)
		if x == 0 and z == 0:
			continue	
		g = math.gcd(z, N)
		if 1 < g < N:
			return g
		for p in primes[p_B : ]:
			x, z = mul(x, z, p, a, N)
			if x == 0 and z == 0:
				break
			g = math.gcd(z, N)
			if g != 1 and g != N:
				return g
	return False
#


def elliptic_factor(N):
	if helpers.probably_prime(N):
		print(N)
		return
	if N < 1000000:
		helpers.trial_factor(N)
		return
	d_1 = elliptic_find(N, 2000, 100000)
	if not d_1:
		print("FAIL: %d" % N)
		return
	d_2 = N // d_1
	elliptic_factor(d_1)
	elliptic_factor(d_2)
#


#N = 8767367846378687364783967843645675822
#N = 340282366920938463463374607431768211457
#N = 1633235598613468161901778096143
#########75903475845789407890748357485708947384705870489570489750384078340758304859
def main():
	while True:
		N = int(input())
		start = time.time()
		elliptic_factor(N)
		print("Time: %s" % (time.time() - start))
#

if __name__ == "__main__":
	main()
#
