n=int(input())
#map system
candles_height = map(int,input().split())
#creAte list
list = list(candles_height)
max_ = max(list)
counts = list.count(max_)
print(counts)