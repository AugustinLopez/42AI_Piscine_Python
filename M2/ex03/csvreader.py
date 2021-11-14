#!/usr/bin/env python

import csv
from io import TextIOWrapper


class CsvReader():
	def __init__(self, filename = None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.file: TextIOWrapper = None
		self.line = 0
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		try:
			self.file = open(self.filename, 'r')
			csv_reader = csv.reader(self.file, delimiter = self.sep)
			header = next(csv_reader)
			column = len(header)
			for i, row in enumerate(csv_reader):
				if (column != len(row)):
					raise IndexError("Row of length {} VS Header of length {}"
						.format(len(row), column))
				for val in row:
					if val is "" or val is None:
						raise IndexError("Empty values are illegal")
			self.line = i + 1 - (self.header == True)
			self.file.seek(0)
		except (OSError, IndexError) as e:
			print("Error: {}. Interruption.".format(e))
			self = None
		return self

    # __exit__ must have those 4 arguments in its signature even if unused
	def __exit__(self, type, value, traceback):
		if self.file:
			if not self.file.closed:
				self.file.close()

	def getdata(self):
		data = []
		try:
			csv_reader = csv.reader(self.file, delimiter = self.sep)
			if (self.header == True):
				row = next(csv_reader)
			for i, row in enumerate(csv_reader):
				if (i < self.skip_top):
					pass
				elif (i > self.line - self.skip_bottom):
					break
				else:
					data.append(row)
		except OSError as e:
			print("Error: {}. Interruption.".format(e))
			data = None
		self.file.seek(0)
		return data

	def getheader(self):
		try:
			if (self.header == False):
				return None
			csv_reader = csv.reader(self.file, delimiter = self.sep)
			return(next(csv_reader))
		except OSError as e:
			print("Error: {}. Interruption.".format(e))
			return None

if __name__ == "__main__":
	with CsvReader('good.csv', header=True, skip_top=1, skip_bottom=1) as file:
		data = file.getdata()
		header = file.getheader()
		print(header)
		for elem in data:
			print(elem)
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")
		else:
			print(file)