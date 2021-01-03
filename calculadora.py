import math


menu="""

Select an option to calculate

1 - Sin
2 - Cos
3 - Tan
4 - ln

"""

option=int(input(menu))

def petition():
    number=float(input('Submit a value: '))
    return number

def calculate():
    if option == 1:
        number = petition()
        result = math.sin(number)
        result = round(result,3)
        result = str(result)
        number = str(number)  
        print('The sinus of ' + number + ' is ' + result) 
    elif option == 2:
        number = petition()
        result = math.cos(number)
        result = round(result,3)
        result = str(result)
        number = str(number)  
        print('The cosine of ' + number + ' is ' + result)
    elif option == 3:
        number = petition()
        result = math.tan(number)
        result = round(result,3)
        result = str(result)
        number = str(number)  
        print('The tangent of ' + number + ' is ' + result)
    elif option == 4:
        number = petition()
        result = math.log(number)
        result = round(result,3)
        result = str(result)
        number = str(number)  
        print('The natural logarithm of ' + number + ' is ' + result)
    else:
        print('Please, insert a valid option')


if __name__ == "__main__":
    calculate()  