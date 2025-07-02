from tkinter import *
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete(1.0, END)
            text_area.insert(END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, END))
        messagebox.showinfo("저장 완료", "파일이 성공적으로 저장되었습니다!")

root = Tk()
root.title("간단 메모장")
root.geometry("500x400")

# 메뉴 생성
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=root.quit)

# 텍스트 입력 영역
text_area = Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

root.mainloop()