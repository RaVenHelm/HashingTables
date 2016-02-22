
class Utility:
	@staticmethod
	def print_type_val(variable):
		print(type(variable), variable)

	@staticmethod
	def all_elements_empty(table):
		return all(i is None for i in table.values)

	@staticmethod
	def print_table_values(values):
		print('   INDEX    VALUE')
		for index in range(len(values)):
			if values[index] is not None:
				print('    {}        {}'.format(index, values[index]))

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
		print('Enter Record:')
		print('    Name:    ', end='')
		input_name = input()
		print('    ID:      ', end='')
		input_id = input()
		table.insert_value(input_id)



class HashTable:

	def __init__(self, to_print=True):
		self.size = 100
		self.values = [None] * self.size
		self.collisions = 0
		self.print = to_print
		self.print_table()
		self.get_input()

	def insert_value(self, value):
		for i in range(len(self.values)):
			e = self.values[i]
			if e is None:
				self.values[i] = value
				return

	def hash(self, index):
		return index + 1

	def get_input(self):
		Utility.get_user_input(self)

	def print_table(self):
		Utility.print_current_table(self)

	# Linear Searching will be the default hash table algorithm
	# Override for custom
	def get_hash_index(self, string):
		string = str(string)

		hash_index = int(string[len(string)-2:len(string)])
		orig_hash_index = hash_index

		# print('Value at index: {}'.format(self.values[hash_index]))
		while self.values[hash_index] is not None:
			fmt_string = 'Calculating hashing index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			self.collisions += 1
			fmt_is_not_empty = '(Collision #{} - {})'
			fmt_is_not_empty = fmt_is_not_empty.format(self.collisions, self.values[hash_index])
			print(fmt_is_not_empty.rjust(len(fmt_is_not_empty) + 2))
			hash_index = self.hash(hash_index)
		else:
			fmt_string = 'Calculating hashing index:'
			print(fmt_string.rjust(len(fmt_string) + 4), end='')
			print('{}'.format(hash_index).rjust(4), end='')
			fmt_is_empty = '(empty)'
			print(fmt_is_empty.rjust(len(fmt_is_empty) + 2))
			return hash_index, orig_hash_index


class LinearHashTable(HashTable):

	def __init__(self, to_print=True):
		HashTable.__init__(self, to_print)

	def insert_value(self, value):
		# Utility.print_type_val(value)
		hash_index = self.get_hash_index(value)[0]
		fmt_string = 'Storing in location {}'
		self.values[hash_index] = value
		print(fmt_string.format(hash_index).rjust(len(fmt_string) + 4))
		print()
		self.print_table()
		print()
