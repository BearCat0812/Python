import tkinter as tk

# 설정값
BALL_SIZE = 30
SPEED_X = 3
SPEED_Y = 2

# 초기화
window = tk.Tk()
window.title("공 튀기기")
canvas = tk.Canvas(window, width=500, height=400, bg="white")
canvas.pack()

# 공 만들기 (처음 위치는 x=50, y=50)
ball = canvas.create_oval(50, 50, 50 + BALL_SIZE, 50 + BALL_SIZE, fill="red")

# 공의 이동 방향
dx = SPEED_X
dy = SPEED_Y

# 애니메이션 함수
def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)
    
    # 현재 공의 좌표 확인
    x1, y1, x2, y2 = canvas.coords(ball)

    # 벽에 닿았는지 확인하고 방향 전환
    if x1 <= 0 or x2 >= canvas.winfo_width():
        dx = -dx
    if y1 <= 0 or y2 >= canvas.winfo_height():
        dy = -dy

    # 일정 시간 후 다시 실행 (재귀적으로 반복)
    window.after(10, move_ball)

# 시작
move_ball()

window.mainloop()
