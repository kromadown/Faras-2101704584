var = 'abcba'
var = var.casefold()
rev_var = reversed(var)

if list(var) == list(rev_var):
    print ("It's Palindrome")
else:
    print ("It's not Palindrome")
