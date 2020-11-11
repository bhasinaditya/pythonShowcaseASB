######################################################
# Program to display exception handling

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

######################################################
# This chunk shows exception does not return pointer back to try block


def spam2(dividedBy):
        return 42 / dividedBy


try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spam2(1))
except ZeroDivisionError:
    print('Error: Invalid Argument')

######################################################