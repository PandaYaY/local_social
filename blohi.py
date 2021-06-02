def game():
    import os
    from random import randint

    print('Сделайте ставку, выбрав одну из 8 блох')
    bet = int(input('Номер блохи: '))

    blohi = [0, 0, 0, 0, 0, 0, 0, 0]
    max = -1
    line = '|' + '*' * 78 + '|'

    while True:
        os.system('cls')
        print(line)
        print(f'|{"Блошиные бега!": ^78}|')
        print(line)

        for i in range(8):
            if max < blohi[i]:
                max = blohi[i]
                num = i+1

            print(f'|{i+1}.'+' '*(blohi[i]-1)+'>'+' '*(76-blohi[i])+'|')
        print(line)

        if max == 76:
            break

        for i in range(8):
            step = randint(0, 2)
            blohi[i] += step
            if blohi[i] > 76:
                blohi[i] = 76

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

# print(game())
