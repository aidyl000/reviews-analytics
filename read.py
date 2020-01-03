data = []
count = 0 # 讓他每讀1000筆就印一次
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # % 是用來求餘數
            print(len(data)) # 每讀一行就把長度印出來
print(data[0])
print('(╬•᷅д•᷄╬)')
print(data[1])