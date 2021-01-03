from math import sin,cos,tan,log

print("""
Operations available

- Sinus
- Cosene
- Tangent
- Natural logarithm

""")

def apply_funtion(f,n):
    function={
        'sin':sin,
        'cos':cos,
        'tan':tan,
        'ln':log
    }
    result = {}
    for i in range(1, n+1):
        result[i]=function[f](i)
    return result


def calculate():
   f=input('Submit the operation to be carried out: ')
   n=int(input('Submit a number: '))
   for i, j in apply_funtion(f,n).items():
       print(i, round(j,2))


if __name__ == "__main__":
    calculate() 