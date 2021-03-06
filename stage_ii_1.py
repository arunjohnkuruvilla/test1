#! /usr/bin/env python

import sys
import md5
import time

def build_data(filename):
	dump_file = open(filename, "r")
	data = {}
	for line in dump_file:
		data[line[:-1]] = ""
	return data

def characters(CHARACTERS_FILENAME):
	char_file = open(CHARACTERS_FILENAME, 'r')
	chars = []
	for line in char_file:
		if(line[-1] != ''):
			chars.append(line[:-1])
	return chars

def check(keyword, check_list):
	m = md5.new()
	m.update(keyword)
	test_hash = m.hexdigest()
	result = []
	print keyword
	if test_hash in check_list:
		result.append(1)
		result.append(keyword)
		result.append(test_hash)
	else:
		result.append(0)
	return result

def print_out(OUTPUT_FILENAME, PASSWORD, HASH):
	out_file = open(OUTPUT_FILENAME, "a")
	out_file.write("%s : %s" % (PASSWORD, HASH))
	out_file.close()

############################################################################
#	Brute force strings of length 1-6
############################################################################
def make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			if size_one == 0:
				size_one = 1
				print "Trying strings of length 1..."
			for char1 in chars:
				string = char1
				check_result = check(string, data)
				if(check_result[0]):
					print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
					results[check_result[1]] = check_result[2]
				#keywords.append(string)
		if x == 2:																# Strings of length 2
			if size_two == 0:
				size_two = 1
				print "Completed strings of length 1."
				print "Trying strings of length 2..."
			for char1 in chars:
				for char2 in chars:
					string = char1 + char2
					check_result = check(string, data)
					if(check_result[0]):
						print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
						results[check_result[1]] = check_result[2]
					#keywords.append(string)
		if x == 3:																# Strings of length 3
			if size_three == 0:
				size_three = 1
				print "Completed strings of length 2."
				print "Trying strings of length 3..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						string = char1 + char2 + char3
						check_result = check(string, data)
						if(check_result[0]):
							print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
							results[check_result[1]] = check_result[2]
						#keywords.append(string)
		if x == 4:																# Strings of length 4
			if size_four == 0:
				size_four = 1
				print "Completed strings of length 3."
				print "Trying strings of length 4..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							string = char1 + char2 + char3 + char4
							check_result = check(string, data)
							if(check_result[0]):
								print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
								results[check_result[1]] = check_result[2]
							#keywords.append(string)'''		
		if x == 5:																# Strings of length 5	
			if size_five == 0:
				size_five = 1
				print "Completed strings of length 4."
				print "Loading strings of length 5..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								string = char1 + char2 + char3 + char4 + char5
								check_result = check(string, data)
								if(check_result[0]):
									print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
									results[check_result[1]] = check_result[2]
								#keywords.append(string)
		if x == 6:																# Strings of length 6
			if size_six == 0:
				size_six = 1
				print "Completed strings of length 5."
				print "Loading strings of length 6..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									string = char1 + char2 + char3 + char4 + char5 + char6
									check_result = check(string, data)
									if(check_result[0]):
										print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
										results[check_result[1]] = check_result[2]
									#keywords.append(string)
	print "Completed strings of length 6."
	return results

############################################################################
#	To check a password file
############################################################################
def make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	size_six = 0
	size_seven = 0
	size_eight = 0

	for x in xrange(6,9):
		if x == 6:																# Strings of length 6
			if size_six == 0:
				size_six = 1
				print "Loading strings of length 6..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									string = char1 + char2 + char3 + char4 + char5 + char6
									check_result = check(string, data)
									if(check_result[0]):
										print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
										results[check_result[1]] = check_result[2]
									#keywords.append(string)'''
		if x == 7:																# Strings of length 6
			if size_seven == 0:
				size_seven = 1
				print "Completed strings of length 6."
				print "Loading strings of length 7..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										string = char1 + char2 + char3 + char4 + char5 + char6 + char7
										check_result = check(string, data)
										if(check_result[0]):
											print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
											results[check_result[1]] = check_result[2]
		if x == 8:																# Strings of length 6
			if size_eight == 0:
				size_eight = 1
				print "Completed strings of length 7."
				print "Loading strings of length 8..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
											check_result = check(string, data)
											if(check_result[0]):
												print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
												results[check_result[1]] = check_result[2]
	print "Completed strings of length 8."
	return results

def make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	for x in xrange(8,13):
		if x == 8:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
											check_result = check(string, data)
											if(check_result[0]):
												print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
												results[check_result[1]] = check_result[2]

		if x == 9:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9
												check_result = check(string, data)
												if(check_result[0]):
													print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
													results[check_result[1]] = check_result[2]

		if x == 10:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10
													check_result = check(string, data)
													if(check_result[0]):
														print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
														results[check_result[1]] = check_result[2]

		if x == 11:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													for char11 in chars:
														string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11
														check_result = check(string, data)
														if(check_result[0]):
															print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
															results[check_result[1]] = check_result[2]
		if x == 12:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													for char11 in chars:
														for char12 in chars:
															string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11 + char12
															check_result = check(string, data)
															if(check_result[0]):
																print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
																results[check_result[1]] = check_result[2]
	print "Completed strings of length 12."
	return results

