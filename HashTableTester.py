from HashTable import *

import argparse


def make_data(**kwargs):
	return Utility.make_data_dictionary(id=kwargs['id'], name=kwargs['name'])


def main(arguments):
	l = LinearHashTable()

	# string = '31415'
	# l.insert_value(make_data(id=string, name='Jimbo'))
	#
	# l.insert_value(make_data(id='76666', name='Danni'))
	# l.insert_value(make_data(id=10015, name='Sally'))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tester for Assignment #6')
	args = parser.parse_args()
	main(args)