from math import sin,cos,tan,log

print("""
Operations available

[1]-sin
[2]-cos
[3]-tan
[4]-ln

""")

epsilon=0.01
def apply_funtion(f,n):
    function={
        1:sin,
        2:cos,
        3:tan,
        4:log
    }
    result = {}
    for i in range(1, n+1):
        result[i]=function[f](i)
    return result


def calculate():
    
    while True:
        f=input('Submit the operation to be carried out: ')
        try:
            f = int(f)
            if f > 4 or f < 0:
                print('You can only select one of the four operations above')
                calculate()
            break
        except ValueError:
            print('Please, submit a number according to the operations above')

    if int(f)<5:
        while True:
            n=input('Submit a number: ')
            try:
                n=int(n)
                break
            except ValueError:
                print('Please, submit a number')

        for i, j in apply_funtion(f,n).items():
            print(i, round(j,2))
        print('These results are in radians')

                                
if __name__ == "__main__":
    calculate() 