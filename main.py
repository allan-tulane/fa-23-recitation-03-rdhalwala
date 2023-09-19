"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)
  n = len(xvec)

  
  if (x.decimal_val <= 1) and (y.decimal_val <= 1):
    return BinaryNumber(x.decimal_val * y.decimal_val)



  else:
    #call split number to split xvec and yvec in half
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    
    
    #recursive
    #xleft*yleft
    left_product = _quadratic_multiply(x_left, y_left)
    #make binary of 2 for number
    #multiply b 2^n with bit shift
    part_1 = bit_shift(left_product, n)

    #xl times yr
    left_right = _quadratic_multiply(x_left, y_right)
    #xr times yl
    right_left = _quadratic_multiply(x_right, y_left)
    #sum
    left_right_sum = BinaryNumber(left_right.decimal_val + right_left.decimal_val)
    #multiply sum by 2^n/2
    part_2 = bit_shift(left_right_sum, n//2)

    
    #xr times yr
    part_3 = _quadratic_multiply(x_right, y_right)

    

    #sum
    result = BinaryNumber(part_1.decimal_val + part_2.decimal_val + part_3.decimal_val)


    return result

    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000


    
    

