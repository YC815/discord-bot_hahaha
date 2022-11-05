import random
import time          # import time 模組
answer = []
for i in range(4):
    answer.append(random.randint(0, 9))
print(answer)
a = b = n = 0
num = 0              # 新增 num 變數為 0，作為計算次數使用
t = time.time()      # 新增 t 變數為現在的時間
while a != 4:
    num += 1         # 每次重複時將 num 增加 1
    a = b = n = 0
    user = list(input('輸入四個數字：'))
    for i in user:
        if int(user[n]) == answer[n]:
            a += 1
        else:
            if int(i) in answer:
                b += 1
        n += 1
    output = ','.join(user).replace(',', '')
    print(f'{a}A{b}B')
t = round((time.time() - t), 3)                # 當 a 等於 4 時，計算結束和開始的時間差
print(f'答對了！總共猜了 {num} 次，用了 {t} 秒')   # 印出對應的文字
# import random
# count = 0
# ans = str(random.randint(0, 9999))
# for a in ans:
#     count += 1
# if count == 0:
#     ans = '0000'
# elif count == 1:
#     ans = '000' + ans
# elif count == 2:
#     ans = '00' + ans
# elif count == 3:
#     ans = '0' + ans

# inp = ''
# count = 0
# a = 0
# b = 0
# while inp != ans:
#     inp = str(input("輸入猜測: "))
#     for i in inp:
#         count += 1
#     if count != 4:
#         print("請輸入四位數字")
#         print()
#         count = 0
#         continue
#     count = 0
#     if inp[0] == ans[0]:
#         a += 1
#     if inp[1] == ans[1]:
#         a += 1
#     if inp[2] == ans[2]:
#         a += 1
#     if inp[3] == ans[3]:
#         a += 1

#     if inp[0] in ans and inp[0] != ans[0]:
#         b += 1
#     if inp[1] in ans and inp[1] == ans[1]:
#         b += 1
#     if inp[2] in ans and inp[2] == ans[2]:
#         b += 1
#     if inp[3] in ans and inp[3] == ans[3]:
#         b += 1
#     print("%dA%dB" % (a, b))
#     print()
#     count = 0
#     a = 0
#     b = 0
# print("恭喜猜中！ 謎底: %s" % (ans))
