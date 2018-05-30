#!/usr/bin/python

"""
Mimik is a tool for generating valid RSA ID numbers, and credit card numbers for Mastercard SA and FNB Visa
Version: 1.0 (01-03-2014)

[-] RSA ID FORMAT: [DOB - 6 bits][GENDER - 4 bits][0][RANDOM - 1 bit][PARITY - 1 bit]
[-] CREDIT CARD FORMAT: [IIN][ACCOUNT NUMBER][PARITY]
[-] VISA FNB IIN: 490115
[-] MASTERCARD IIN: 5221** 
"""

import argparse
import random

def luhn_checksum(idnum):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(idnum)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def calculate_luhn(partial_id):
    check_digit = luhn_checksum(int(partial_id) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit

if __name__ == "__main__":	

	parser = argparse.ArgumentParser(prog='mimik')
	parser.add_argument('-i', dest='dob', action='store', nargs=3, metavar=('YY', 'MM', 'DD'), help="generate RSA ID number") 
	parser.add_argument('-c', dest='creditcard', action='store', choices=['visa','mastercard'], help="generate credit card number")
	args = parser.parse_args()	

	try:
		if args.dob and len(args.dob) == 3 and len(args.dob[0]) == 2 and len(args.dob[1]) == 2 and len(args.dob[2]) == 2:
			number = str(args.dob[0]) + str(args.dob[1]) + str(args.dob[2]) + str(random.randint(0000, 9999)) + '0' + str(random.randint(0, 9))
			parity = calculate_luhn(number)
			print "[+] ID No: " + number + str(parity)
		else:
			raise e	
		if args.creditcard:
			if args.creditcard == 'visa':
				number = str(490115) + str(random.randint(000000000, 999999999))
			else:
				number = str(522100) + str(random.randint(000000000, 999999999))
			parity = calculate_luhn(number)
			print "[+] CC No: " + number + str(parity)	
	except Exception, e:
		print "[-] Your feet are bigger than your flip flops..."
