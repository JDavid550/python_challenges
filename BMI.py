import math

def bmi(mass,height):
    
    bmi=mass/height
    bmi=round(bmi,2)
    bmi=str(bmi)
    return bmi
    
    
def analysis(mass,height):

    message=bmi(mass,height)
    message=float(message)
    message= math.floor(message)
    
    if message < 18.5:
        print('You weight less than expected')
    elif 18.5 < message > 24.9:
        print('Your weight is normal for your size')
    elif 25 < message >29.9:
        print('You weight more than expected')
    elif message >= 30:
        print ('You suffer obesity')
    

def run():
    
    while True:
        mass=input('Submit your mass in Kg: ')
        try:
            mass=float(mass)
            break
        except ValueError:
            print('Submit a valid value')  
    while True:
        height = input('Submit your height meters: ')
        try:
            height=2**float(height)
            break
        except ValueError:
            print('Submit a valid value')

    print('Your body mass index is ' + bmi(mass,height))
    analysis(mass,height)
    
if __name__ == "__main__":
    run()