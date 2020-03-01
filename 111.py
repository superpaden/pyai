import random
print("歡迎使用晚餐小幫手")
print("請輸入你想吃的晚餐選項")
print("輸入完後請輸入0")
L = []
while  True:
    a = input(":" )
    if a == "0":
        break
    else:
        L.append(a)
random.shuffle(L)
print(f'你今天吃的是 {L.pop(0)}' )
input("按下enter 結束程式")