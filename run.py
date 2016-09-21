#! /usr/bin/env python

import sys
import md5
import time
import stage_ii_0
import stage_ii_1
import stage_ii_2

import stage_iii_0
import stage_iii_1
import stage_iii_2

if __name__ == '__main__':

	HASH_FILENAME = "eHarmony.txt"
	CHARACTERS_FILENAME = "characters.txt"
	OUTPUT_FILENAME = "out.txt"
	STAGE_NO = 1
	
	results = {}

	if len(sys.argv) <= 2 :
		print "No arguments provided. Using default values"
	else:
		HASH_FILENAME = sys.argv[1]
		STAGE_NO = int(sys.argv[2])
		OUTPUT_FILENAME = sys.argv[3]
		CHARACTERS_FILENAME = sys.argv[4]

############################################################################
#	EHARMONY.TXT
############################################################################

############################################################################
#	To check a password file
############################################################################
	if(STAGE_NO == 10):
		PASSWORD_FILE = sys.argv[5]
		results = stage_ii_0.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

############################################################################
#	Brute force strings of length 1-5
############################################################################
	if(STAGE_NO == 11):
		results = stage_ii_1.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

############################################################################
#	Brute force strings of length 6-8
############################################################################
	if(STAGE_NO == 12):
		results = stage_ii_1.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

############################################################################
#	Brute force strings of length 8-12
############################################################################
	if(STAGE_NO == 13):
		results = stage_ii_1.make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

############################################################################
#	Hybrid Attack [Password File + Strings of length 1-3]
############################################################################
	if(STAGE_NO == 14):
		PASSWORD_FILE = sys.argv[5]
		results = stage_ii_2.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

############################################################################
#	Hybrid Attack [Strings of length 1-3 + Password File]
############################################################################
	if(STAGE_NO == 15):
		PASSWORD_FILE = sys.argv[5]
		results = stage_ii_2.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

############################################################################
#	Hybrid Attack [Password File + Strings of length 1-4]
############################################################################
	if(STAGE_NO == 16):
		PASSWORD_FILE = sys.argv[5]
		results = stage_ii_2.make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

############################################################################
#	Hybrid Attack [Strings of length 1-4 + Password File]
############################################################################
	if(STAGE_NO == 17):
		PASSWORD_FILE = sys.argv[5]
		results = stage_ii_2.make_keywords_4(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)



############################################################################
#	FORMSPRING.TXT
############################################################################

	if(STAGE_NO == 20):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage_iii_0.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force strings of length 1-4
	if(STAGE_NO == 21):
		start = time.time()

		results = stage_iii_1.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	if(STAGE_NO == 22):
		start = time.time()

		results = stage_iii_1.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	if(STAGE_NO == 23):
		start = time.time()

		results = stage_iii_1.make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force PASSWORD + strings of length 1-3 + SALT
	if(STAGE_NO == 25):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage_iii_2.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force PASSWORD + strings of length 1-3 + SALT
	if(STAGE_NO == 26):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage_iii_2.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)


	print "Results:"
	for key, value in results.iteritems():
		print key, value

	#for keyword in keywords:

