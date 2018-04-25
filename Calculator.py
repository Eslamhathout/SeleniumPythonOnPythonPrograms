
try:
    def add(x,y):
        if type(x) == String:
		             try:
			                      x = int(x)
		             except:
			                      raise TypeError('You can not pass strings to add func')
        elif type(y) == string:
		             try:
			                      y = int(y)
		             except:
			                      raise TypeError('You can not pass strings to add func')
        return x + y
except TypeError:
    raise ValueError('To use add pass only 2 numbers.')


def sub(x,y):
    return x-y

try:
    def multiply(x,y):
        return x*y
except TypeError:
    raise TypeError('To use multiply pass only 2 numbers.')

def divide(x,y):
    if y ==0:
        raise ValueError('Can not divide by Zero')
    return float(x)/y
