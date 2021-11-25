import csv


class CsvReader():
    def __init__(self, filename: str = None, sep: str = ',',
                 header: bool = False, skip_top: int = 0,
                 skip_bottom: int = 0):

        if not isinstance(filename, str) and filename is not None:
            raise TypeError("Expected str. Got " + str(type(filename)))
        if not isinstance(sep, str) and sep is not None:
            raise TypeError("Expected str. Got " + str(type(sep)))
        if not isinstance(skip_top, int):
            raise TypeError("Expected int. Got " + str(type(skip_top)))
        if not isinstance(skip_bottom, int):
            raise TypeError("Expected int. Got " + str(type(skip_bottom)))
        if skip_bottom < 0 or skip_top < 0:
            raise ValueError("skip values cannot be lower than 0")

        self.filename = filename
        self.sep = sep
        self.as_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.header = []

    def __enter__(self):
        try:
            with open(self.filename, 'r') as fp:
                reader = csv.reader(fp, delimiter=self.sep)
                self.header = next(reader)
                column = len(self.header)
                skip_bottom = self.skip_bottom
                if self.as_header is False:
                    if self.skip_bottom == 0:
                        self.data.append(self.header)
                    else:
                        skip_bottom -= 1
                    self.header = None
                for i, row in enumerate(reader):
                    if (column != len(row)):
                        raise IndexError("Row {} of length {} \
                                         VS Header of length {}"
                                         .format(i + 2, len(row), column))
                    for val in row:
                        if val is "" or val is None:
                            raise IndexError("Row {} has an empty value"
                                             .format(i + 2))
                    if skip_bottom > 0:
                        skip_bottom -= 1
                    else:
                        self.data.append(row)
                if self.skip_top > 0:
                    del self.data[-self.skip_top:]
        except (OSError, IndexError) as e:
            print("Error: {}.".format(e))
            self = None
        return self

    # __exit__ must have those 4 arguments in its signature even if unused
    def __exit__(self, type, value, traceback):
        return

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header
