

def number_of_bottles():
    x = 100
    for n in range(1,99):
        print(100 -n,'bottles of milk on the wall, ',end='')
        print(100 -n,'bottles of milk.')
        print('Take one down and pass it around, ',end='')
        print(100 -n-1,'bottles of milk on the wall.')
        print('')
    print('1 bottle of milk on the wall, 1 bottle of milk.')
    print('Take one down and pass it around, no more bottles of milk on the wall.')
    print('')
    print('No more bottles of milk on the wall, no more bottles of milk.')
    print('Go to the store and buy some more, 99 bottles of milk on the wall.')
    print('')
    
number_of_bottles()