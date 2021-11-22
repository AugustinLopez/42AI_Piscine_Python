from copy import deepcopy
from typing import List, Tuple, Optional


class Matrix:
    @property
    def row(self) -> int:
        return self.shape[0]

    @property
    def col(self) -> int:
        return self.shape[1]

    @row.setter
    def row(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Expected int. Got " + str(type(value)))
        elif value < 0:
            raise ValueError("Expected positive int")
        self.shape = (value, self.shape[1])

    @col.setter
    def col(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Expected int. Got " + str(type(value)))
        elif value < 0:
            raise ValueError("Expected positive int")
        self.shape = (self.shape[0], value)

    def __init_tuple(self, args: Tuple[int, int]):
        """Tuple initialization give an empty matrix of size (x,y)"""
        if len(args) != 2:
            raise ValueError("Expected 2 elements. Got " + str(len(args)))
        if not (isinstance(args[0], int) and isinstance(args[1], int)):
            raise TypeError("Expected (int, int). Got (" 
                            + str(type(args[0])) + "," 
                            + str(type(args[1])) + ")")
        self.shape = args
        if self.row <= 0 or self.col <= 0:
            raise ValueError("Dimensions must be strictly positive")
        self.data = [[0.0] * self.col for _ in range(self.row)]

    def __init_list_of_list(self, args: List[List[float]]):
        if len(args) == 0:
            raise ValueError("Encompassing list cannot be empty")
        if not isinstance(args[0], list):
            raise TypeError("Expected list. Got " + str(type(args[0])))
        self.row = len(args)
        self.col = len(args[0])
        self.data = [[0.0] * self.col for _ in range(self.row)]
        for c in range(self.col):
            try:
                self.data[0][c] = float(args[0][c])
            except ValueError:
                raise ValueError("Cannot convert element [0," + str(c) + "] to float")
            except TypeError:
                    raise TypeError("Cannot convert element [0," 
                                     + str(c) + "] to float")
        for i, r in enumerate(args[1:], 1):
            if len(r) != self.col:
                raise ValueError("Inconsistent matrix dimension")
            for c in range(self.col):
                try:
                    self.data[i][c] = float(args[i][c])
                except ValueError:
                    raise ValueError("Cannot convert element [" 
                                     + str(i) + "," + str(c) + "] to float")
                except TypeError:
                    raise TypeError("Cannot convert element [" 
                                     + str(i) + "," + str(c) + "] to float")

    def __init__(self, args):
        self.data: List[List[float]] = [[]]
        self.shape: Tuple[int, int]  = (0, 0)
        if isinstance(args, list):
            self.__init_list_of_list(args)
        elif isinstance(args, tuple):
            self.__init_tuple(args)
        elif isinstance(args, Matrix):
            self.data = deepcopy(args.data)
            self.shape = args.shape
        else:
            raise TypeError(str(type(args)) + " not supported")

    def T(self):
        """Return the transpose of the matrix"""
        return Matrix([list(i) for i in zip(*self.data)])

    def _add_help(self, other, mul = 1):
        if not isinstance(other, Matrix):
            raise TypeError("Expected Matrix or subclass. Got "
                            + str(type(other)))
        if self.shape != other.shape:
             raise ValueError("Expected same shape. Got " 
                              + str(self.shape) + " != " + str(other.shape))
        tmp = [[0.0] * self.col for _ in range(self.row)]
        for r in range(self.row):
            for c in range(self.col):
                tmp[r][c] = self.data[r][c] + mul * other.data[r][c]
        return tmp
  
    def __add__(self, other):
       return Matrix(self._add_help(other))

    def __sub__(self, other):
       return Matrix(self._add_help(other, -1))

    def __rsub__(self, other):
       return self.__sub__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def _div_help(self, other, reverse = False):
        if isinstance(other, Matrix):
            if other.shape != (1, 1):
                raise ValueError("Matrix instance is not a scalar")
            divisor = other.data[0][0]
        elif isinstance(other, int) or isinstance(other, float):
            divisor = float(other)
        else:
            raise TypeError("Expected float or int. Got" + str(type(other)))
        if divisor == 0.0:
            raise ZeroDivisionError("Cannot proceed")
        if reverse:
            tmp = [[divisor / self.data[0][0]]]
        else:
            tmp = deepcopy(self.data)
            for r in range(self.row):
                for c in range(self.col):
                    tmp[r][c] /= divisor
        return tmp

    def __truediv__(self, other):
        return Matrix(self._div_help(other))

    def __rtruediv__(self, other):
        if self.shape != (1, 1):
            raise TypeError("Matrix instance is not a scalar")
        elif self.shape[0][0] == 0:
            raise ZeroDivisionError("Cannot proceed")
        return Matrix(self._div_help(other, True))
    
    def __scalar_mul(scalar, obj):
        tmp = deepcopy(obj.data)
        for r in range(obj.row):
            for c in range(obj.col):
                tmp[r][c] *= scalar
        return tmp

    def _mul_help(self, other):
        if isinstance(other, Matrix):
            if other.shape == (1, 1):
                return self.__scalar_mul(other.data[0][0], self.data)
            elif self.shape == (1, 1):
                return self.__scalar_mul(self.data[0][0], other.data)
            elif self.col == other.row and self.row == other.col:
                tmp = [[0.0] * other.col for _ in range(self.row)]
                transpose = [list(i) for i in zip(*other.data)]
                for r in range(self.row):
                    for c in range(other.col):
                        tmp[r][c] = map(lambda x, y: x * y, (self[r], transpose[c]))
            else:
                raise TypeError("")
            return tmp
        elif isinstance(other, int) or isinstance(other, float):
            return self.__scalar_mul(other, self.data)

    def __str__(self):
        return (str(self.data))
    
    def __repr__(self):
        return (str(self))

class Vector(Matrix):
    def __add__(self, other):
        return Vector(self._add_help(other))
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
       return Vector(self._add_help(other, -1))

    def __rsub__(self, other):
       return self.__sub__(other)

    def __truediv__(self, other):
        return Vector(self._div_help(other))

    def __rtruediv__(self, other):
        if self.shape != (1, 1):
            raise TypeError("Matrix instance is not a scalar")
        elif self.shape[0][0] == 0:
            raise ZeroDivisionError("Cannot proceed")
        return Vector(self._div_help(other, True))

    def __init__(self, args):
        if isinstance(args, Vector):
            pass
        elif isinstance(args, Matrix):
            if not args.row == 1 and not args.col == 1:
                raise ValueError("Expected dimension of (X,1) or (1,Y). Got ("
                                + (str(len(args)) + "," 
                                + str(len(args[0])) + ")"))
        elif isinstance(args, list):
            if (len(args) > 0):
                if not isinstance(args[0], list):
                    raise TypeError("Expected list[list]. Got list[" 
                                    + str(type(args[0])) + "]")
                if not len(args) == 1 and not len(args[0]) == 1:
                    raise ValueError("Expected dimension of (X,1) or (1,Y). Got ("
                                    + (str(len(args)) + "," 
                                    + str(len(args[0])) + ")"))
        else:
            raise TypeError(str(type(args)) + " not supported")
        super().__init__(args)
        