from tkinter import *

root = Tk()
root.geometry("640x480")

ent_value = StringVar()

def click():
    print(ent_value.get())

# pack(), grid(), place()

btn = Button(root, text="Button", command=click)
# btn.pack()

# grid() : 격자 방식
btn.grid(row=0, column=0)

# place() : 좌표 값을 따라서 지정
# btn.place(x=50, y=50)

ent = Entry(root, textvariable=ent_value)
# ent.pack()

menubar = Menu(root)
menu_1 = Menu(menubar, tearoff=False)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

root.config(menu=menubar)
root.mainloop()