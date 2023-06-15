from hashlib import sha256 as sha
import string

def a(n):
	b = 0
	while n != 1:
		if n & 1:
			n *= 3
			n += 1
		else:
			n //= 2
		b += 1

	return b


def d(u, p):
	return (u << p % 5) - 158


def j(q, w):
	return ord(q) * 115 + ord(w) * 21


def t(x):
	#x = input()
	# len(x) == 15

	l = [-153, 462, 438, 1230, 1062, -24, -210, 54, 2694, 1254, 69, -162, 210,
	 150]
	m = 'b4f9d505'

	#if len(x) - 1 != len(l):
	#	return False
	#print(list(enumerate(zip(x, x[1:]))))
	for i, c in enumerate(zip(x, x[1:])):
		# print(f'i: {i}, c: {c}')
		#print(c)
		if d(a(j(*c) - 10), i) * 3 != l[i]:
			return False
		#print(c)
		#if sha(x.encode()).hexdigest()[:8] != m:
		#	return False
	return True



def solve(flag):
	for char_1 in string.printable:
		if char_1 == '~':
			break
		for char_2 in string.printable:
			if char_2 == '~':
				break
			test = flag + char_1 + char_2
			if len(test) == 15:
				if char_2 != '}':
					continue
				print(test)
			if t(test):
				if len(test) == 15:
					m = 'b4f9d505'
					if sha(test.encode()).hexdigest()[:8] == m:
						print(test)
						exit()
				else:
					solve(test)
	


flag = 'flag{'
solve(flag)

# flag{380822974}
