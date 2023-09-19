from main import *



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert quadratic_multiply(BinaryNumber(4), BinaryNumber(16)) == 4*16
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(5)) == 10*5
  assert quadratic_multiply(BinaryNumber(8), BinaryNumber(12)) == 8*12
