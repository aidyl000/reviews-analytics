data = []
count = 0 # 讓他每讀1000筆就印一次
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # % 是用來求餘數
            print(len(data)) # 每讀一行就把長度印出來
print('檔案讀取完了', '總共有', len(data), '筆資料')

sum_len = 0 # 加總
for d in data: # 每一筆留言的長度
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))