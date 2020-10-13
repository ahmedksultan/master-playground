import numpy as np

# numpy main object is ndarray
     # homogenous multidimensional array
     # dimensions are AXES, # of axes is called rank
     # how to make arrays in numpy:
     
          # np.array([1, 2, 3])

          # np.ones((r, c), dtype=)
               # makes r rows, c columns with 1
               # dtype can be subbed out (np.int16, np.bool)

          # np.full((r, c), num, dtype=)
               # same as .ones(), but with a # num

          # np.arange(start, stop, jump)
               # makes array from [start, stop), with jump

          # np.linspace(start, stop, num_incr)
               # makes array from [start, stop] with num_incr jumps

          # np.random.rand((r, c))
               # makes array r x c, with random numbers (0, 1)

          # np.empty((r, c))
               # makes array r x c  with unitialized values

# array attributes
     # ndim    :: returns dimensions of array
     # shape   :: returns tuple of integers, indicating array size
     # size    :: returns total # of elements
     # dtype   :: returns type of elements
     # itemsize:: returns size of bytes in each item
     # arange  :: returns ndarray of evenly spaced values
     # reshape :: reshapes numpy array

# array slicing
     # MODIFYING SLICES MODIFIES ORIGINAL
          # .copy() prevents this
     # array[x:y] modifies [x, y) indices in array
     # boolean indexing

# numpy broadcasting
     # when arrays do not have the same rank, 1 will be added to smaller ranking arrays until ranks match
     # when either dimension comapres to 1, the other is used (dimensions of size 1 stretched to match other)

# math and numpy 
     # basic mathematical and statistical functions: mean, max, min, sum, prod, std, var, sum, 
     # additions, subtraction, product, dot product, division, modulo, exponents, 
     # conditional operations

     # linear equations 
          # 2x + 6y = 6
          # 5x + 3y = -9

          #import numpy as np
          #coeffs  = np.array([[2, 6], [5, 3]])
          #depvars = np.array([6, -9])
          #solution = np.linalg.solve(coeffs, depvars)
          #print(solution)