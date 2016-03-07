from HashTable import *

import random

class HashTableAnalysis(object):
    """docstring for HashTableAnalysis"""
    def __init__(self, table, runs=10):
        self.table = table
        self.test_runs = runs
        self.record_count = list(range(1,self.table.size + 1))
        self.total_collisions = [0.0] * self.table.size
        self.total_found = [0.0] * self.table.size
        self.total_not_found = [0.0] * self.table.size
        self.average_collisions = [0.0] * self.table.size
        self.average_found = [0.0] * self.table.size
        self.average_not_found = [0.0] * self.table.size
        self.do_runs()
        
    def do_runs(self):
        for i in range(self.test_runs):
            print('-----> Test Run #{}'.format(i + 1))
            print()
            print('#RECORDS\tCOLLISIONS\tFOUND PROBES\tNOT-FOUND PROBES')
            self.run_test()
            self.table.reset()

            for i in range(self.table.size):
                self.average_collisions[i] += self.total_collisions[i] / (self.test_runs)
                self.average_found[i] += self.total_found[i] / (self.test_runs)
                self.average_not_found[i] += self.total_not_found[i] / (self.test_runs)

            self.reset()
            # print(self.average_collisions)
            print()
        print()
        self.print_averages()

    def reset(self):
        self.total_collisions = [0.0] * self.table.size
        self.total_found = [0.0] * self.table.size
        self.total_not_found = [0.0] * self.table.size

    def print_averages(self):
        print('-----> Overall Average')
        print()
        print('#RECORDS\tCOLLISIONS\tFOUND PROBES\tNOT-FOUND PROBES')
        for i in range(self.table.size):
            fmt_string = '{}\t{:1}\t{:2}\t{:2}'
            res = fmt_string.format(i + 1, self.average_collisions[i], self.average_found[i], self.average_not_found[i])
            print(res)
        print()

    def run_test(self):
        records = Utility.create_random_records_list(self.table.size) # Random records for population
        for i,r in enumerate(records):
            fmt_string = '{}\t{}\t{}\t{}'
            data = Utility.make_data_dictionary(id=r)
            collisions_required = self.table.insert_value(data)
            found_records = Utility.create_found_records_list(self.table)
            not_found_records = Utility.create_not_found_records_list(self.table)

            # search through found records
            found_probes = [self.table.search_by_id(id) for id in found_records]
            found_avg = sum(found_probes) / len(found_probes)

            # search through not found records
            not_found_probes = [self.table.search_by_id(id) for id in not_found_records]
            not_found_avg = sum(not_found_probes) / len(not_found_probes)

            
            # place results into running totals
            self.total_collisions[i] = collisions_required
            self.total_found[i] = found_avg
            self.total_not_found[i] = not_found_avg
            res = fmt_string.format(i + 1, collisions_required, found_avg, not_found_avg)
            print(res)
        

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