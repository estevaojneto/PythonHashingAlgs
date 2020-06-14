import math;

def md5hash(msg):
	r = [7,12,17,22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
	max32bit = pow(2, 32);
	for i in range(0, 64):
	    k[i] = math.floor(max32bit * abs(sin(i+1)))
	h0 = 0x67452301
	h1 = 0xEFCDAB89
	h2 = 0x98BADCFE
	h3 = 0x10325476
	