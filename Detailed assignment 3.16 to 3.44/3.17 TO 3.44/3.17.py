#3.17 Use the eval()function to evaluate these strings as Python expressions:
hello='hellow'
print(eval('2*3+1'))
print(eval('hello'))#name error come if hellow is not defined
print(eval("'hello'+' '+'world!'"))
print(eval("'ASCII'.count('I')"))
print(eval('x = 5'))#since it is an statement,it wil give syntax error, we should use expressions

