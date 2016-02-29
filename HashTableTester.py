from HashTable import *

import argparse


def make_data(**kwargs):
    return Utility.make_data_dictionary(id=kwargs['id'], name=kwargs['name'])


def main(arguments):
    l = LinearHashTable()
    c = CustomHashTable()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tester for Assignment #6')
    args = parser.parse_args()
    main(args)
