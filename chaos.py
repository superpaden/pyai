import random
people = input("有幾個要玩: ")
num = int(people)

giver_change = random.sample(list(range(1,num+1)),num)
gift_change = random.sample(list(range(1,num+1)),num)
receiver_change = random.sample(list(range(1,num+1)),num)


for i in range(1,num+1):
    a= giver_change.pop()
    b= gift_change.pop()
    c= receiver_change.pop()
  
    if a == c :
        print(f"顆顆,{a}號你這個聖誕邊緣人^_^")
        print(f'請拿{b}號禮物，送給你自己')
        print(" ")
        input("按任意鍵繼續")
        print(' ')
    else:
        print(f'{a}號請拿{b}號玩家帶來的禮物給{c}號')
        print(' ')
        input("按任意鍵繼續")
        print(' ')
