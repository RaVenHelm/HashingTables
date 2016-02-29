def max_index(array):
	return len(array) - 1


class Utility:
	@staticmethod
	def print_type_val(variable):
		print(type(variable), variable)

	@staticmethod
	def all_elements_empty(table):
		return all(i is None for i in table.values)

	@staticmethod
	def make_data_dictionary(**kwargs):
		return {'ID':kwargs['id'], 'NAME':kwargs['name']}

	@staticmethod
	def print_table_values(values):
		print('   INDEX    NAME    ID')
		for index in range(len(values)):
			if values[index] is not None:
				print('    {}        {}      {}'.format(index, values[index]['NAME'], values[index]['ID']))

	@staticmethod
	def print_current_table(table):
		print('Current Table:')
		if Utility.all_elements_empty(table):
			fmt_string = '<no records>'
			print(fmt_string.rjust(len(fmt_string) + 4))
			print()
		else:
			Utility.print_table_values(table.values)

	@staticmethod
	def get_user_input(table):
		print('Enter Record {}:'.format(table.records + 1))
		print('    Name:    ', end='')
		input_name = input()
		print('    ID:      ', end='')
		input_id = input()
		data = Utility.make_data_dictionary(id=input_id, name=input_name)
		table.insert_value(data)

	@staticmethod
	def get_user_search_input(table):
		table.searches += 1
		print('Search #{}:'.format(table.searches))
		print('    Enter ID:    ', end='')
		input_id = input()
		table.search_by_id(input_id)

	@staticmethod
	def print_table_complete(table):
		fmt_string = 'Table complete. {} records in {} spaces, with {} collisions'\
			.format(table.records, table.size, table.collisions)
		print(fmt_string)

	@staticmethod
	def print_search_summary(table):
		fmt_string = 'Summary: Performed {} searches, requiring {} probes, for an average of {} probes per search.'\
			.format(table.searches, table.probes, table.probes/table.searches)
		print(fmt_string)

	@staticmethod
	def value_to_string(value):
		return '{},{}'.format(value['NAME'], value['ID'])


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
		print('#' * 20, ' ', '-->', ' ', 'Building the Table', ' ', '<--', ' ', '#' * 20)
		self.print_table()
		while self.saturation < 3.0:
			self.get_input()
			self.saturation = 100 * (self.records/self.size)
		Utility.print_table_complete(self)
		print('#' * 20, ' ', '-->', ' ', 'Searching the Table', ' ', '<--', ' ', '#' * 20)
		self.get_search_input()

	def insert_value(self, value):
		for i in range(len(self.values)):
			e = self.values[i]
			if e is None:
				self.values[i] = value
				return

	# Linear Hashing will be the default hash table algorithm
	# Override for custom
	def hash(self, index):
		if index >= max_index(self.values):
			return 0
		else:
			return index + 1

	def search_by_id(self, id):
		self.calculate_index(id)

	def get_input(self):
		Utility.get_user_input(self)

	def get_search_input(self):
		Utility.get_user_search_input(self)

	def print_table(self):
		Utility.print_current_table(self)

	def end(self):
		Utility.print_search_summary(self)

	# Linear Searching will be the default hash table algorithm
	# Override for custom
	def get_hash_index(self, value):
		# Utility.print_type_val(value)
		data_id = value['ID']
		string = str(data_id)

		hash_index = int(string[len(string)-2:len(string)])
		orig_hash_index = hash_index

		# print('Value at index: {}'.format(self.values[hash_index]))
		while self.values[hash_index] is not None:
			fmt_string = 'Calculating hashing index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			self.collisions += 1
			fmt_is_not_empty = '(Collision #{} - {})'
			fmt_is_not_empty = fmt_is_not_empty.format(self.collisions, Utility.value_to_string(self.values[hash_index]))
			print(fmt_is_not_empty.rjust(len(fmt_is_not_empty) + 2))
			hash_index = self.hash(hash_index)
		else:
			fmt_string = 'Calculating hashing index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			fmt_is_empty = '(empty)'
			print(fmt_is_empty.rjust(len(fmt_is_empty) + 2))
			return hash_index, orig_hash_index

	def calculate_index(self, value):
		string = str(value)
		hash_index = int(string[len(string)-2:len(string)])
		orig_hash_index = hash_index
		while self.values[hash_index] is not None:
			fmt_string = 'Calculated index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			self.probes += 1

			if self.values[hash_index]['ID'] != value:
				fmt_is_not_empty = '({}, {})'
				fmt_is_not_empty = fmt_is_not_empty.format(self.collisions, self.values[hash_index].name)
				print(fmt_is_not_empty.rjust(len(fmt_is_not_empty) + 2))
				hash_index = self.hash(hash_index)
			else:
				# fmt_string = 'Calculated index:'
				# print(fmt_string.rjust(len(fmt_string) + 4), end='')
				# print('{}'.format(hash_index).rjust(4), end='')
				# print('Found at index {}.'.format(hash_index))
				break
		else:
			fmt_string = 'Calculated index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			self.probes += 1
			fmt_is_empty = '(empty)'
			print(fmt_is_empty.rjust(len(fmt_is_empty) + 2))
			print('Not in table')
			print('Required {} probes.'.format(self.probes))
			return hash_index, orig_hash_index
		print('Required {} probes.'.format(self.probes))
		return hash_index, orig_hash_index

	def insert_value(self, value):
		# Utility.print_type_val(value)
		hash_index = self.get_hash_index(value)[0]
		fmt_string = 'Storing in location {}'
		self.values[hash_index] = value
		self.records += 1
		print(fmt_string.format(hash_index).rjust(len(fmt_string) + 4))
		print()
		self.print_table()
		print()


class LinearHashTable(HashTable):
	def __init__(self, to_print=True):
		if to_print:
			print('#' * 32)
			print('Hash Algoirthm #1 - Linear')
			print('#' * 32)
		HashTable.__init__(self, to_print)
		self.end()


class CustomHashTable(HashTable):

	def __init__(self, to_print=True):
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
