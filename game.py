from random import shuffle
import sys

# created some time in 2015
class door_game:

	games_played, games_won, choice, doors = 0, 0, '1', {}


	def __init__(self):
		self.start_game()


	def start_game(self):
		random_door = [1, 0, 0]
		shuffle(random_door)
		self.doors = {'1': random_door[0], '2': random_door[1], '3': random_door[2]}
		
		self.give_door_choice()
		
		self.remove_losing_door(1)

		self.give_change_choice()

		self.show_results()

		self.play_again()


	def give_door_choice(self):
		self.choice = raw_input("Please choose a door[1, 2, 3]: ")
		#choice = int(choice)
		if self.choice not in self.doors:
			print ' --- Door number ' + self.choice + ' does not exist.'
			sys.exit()

		print ' --- You chose door number', self.choice


	def remove_losing_door(self, remove):
		remove = str(remove)
		if self.choice != remove and self.doors[remove] == 0:
			print ' --- Removing a losing door.'
			del self.doors[remove]
		else:
			remove = int(remove)
			remove += 1
			self.remove_losing_door(remove)
			return

		print ' --- Removed door number', remove


	def give_change_choice(self):
		change = raw_input("Would you like to choose a different door? [y, n]: ")

		if change not in ['y', 'n']:
			print ' --- Try again.'
			sys.exit()

		if change == 'y':
			print ' --- You chose a different door.'
			del self.doors[self.choice]


	def show_results(self):
		key, value = self.doors.popitem()
		if value == 1:
			print ' --- You won! :)'
			self.games_won += 1
		else:
			print ' --- You lost! :('

		self.games_played += 1
		print ' --- Games played:' + str(self.games_played) + '. Games won: ' + str(self.games_won)


	def play_again(self):
		try_again = raw_input("Play again? [y, n]: ")

		if try_again == 'y':
			self.start_game()
		else:
			print ' --- Bye!'


door_game()