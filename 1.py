import tkinter as tk
from PIL import ImageTk, Image
import sys
print("轟隆轟隆")
print("小明: 為甚麼我會在這裡?")
win = tk.Tk()
win.title("1")
win.geometry("1280x720")
win.configure(background='white')

path = "1.png" 
img=ImageTk.PhotoImage(Image.open(path)) 
lab1=tk.Label(win, image=img)

lab1.pack()
win.mainloop()

pic=Image.open(path)
print("這時候應該做甚麼?")
print("a 放置play甚麼都不做")
print("b 總之先做些甚麼")
print("c 來問問神奇海螺")


while True :
    a = input()
    if a in {'a','b'}:
        win = tk.Tk()
        win.title("2")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "2.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        sys.exit(0)
       
        
    elif a == "c":
        win = tk.Tk()
        win.title("3")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "3.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        break
    else:
        print("請重新輸入ZZ")
        continue

print("看來小明十分遵守呢")
print("="*30)
print("過了一陣子後小明餓了 於是....")
print("a 離開這裡不遵守神奇海螺的指示")
print("b 繼續遵守")
print('c 那我要睡啦 在cosco哭 哭整整一小時  哀有 他的手可以穿過我的巴巴阿')

while True :
    a = input()
    if a in {'a','b'}:
        win = tk.Tk()
        win.title("2")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "2.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        sys.exit(0)
    elif a == "c":
        win = tk.Tk()
        win.title("4")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "4.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        break
    else:
        print("請重新輸入ZZ")
        continue
print("獲得了替身 效果十分顯著?")
print("="*30)
print("這時候應該做甚麼呢?")
print("a 組成月晨遠征軍 打倒 CIO")
print("b 找尋異世界入口")
print("c 撒撒給優")

while True :
    a = input()
    if a in {'a','b'}:
        win = tk.Tk()
        win.title("2")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "2.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        sys.exit(0)
    elif a == "c":
        win = tk.Tk()
        win.title("5")
        win.geometry("1280x720")
        win.configure(background='white')

        path = "5.png" 
        img=ImageTk.PhotoImage(Image.open(path)) 
        lab1=tk.Label(win, image=img)

        lab1.pack()
        win.mainloop()
        break
    else:
        print("請重新輸入ZZ")
        continue
print("最終小明與五子結為連理")
print("可喜可賀")
input("enter結束")
