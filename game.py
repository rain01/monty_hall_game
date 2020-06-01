import sys
from random import shuffle


def main(argv):
    door_game = DoorGame()

    # play n fast games
    if len(argv) > 0:
        how_many = int(argv[0])
        choice = argv[1] if len(argv) > 1 else 1
        change = int(argv[2]) if len(argv) > 2 else True

        for i in range(how_many):
            door_game.fast_game(choice, change)

        # show results
        door_game.show_final_results()
    else:
        # start regular game
        door_game.start_game()


class DoorGame:
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.choice = '1'
        self.doors = {}

    def start_game(self):
        self.init_doors()

        try:
            self.give_door_choice()

            self.remove_losing_door()

            self.give_change_choice()

            self.show_results()
        except ValueError as e:
            print(e)

        self.play_again()

    def init_doors(self):
        random_door = [1, 0, 0]
        shuffle(random_door)
        self.doors = {
            '1': random_door[0],
            '2': random_door[1],
            '3': random_door[2]
        }

    def give_door_choice(self):
        self.choice = input('Please choose a door[1, 2, 3]: ')

        if self.choice not in self.doors:
            raise ValueError(f' --- Door number {self.choice} does not exist.')

        print(' --- You chose door number', self.choice)

    def remove_losing_door(self, remove='1'):
        # make sure not to remove selected door and not the price door
        if self.choice != remove and self.doors[remove] == 0:
            del self.doors[remove]
        else:
            # otherwise try the next door
            remove = int(remove)
            remove += 1
            self.remove_losing_door(str(remove))
            return

        print(' --- Removed losing door number', remove, end='')

    def give_change_choice(self):
        change = input('\nWould you like to choose a different door? [Y/n]: ').strip() or 'y'

        while change.lower() not in ['y', 'n']:
            change = input(' --- Incorrect input. Try again...[Y/n]: ').strip() or 'y'

        if change.lower() == 'y':
            print(' --- You chose a different door.')

            # remove first choice
            del self.doors[self.choice]
            self.choice = None

    def get_results(self):
        # if selection wasn't changed
        if self.choice:
            value = self.doors[self.choice]
        else:
            # if selection was changed, select the last leftover selection
            key, value = self.doors.popitem()

        if value == 1:
            self.games_won += 1

        return value

    def show_results(self):
        value = self.get_results()

        if value == 1:
            print(' --- You won! :)')
        else:
            print(' --- You lost :(')

        self.games_played += 1

        self.show_final_results()

    def show_final_results(self):
        print(f' --- Games played: {self.games_played}. Games won: {self.games_won}')

    def play_again(self):
        try_again = input('Play again? [Y/n]: ').strip() or 'y'

        if try_again.lower() == 'y':
            self.start_game()
        else:
            print(' --- Bye!')

    def fast_game(self, choice, change=True):
        self.init_doors()

        self.choice = str(choice)

        self.remove_losing_door()

        if change:
            del self.doors[self.choice]
            self.choice = None

        value = self.get_results()

        print(' WON!' if value else '')

        self.games_played += 1


if __name__ == '__main__':
    main(sys.argv[1:])
