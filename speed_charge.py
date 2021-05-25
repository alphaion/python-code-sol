def speed_limit(speed):
    if speed <=90:
        message = 'No Punishment and No Warning'
    if speed>=91 and speed<=110:
        warn = (speed-90)*300
        message = warn,'Warning'
    if speed>110:
        warn = (speed-90)*500
        message = warn,'License Removed'
    return message
def main():
    speed = int(input('Enter Speed'))
    myfunc = speed_limit(speed)
    print(myfunc)
if __name__=='__main__':
    main()