from HashTable import *

import random

class HashTableAnalysis(object):
    """docstring for HashTableAnalysis"""
    def __init__(self, table, runs=10):
        self.table = table
        self.test_runs = runs
        self.record_count = list(range(1,101))
        self.totals = [{'collisions':0.0, 'found':0.0, 'notfound': 0.0}] * 100
        self.do_runs()
        
    def do_runs(self):
        for i in range(self.test_runs):
            print('-----> Test Run #{}'.format(i + 1))
            print()
            print('#RECORDS\tCOLLISIONS\tFOUND PROBES\tNOT-FOUND PROBES')
            self.run_test()
            self.table.reset()
            print()
        print('-----> Overall Average')

    def run_test(self):
        records = Utility.create_random_records_list(100) # Random records for population
        found_records = Utility.create_found_records_list(self.table)
        not_found_records = []
        for i,r in enumerate(records):
            if self.table.saturation >= 100.0:
                break
            found_records = Utility.create_found_records_list(self.table)
            if i <= 5:
                print(found_records)
            data = Utility.make_data_dictionary(id=r)
            self.table.insert_value(data)
        # print(self.table.collisions)


def main():
    l = LinearHashTable(to_print=False)
    c = CustomHashTable(to_print=False)

    print('*' * 50)
    print('Algorithm 1 - Linear Hashing')
    print('*' * 50)
    print()
    HashTableAnalysis(l)

    # print('*' * 50)
    # print('Jump - K Analysis')
    # print('*' * 50)
    # HashTableAnalysis(c)

    

if __name__ == '__main__':
    print('Ty Enders')
    print('Assignment 7 - Hashing Analysis')
    print()
    main()