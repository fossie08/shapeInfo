import math 
PI = math.pi

def cone():
    def calcSurfaceArea(height, radius):
        #calculates the slant length 
        slantLength = (height**2) + (radius**2)
        slantLength = math.sqrt(slantLength)

        #calculates the base area 
        baseArea = (radius**2) * PI 

        #calculates the the lateral surface area 
        lateralSurfaceArea  = radius * slantLength * PI 

        return baseArea + lateralSurfaceArea
    

    def calcVolume(height, radius): 
        volume = (1/3) * PI * (radius**2) * height 
        return volume


    #receiving dimension inputs for the user. Checks if input is a floating number 
    while True:
        try: 
            height = float(input('Please enter height of the cone: '))
            break
        except ValueError: 
            print('Please enter a number')
    while True: 
        try: 
            radius = float(input('Please enter radius of the base of the cone: '))
            break
        except ValueError: 
            print('Please enter a number')


    coneSurfaceArea = round(calcSurfaceArea(height, radius),2)
    coneVolume = round(calcVolume(height, radius),2)


    print (f'The surface area of the cone is: {coneSurfaceArea}')
    print(f'The volume of the cone is: {coneVolume}')


cone()