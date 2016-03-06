from random import randrange, sample

import sys

def max_index(array):
    return len(array) - 1

def last(array):
    return array[len(array) - 1]


class Utility:

    @staticmethod
    def print_type_val(variable):
        print(type(variable), variable)

    @staticmethod
    def all_elements_empty(table):
        return all(i is None for i in table.values)

    @staticmethod
    def make_data_dictionary(**kwargs):
        if 'id' not in kwargs:
            raise Exception('Need id to create data dictionary')

        if 'name' in kwargs:
            return {'ID': kwargs['id'], 'NAME': kwargs['name']}
        else:
            return {'ID': kwargs['id']}

    @staticmethod
    def create_random_records_list(count):
        records = []
        while len(records) < 100:
            r = randrange(100000, 1000000)
            if r in records:
                continue
            else:
                records.append(r)
        return records

    @staticmethod
    def create_found_records_list(table):
        values = [x for x in table.values if x is not None]
        records = [v['ID'] for v in values]
        if len(records) <= 10:
            _last = last(records)
            remaining = 10 - len(records)
            # replicate last record until list is filled
            [records.append(_last) for i in range(remaining)]
            return records
        else:
            return sample(records, 10)

    @staticmethod
    def create_not_found_records_list(table):
        values = [x for x in table.values if x is not None]
        ids = [v['ID'] for v in values]
        records = []
        while len(records) < 10:
            r = randrange(100000, 1000000)
            if r in ids:
                continue
            else:
                records.append(r)
        return records

    @staticmethod
    def print_table_values(values):
        if table.to_print:
            print('   INDEX    NAME    ID')
            for index in range(len(values)):
                if values[index] is not None:
                    print('    {}        {}      {}'.format(
                        index, values[index]['NAME'], values[index]['ID']))

    @staticmethod
    def print_current_table(table):
        if table.to_print:
            print('Current Table:')
            if Utility.all_elements_empty(table):
                fmt_string = '<no records>'
                print(fmt_string.rjust(len(fmt_string) + 4))
                print()
            else:
                Utility.print_table_values(table.values)

    @staticmethod
    def get_user_input(table):
        if table.to_print:
            print('Enter Record {}:'.format(table.records + 1))
            print('    Name:    ', end='')
            input_name = input()
            print('    ID:      ', end='')
            input_id = input()
            data = Utility.make_data_dictionary(id=input_id, name=input_name)
            table.insert_value(data)

    @staticmethod
    def get_user_search_input(table):
        if table.to_print:
            table.searches += 1
            print('Search #{}:'.format(table.searches))
            print('    Enter ID:    ', end='')
            input_id = input()
            table.search_by_id(input_id)

    @staticmethod
    def print_table_complete(table):
        if table.to_print:
            fmt_string = 'Table complete. {} records in {} spaces, with {} collisions'\
                .format(table.records, table.size, table.collisions)
            print(fmt_string)

    @staticmethod
    def print_search_summary(table):
        if table.to_print:
            fmt_string = 'Summary: Performed {} searches, requiring {} probes, for an average of {} probes per search.'\
                .format(table.searches, table.probes, table.probes / table.searches)
            print(fmt_string)

    @staticmethod
    def value_to_string(value):
        try:
            return '{},{}'.format(value['NAME'], value['ID'])
        except Exception as e:
            return '{},{}'.format(value['ID'])
        



class HashTable:

    def __init__(self, to_print=True):
        self.size = 100
        self.values = [None] * self.size
        self.records = 0
        self.collisions = 0
        self.probes = 0
        self.searches = 0
        # Filled entries/Size
        self.saturation = 0.0
        self.print = to_print

        if self.to_print:
            print('#' * 20, ' ', '-->', ' ',
                  'Building the Table', ' ', '<--', ' ', '#' * 20)
            self.print_table()

            # If getting user input, automatically add record
            while self.saturation < 12.0:
                self.get_input()
                # self.saturation = 100 * (self.records / self.size)

            # If getting user input, automatically search after population
            # TODO: add loop for multiple searches
            Utility.print_table_complete(self)
            print('#' * 20, ' ', '-->', ' ',
                  'Searching the Table', ' ', '<--', ' ', '#' * 20)
            self.get_search_input()

    # Linear Hashing will be the default hash table algorithm
    # Override for custom
    def hash(self, index):
        if index >= max_index(self.values):
            return 0
        else:
            return index + 1

    def search_by_id(self, id):
        return self.calculate_index(id)[2]

    def get_input(self):
        if self.to_print:
            Utility.get_user_input(self)

    def get_search_input(self):
        if self.to_print:
            Utility.get_user_search_input(self)

    def print_table(self):
        if self.to_print:
            Utility.print_current_table(self)

    def reset(self):
        self.size = 100
        self.values = [None] * self.size
        self.records = 0
        self.collisions = 0
        self.probes = 0
        self.searches = 0
        # Filled entries/Size
        self.saturation = 0.0

    def end(self):
        if self.to_print:
            Utility.print_search_summary(self)

    # Linear Searching will be the default hash table algorithm
    # Override for custom
    def get_hash_index(self, value):
        data_id = value['ID']
        string = str(data_id)

        hash_index = int(string[len(string) - 2:len(string)])
        orig_hash_index = hash_index

        while self.values[hash_index] is not None:
            if self.to_print:
                fmt_string = 'Calculating hashing index:'
                print(fmt_string.rjust(len(fmt_string) + 4), end='')
                print('{}'.format(hash_index).rjust(4), end='')
            self.collisions += 1
            if self.to_print:
                fmt_is_not_empty = '(Collision #{} - {})'
                fmt_is_not_empty = fmt_is_not_empty.format(self.collisions, Utility.value_to_string(self.values[hash_index]))
                print(fmt_is_not_empty.rjust(len(fmt_is_not_empty) + 2))
            hash_index = self.hash(hash_index)
        else:
            if self.to_print:
                fmt_string = 'Calculating hashing index:'
                print(fmt_string.rjust(len(fmt_string) + 4), end='')
                print('{}'.format(hash_index).rjust(4), end='')
                fmt_is_empty = '(empty)'
                print(fmt_is_empty.rjust(len(fmt_is_empty) + 2))
            return hash_index, orig_hash_index

    # This is for searching
    def calculate_index(self, value):
        string = str(value)
        hash_index = int(string[len(string) - 2:len(string)])
        orig_hash_index = hash_index
        required_probes = 1
        i = 0
        while self.values[hash_index] is not None and required_probes < self.size:
            if self.to_print:
                fmt_string = 'Calculated index:'
                print(fmt_string.rjust(len(fmt_string) + 4), end='')
                print('{}'.format(hash_index).rjust(4), end='')

            self.probes += 1
            required_probes += 1

            if self.values[hash_index]['ID'] != value:
                if self.to_print:
                    fmt_is_not_empty = '({}, {})'
                    fmt_is_not_empty = fmt_is_not_empty.format(self.collisions, self.values[hash_index].name)
                    print(fmt_is_not_empty.rjust(len(fmt_is_not_empty) + 2))

                hash_index = self.hash(hash_index)
                
                
            else:
                return hash_index, orig_hash_index, required_probes
        else:
            if self.to_print:
                fmt_string = 'Calculated index:'
                print(fmt_string.rjust(len(fmt_string) + 4), end='')
                print('{}'.format(hash_index).rjust(4), end='')

            if self.to_print:
                fmt_is_empty = '(empty)'
                print(fmt_is_empty.rjust(len(fmt_is_empty) + 2))
                print('Not in table')
                print('Required {} probes.'.format(self.probes))
            return hash_index, orig_hash_index, required_probes

        if self.to_print:
            print('Required {} probes.'.format(self.probes))

        return hash_index, orig_hash_index, required_probes

    def insert_value(self, value):
        hash_index, orig = self.get_hash_index(value)
        self.values[hash_index] = value
        self.records += 1
        self.saturation = 100 * (self.records / self.size)
        if self.to_print:
            fmt_string = 'Storing in location {}'
            print(fmt_string.format(hash_index).rjust(len(fmt_string) + 4))
            print()
            self.print_table()
            print()


class LinearHashTable(HashTable):

    def __init__(self, to_print=True):
        self.to_print = to_print
        if to_print:
            print('#' * 32)
            print('Hash Algoirthm #1 - Linear')
            print('#' * 32)
        HashTable.__init__(self, to_print)
        self.end()


class CustomHashTable(HashTable):

    def __init__(self, to_print=True):
        self.to_print = to_print
        if to_print:
            print('#' * 32)
            print('Hash Algoirthm #2 - Jump-K')
            print('#' * 32)
        HashTable.__init__(self, to_print)
        self.end()

    # Jump K Method, just cause it's easier
    def hash(self, index):
        if index >= max_index(self.values):
            return 0
        else:
            return index + 5
