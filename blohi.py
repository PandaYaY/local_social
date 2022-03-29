import os
from random import randint
from time import sleep


def game():
    num = 0
    max_step = -1
    blohi = [0, 0, 0, 0, 0, 0, 0, 0]
    line = '|' + '*' * 78 + '|'

    bet = int(input('Сделайте ставку, выбрав одну из 8 блох\nНомер блохи: '))

    while True:
        os.system('cls')
        print(f'{line}\n|{"Блошиные бега!": ^78}|\n{line}')

        for i in range(8):
            if max_step < blohi[i]:
                max_step = blohi[i]
                num = i+1

            print(f'|{i+1}.'+' '*(blohi[i]-1)+'>'+' '*(76-blohi[i])+'|')
        print(line)

        if max_step == 76:
            break

        for i in range(8):
            step = randint(0, 2)
            blohi[i] += step
            if blohi[i] > 76:
                blohi[i] = 76
        sleep(0.25)

    winner = f'Победитель под номером {num}!'
    print(f'|{winner: ^78}|')
    print(line)

    if num == bet:
        print('Ставка зашла')
        bet = 1
    else:
        print('Ставка не зашла')
        bet = 0

    return bet


if __name__ == "__main__":
    game()
