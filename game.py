from random import shuffle
import sys


def main():
    door_game = DoorGame()
    door_game.start_game()


class DoorGame:
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.choice = '1'
        self.doors = {}

    def start_game(self):
        random_door = [1, 0, 0]
        shuffle(random_door)
        self.doors = {
            '1': random_door[0],
            '2': random_door[1],
            '3': random_door[2]
        }
        
        self.give_door_choice()
        
        self.remove_losing_door()

        self.give_change_choice()

        self.show_results()

        self.play_again()

    def give_door_choice(self):
        self.choice = input('Please choose a door[1, 2, 3]: ')

        if self.choice not in self.doors:
            print(f' --- Door number {self.choice} does not exist.')
            sys.exit()

        print(' --- You chose door number', self.choice)

    def remove_losing_door(self, remove='1'):
        # make sure not to remove selected door and not the price door
        if self.choice != remove and self.doors[remove] == 0:
            print(' --- Removing a losing door.')
            del self.doors[remove]
        else:
            # otherwise try the next door
            remove = int(remove)
            remove += 1
            self.remove_losing_door(str(remove))
            return

        print(' --- Removed door number', remove)

    def give_change_choice(self):
        change = input('Would you like to choose a different door? [Y/n]: ').strip() or 'y'

        while change.lower() not in ['y', 'n']:
            change = input(' --- Incorrect input. Try again...[Y/n]: ').strip() or 'y'

        if change.lower() == 'y':
            print(' --- You chose a different door.')
            del self.doors[self.choice]
            self.choice = None

    def show_results(self):
        # if selection wasn't changed
        if self.choice:
            value = self.doors[self.choice]
        else:
            # if selection was changed, select the last leftover selection
            key, value = self.doors.popitem()

        if value == 1:
            print(' --- You won! :)')
            self.games_won += 1
        else:
            print(' --- You lost! :(')

        self.games_played += 1
        print(f' --- Games played: {self.games_played}. Games won: {self.games_won}')

    def play_again(self):
        try_again = input('Play again? [Y/n]: ').strip() or 'y'

        if try_again.lower() == 'y':
            self.start_game()
        else:
            print(' --- Bye!')


if __name__ == '__main__':
    main()
