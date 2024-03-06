# Sample taken from pyStritch Github repository
# https://github.com/mmulqueen/pyStritch
from pystritch.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())
