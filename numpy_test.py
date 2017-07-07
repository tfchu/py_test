import numpy as np

def test():
    #x = np.array([2, 3, 1, 0])
    x = np.arange(10)   # 0, 1, 2, ... 9
    
    # see numpy, array indexing
    #2d
    x.shape = (2, 5)    # break into 2 rows, 5 elements each
                        # 0, 1, 2, 3, 4
                        # 5, 6, 7, 8, 9
    print(x)            # whole thing
    print(x[1])         # 2nd row, which is sub-dimensional array
    print(x[1, 3])      # 2nd row, 4th column
    print(x[1][3])      # same but temp array is created (2nd row)

    #2d: goal is to replace elements that are multiples of 3
    # with (next element - previous element + self) among the multiples of 3 list
    x = np.arange(35).reshape(5, 7)
    print(x)
    print(x[1:5:2, ::3])    # row: 1, 3; col: 0, 3, 6
    
    x = np.ravel(x)         # convert back to 1d array, see also flatten/concatenate
    print(x)

    multiple_of_three_index = np.where(x % 3 == 0)[0]   # find the indexes of multiples of 3
    print(multiple_of_three_index)
    tmp = x[multiple_of_three_index]                    # tmp array holding values of the indexes
    print(tmp)
    tmp[1:-1] = tmp[:-2] - tmp[2:] + tmp[1:-1]          # do the math
    #x[1:34] = (x[0:33] - x[2:35]) / 2
    print(tmp)
    x[multiple_of_three_index] = tmp                    # replace original elements with new values
    print(x)
    print(x.reshape(5, 7))                              # convert back to 5 x 7 array
    

if __name__ == '__main__':
    test()