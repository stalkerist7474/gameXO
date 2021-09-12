import random

user = ''  # знак игрока
ai = ''  # знак компьютера
turn = ''  # переменная чей следующий ход
field = [
    [" ", "0", "1", "2"],
    ["0", " ", " ", " "],
    ["1", " ", " ", " "],
    ["2", " ", " ", " "]
]


def start_game_choice():
    player_choice = input("Введите Y если хотите начать игру-")
    if player_choice == 'Y':
        print('Игра началась!')
        game()
    else:
        print('Programm stop')
        return

def game():
    side_init()
    side_action(turn)


def side_init():
    global user
    global ai

    print('выберите сторону за которую играть X или 0, X ходит первым')
    user = input("Введите знак стороны-")
    global turn
    if user == 'X':
        ai = '0'
        turn = 'turn_user'  # ход человека
    elif user == '0':
        ai = 'X'
        turn = 'turn_ai'  # ход компа
    else:
        print('неправильно введена сторона, попробуйте еще')
        return side_init()


def gametable():
    for i in field:
        print(*i)


def side_action(turn):
    if turn == 'turn_user':
        user_action()
    elif turn == 'turn_ai':
        ai_action()
    else:
        print('ошибка хода')


def user_action():
    gametable()
    print('Ходят -', user)
    a = int(input("Номер строки вашего хода -"))
    b = int(input("Номер столбца вашего хода -"))
    if 0 <= a <= 2 and 0 <= b <= 2:
        if field[a + 1][b + 1] == " ":

            field[a + 1][b + 1] = user

            if check_win():
                print('Победили', user)
                return
            elif check_draw():
                return

            next_turn = 'turn_ai'
            side_action(next_turn)
        elif field[a + 1][b + 1]:
            print('клетка занята введите координаты еще раз')
            user_action()
    else:
        print('Ошибка при вводе координат, введите снова')
        return user_action()

def ai_action():
    c = random.randint(0, 2)
    d = random.randint(0, 2)
    n = 0
    if field[c + 1][d + 1] == " ":
        field[c + 1][d + 1] = ai
        if check_win():
            print('Победили', ai)
            return
        elif check_draw():
            return
        next_turn = 'turn_user'
        side_action(next_turn)
    elif field[c + 1][d + 1]:
        print('клетка занята, комп ты че?')
        ai_action()


def check_win():
    if field[1][1] == "X" and field[1][2] == "X" and field[1][3] == "X":
        print("Победили крестики")
        return True
    elif field[2][1] == "X" and field[2][2] == "X" and field[2][3] == "X":
        print("Победили крестики")
        return True
    elif field[3][1] == "X" and field[3][2] == "X" and field[3][3] == "X":
        print("Победили крестики")
        return True
    elif field[1][1] == "X" and field[2][1] == "X" and field[3][1] == "X":
        print("Победили крестики")
        return True
    elif field[1][2] == "X" and field[2][2] == "X" and field[3][2] == "X":
        print("Победили крестики")
        return True
    elif field[1][3] == "X" and field[2][3] == "X" and field[3][3] == "X":
        print("Победили крестики")
        return True
    elif field[1][1] == "X" and field[2][2] == "X" and field[3][3] == "X":
        print("Победили крестики")
        return True
    elif field[1][3] == "X" and field[2][2] == "X" and field[3][1] == "X":
        print("Победили крестики")
        return True
    elif field[1][1] == "0" and field[1][2] == "0" and field[1][3] == "0":
        print("Победили нолики")
        return True
    elif field[2][1] == "0" and field[2][2] == "0" and field[2][3] == "0":
        print("Победили нолики")
        return True
    elif field[3][1] == "0" and field[3][2] == "0" and field[3][3] == "0":
        print("Победили нолики")
        return True
    elif field[1][1] == "0" and field[2][1] == "0" and field[3][1] == "0":
        print("Победили нолики")
        return True
    elif field[1][2] == "0" and field[2][2] == "0" and field[3][2] == "0":
        print("Победили нолики")
        return True
    elif field[1][3] == "0" and field[2][3] == "0" and field[3][3] == "0":
        print("Победили нолики")
        return True
    elif field[1][1] == "0" and field[2][2] == "0" and field[3][3] == "0":
        print("Победили нолики")
        return True
    elif field[1][3] == "0" and field[2][2] == "0" and field[3][1] == "0":
        print("Победили нолики")
        return True
    else:
        return False

def check_draw():
    if field[1][1]  and field[1][2]  and field[1][3]  and field[2][1]  and field[2][2]  and field[2][3] and field[2][1]  and field[2][2]  and field[2][3]:
        print("Ничья")
        return True

start_game_choice()