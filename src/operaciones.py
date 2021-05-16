def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b
    
if __name__ == "__main__": 
	a = 23.0
	b = 12.0

	print("{} + {} = {}\n".format(a, b, suma(a,b)))
	print("{} - {} = {}\n".format(a, b, resta(a,b)))
	print("{} * {} = {}\n".format(a, b, multiplicacion(a,b)))
	print("{} / {} = {}".format(a, b, division(a,b)))

