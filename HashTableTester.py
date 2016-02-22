from HashTable import *

import argparse


def main(arguments):
	l = LinearHashTable()
	# l.insert_value(1)
	# l.insert_value(2)
	# values = l.values[0:3]
	# print(values)

	string = '31415'
	l.insert_value(string)

	l.insert_value('22015')
	l.insert_value(10015)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tester for Assignment #6')
	args = parser.parse_args()
	main(args)