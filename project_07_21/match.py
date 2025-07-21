# Python 3.10 이상 제공
# switch-case => match-case

a = 1

# match-case : break 필요없음. default 대신에 case _: 사용
match a:
    case 0:
        print("0입니다.")
    case 1:
        print("1입니다.")
    case 2:
        print("2입니다.")
    case _:
        print("default입니다.")