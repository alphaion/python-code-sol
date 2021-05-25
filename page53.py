def student(number):
    if number>=90 and number<=100:
        grade = 'A'
    elif number>=70 and number<=89:
         grade = 'B'
    elif number>=50 and number<=69:
         grade = 'C'
    elif number>=40 and number<=49:
         grade = 'D'
    else:
         grade = 'F'
    return grade
def main():
    number = int(input('Enter Your Number: '))
    message = student(number)
    print(message)
if __name__=='__main__':
    main()