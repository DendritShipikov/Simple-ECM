import math


def is_strong_pseudoprime(n, a):
	if n < 2:
		return False
	d = n - 1
	s = 0
	while d & 1 == 0:
		d //= 2
		s += 1
	d = pow(a, d, n)
	if d == n - 1 or d == 1:
		return True
	for r in range(1, s):
		d = pow(d, 2, n)
		if d == n - 1:
			return True
	return False
#


def probably_prime(n):
	if n == 2:
		return True
	if not is_strong_pseudoprime(n, 2):
		return False
	if n < 2047:
		return True
	if not is_strong_pseudoprime(n, 3):
		return False
	if n < 1373653:
		return True
	if not is_strong_pseudoprime(n, 5):
		return False
	if n < 25326001:
		return True
	if not is_strong_pseudoprime(n, 7):
		return False
	if n < 3215031751:
		return True
	if not is_strong_pseudoprime(n, 11):
		return False
	if n < 2152302898747:
		return True
	if not is_strong_pseudoprime(n, 13):
		return False
	if n < 3474749660383:
		return True
	if not is_strong_pseudoprime(n, 17):
		return False
	if n < 341550071728321:
		return True
	if not is_strong_pseudoprime(n, 19):
		return False
	if not is_strong_pseudoprime(n, 23):
		return False
	if n < 3825123056546413051:
		return True
	if not is_strong_pseudoprime(n, 29):
		return False
	if not is_strong_pseudoprime(n, 31):
		return False
	if not is_strong_pseudoprime(n, 37):
		return False
	if n < 318665857834031151167461:
		return True
	if not is_strong_pseudoprime(n, 41):
		return False
	if n < 3317044064679887385961981:
		return True
	if not is_strong_pseudoprime(n, 43): #14th prime
		return False
	if n < 6003094289670105800312596501:
		return True
	if not is_strong_pseudoprime(n, 47):
		return False
	if n < 59276361075595573263446330101:
		return True
	if not is_strong_pseudoprime(n, 53):  #16th prime
		return False
	if n < 564132928021909221014087501701:
		return True
	if not is_strong_pseudoprime(n, 59):
		return False
	if not is_strong_pseudoprime(n, 61):
		return False
	if n < 1543267864443420616877677640751301:
		return True
	if not is_strong_pseudoprime(n, 67):
		return False
	if not is_strong_pseudoprime(n, 71):
		return False
	if n < 1000000000000000000000000000000000000: #10**36
		return True
	
	other_primes = [73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
	for p in other_primes:
		if not is_strong_pseudoprime(n, p):
			return False
	return True
#


def prime_sieve(B):
	s = [True] * (B + 1)
	E = math.isqrt(B)
	for i in range(2, E + 1):
		if s[i]:
			for j in range(i * i, B + 1, i):
				s[j] = False
	res = []
	for p in range(2, B + 1):
		if s[p]:
			res.append(p)
	return res
#


def trial_factor(N):
	if probably_prime(N):
		print(N)
		return
	P = N
	d = 2
	while P != 1:
		if P % d == 0:
			P //= d
			print(d)
			if probably_prime(P):
				print(P)
				return
		else:
			d += 1
			if d * d > P:
				print(P)
				return
#
