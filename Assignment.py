var = 'abcba'
var = var.casefold()
rev_var = reversed(var)

if list(var) == list(rev_var):
    print ("It's Palindrome")
else:
    print ("It's not Palindrome")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

result = [fib(n) for n in range (1,11)]
print (result)
