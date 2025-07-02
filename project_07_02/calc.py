from tkinter import *

root = Tk()
root.geometry("200x200")

ent_value = StringVar()

def click(char):
    # 현재 Entry 내용 가져오기
    current = ent_value.get()
    # 'C' 버튼 클릭 시 초기화
    if char == 'C':
        ent_value.set("")
    # '=' 버튼 클릭 시 계산 후 출력
    elif char == '=':
        try:
            result = str(eval(current))  # 계산 결과
            ent_value.set(result)
        except:
            ent_value.set("Error")
    else:
        # 그 외 버튼은 누적해서 입력
        ent_value.set(current + char)


ent = Entry(root, textvariable=ent_value)
ent.grid(row=0, column=1, columnspan=5)

buttons = [
    ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
    ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4),
    ('C', 4, 1), ('0', 4, 2), ('=', 4, 3), ('+', 4, 4)
]

for (text, r, c) in buttons:
    Button(root, text=text, width=3, command=lambda char=text: click(char)).grid(row=r, column=c)

root.mainloop()