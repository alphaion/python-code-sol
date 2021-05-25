def rightTriangle(n):
    for i in range(1,n+1):
        print('#'*i)
def invertedTriangle(n):
    ns = 0
    nsa = 2*n-1
    for i in range(1,n+1):
        print(''*ns +'*'*nsa)
        nsa -=2
        ns +=1
def main():
    x = int(input('Enter 1 for right triangle.\n'+'Enter 2 for inverted triangle.\n'))
    assert x ==1 or x ==2
    n = int(input('Enter Rows: '))
    if x ==1:
        rightTriangle(n)
    else:
        invertedTriangle(n)        
if __name__=='__main__':
      main()