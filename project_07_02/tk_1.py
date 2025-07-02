from tkinter import *

root = Tk()
root.title("Hello Tkinter")
root.geometry("640x480")

# label = Label(root, text="Hello Tkinter!!")
# label.pack()

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# 사각형
canvas.create_rectangle(50, 50, 150, 150, fill="skyblue")

# 원
canvas.create_oval(170, 50, 270, 150, fill="lightgreen")

# 선
canvas.create_line(0, 0, 300, 300, fill="red", width=2)

# 텍스트 : create_text(x, y, text="내용")
# 이미지 : create_image(x, y, image="이미지 경로")

root.mainloop()