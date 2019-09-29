from GameController import GameController


def main():
    print('SUPER FIGHT GAME!')

    gc = GameController()

    warrior = gc.create_warrior()
    opponent = gc.create_opponent()

    print('Your warrior: ', warrior.name)
    print('Opponent: ', opponent.name)

    win = gc.fight(warrior, opponent)

    if win:
        print('YOU WINNER!!!')
    else:
        print('GAME OVER.')


if __name__ == '__main__':
    main()
