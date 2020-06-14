# MD5 sample hashing function by Estevão Neto
# NEVER USE THIS IN PRODUCTION! Always use whatever hashing functions 
# your language or framework natively offers, don't reinvent the wheel.

# MD5 in special is something you should never use if you want to achieve
# security. It has been broken since the late 90s/2000s and its usage
# today is mostly hash verification (e.g finding out if two files are identical)

import math;
import sys;

# Actual hashing function
def hash_md5(msg):
    msg_bin = str_to_bin(msg)
    msg_len64 = len_64(len(msg_bin));
    k = [0] * 64
    # declares shifts
    r = [7, 12, 17, 22] * 4
    r += [5, 9, 14, 20] * 4
    r += [4, 11, 16, 23] * 4
    r += [6, 10, 15, 21] * 4
    max_32 = pow(2, 32)
    
    # we'll use the sin function
    # K is normally a constant
    for i in range(0, 64):
        k[i] = hex(math.floor(max_32 * abs(math.sin(i+1))))
    
    # declares variables, as per MD5 definition
    # reminds me of the registers on the ol' 68000... Good old times
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476
    
    # nicely pads our message
    msg_bin += "1"
    while(len(msg_bin) != 448):
        msg_bin += "0"
    msg_bin += msg_len64
    print(len(msg_bin))
    
# HELPER FUNCTIONS

# Converts a string of characters to a string of characters in binary.
# Each letter is 8 bits (1 byte) long. See bytarray documentation for more
def str_to_bin(msg):
    return ''.join([bin(msg_char) for msg_char in bytearray(msg, 'utf-8')]).replace('0b','0')
    
# Converts a number (message length) to a 64bit binary format, to be appended
# when we're treating the message in hash_md5
def len_64(len_msg):
    bin_len = str(bin(len_msg)).replace('0b', '0')
    bin_len_str = ['0'] * (64-len(bin_len))
    bin_len_str = ''.join(bin_len_str)
    bin_len_str += bin_len;
    return bin_len_str

# CALL TO hash_md5
# Now actually call our function and we'll see what happens!
hash_md5('stu');