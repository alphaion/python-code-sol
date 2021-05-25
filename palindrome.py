def palin(x):
    if x == '':
        return True
    else:
        return (x[0]==x[-1] and palin(x[1:-1]))
def main():
    x = input('')
    if palin(x):
        print('Palin confirm')
    else:
        print('Not at all')
if __name__ == '__main__':
    main()