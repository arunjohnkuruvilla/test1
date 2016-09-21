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
		chars.append(line[:-1])
	return chars

def common_passwords(PASSWORD_FILE):
	password_file = open(PASSWORD_FILE, 'r')
	passwords = []
	for line in password_file:
		line = line[:-1]
		#passwords.append(line)
		passwords.append(line.upper())
	return passwords

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
	out_file.write("%s : %s\n" % (PASSWORD, HASH))
	out_file.close()

def make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	passwords = common_passwords(PASSWORD_FILE)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0


	for password in passwords:
		string = password
		check_result = check(string, data)
		if(check_result[0]):
			print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
			results[check_result[1]] = check_result[2]
		
	return results

