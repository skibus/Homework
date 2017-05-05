print ('''Welcome! If you want to convert number from:
1)Decimal to binary type your number and after space type 10 i.e. 244 10
2)Binary to decimal type your number and after space type 2 i.e. 1111 2\n''')
number = input('What is you number? ')
num_type = number.split(' ')
num = num_type[0]
print (num)


def convert_bin_to_dec(num):
    result = 0
    decimal_number = []
    '''Function converting binary numbers to decimal numbers'''
    for i in range(len(num)):
        if num[i] == '1':
            x = 2 ** (len(num)-i-1)      
            decimal_number.append(x)
        elif num[i] == '0':
            decimal_number.append(0)
        else:
            print ('You didnt enter binary number.')
            exit()
    for i in decimal_number:                # adding numbers in result
        result = result + i
    print (result)

def convert_dec_to_bin(num):
    binary_number = []
    '''Function converting decimal numbers to binary numbers'''
    num = int(num_type[0])
    while num != 0:
        rest = num % 2
        rest = int(rest)
        binary_number.append(rest)
        if rest == 1:
            num = (num - 1) / 2
        else:
            num = num / 2
    for i in binary_number:
        print (i, end='')
    print ('\n')


def main():

    if num_type[1] == '2':  #if the the last number is 'space + 2' we know that input number is bin
        convert_bin_to_dec(num)
    elif num_type[1] == '10':
        convert_dec_to_bin(num)
    else:
        print ('You entered incorrect form of number.')

if __name__ == 'main':
    main()

main()
