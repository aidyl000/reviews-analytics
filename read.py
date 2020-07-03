data = []
count = 0 # 讓他每讀1000筆就印一次
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # % 是用來求餘數
            print(len(data)) # 每讀一行就把長度印出來
print('檔案讀取完了', '總共有', len(data), '筆資料')

print(data[0])

# 文字計數
sum_len = 0 # 加總
for d in data: # for loop 把清單中的東西一個一個拿出來
    sum_len = sum_len + len(d) # 每一筆留言的長度
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100: # 以字母計算
        new.append(d)
print('一共有', len(new), '筆留言長度小於100') 
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d: # 'a' in 'abc' -> True
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[5]) 

wc = {} # word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc: # 如果這個字有出現在字典裡，沒出現就加個not
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Lydia'])

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為：', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')

   