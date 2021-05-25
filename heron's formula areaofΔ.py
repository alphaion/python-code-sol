def areaTriangle(sidea, sideb, sidec):
    x = (sidea+sideb+sidec)/2
    a = (x*(x-sidea)*(x-sideb)*(x-sidec))**1/2
    return a
def main():
    side1 = float(input('Side 1: '))
    side2 = float(input('Side 2: '))
    side3 = float(input('Side 3: '))
    areaTri = areaTriangle(side1, side2, side3)
    print(areaTri, 'is a area of Triangle.')
if __name__=='__main__':
          main()