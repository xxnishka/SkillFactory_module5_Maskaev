def welcome():
    print("======================")
    print("   Добро прожаловать  ")
    print("в игру крестики-нолики!")
    print("======================")
    print("Чтобы начать играть, ")
    print("введите координаты строки (X),")
    print("а затем через пробел ")
    print("координаты столбца (Y).")


def show_field():
    print()
    print("   | 0 | 1 | 2 | "    )
    print("----------------")
    for i, row in enumerate(field):
        row_str = f' {i} | {" | ".join(row)} | '
        print(row_str)
        print("----------------")


def enter_position():
    while True:

        coordinate = input("       Ваш ход:").split()

        if len(coordinate) != 2:
            print(" Введите две координаты! ")
            continue

        x, y = coordinate

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числовые значения! ")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2 :
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def winner():
    winner_pos = (((0, 0), (0, 1), (0, 2)),
                  ((1, 0), (1, 1), (1, 2)),
                  ((2, 0), (2, 1), (2, 2)),
                  ((0, 0), (1, 0), (2, 0)),
                  ((0, 1), (1, 1), (2, 1)),
                  ((0, 2), (1, 2), (2, 2)),
                  ((0, 0), (1, 1), (2, 2)),
                  ((0, 2), (1, 1), (2, 0)))

    for pos in winner_pos:
        symb = []

        for i in pos:
            symb.append(field[i[0]][i[1]])

        if symb == ["X", "X", "X"]:
            print(" Выиграли крестики ")
            return True

        if symb == ["0", "0", "0"]:
            print(" Выиграли нолики ")
            return True

    return False


welcome()
field = [[' '] * 3 for i in range(3)]
step_number = 0

while not winner():
    step_number +=1

    show_field()

    if step_number%2 == 1:
        print(' Ходит крестик ')
    else:
        print(' Ходит нолик ')

    x, y = enter_position()

    if step_number%2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    show_field()

    if step_number == 9:
        print(" Ничья ")
        break





