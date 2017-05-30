# Game
# has: players, unused deck cards, unused cards in hand, discarded cards, used cards, rounds

# Players
# has: kept cards, hand, points

# Cards
# has: symbol(Palace/crown, Library/scroll, Garden/leaves, Temple/hand, Stronghold/castle, None), Ability

# Ability:
# is: majority, each, set, win ties, double most numerous, majority in suits with one card, score highest with single card, each suit don't have

import random

card1 = {"name":"Kings Nest", "symbol":"Palace", "text":"Win all ties", "each":False, "majority":False, "affected_symbol":None}
card2 = {"name":"Ancient Divide", "symbol":"Palace", "text":"For majority in Stronghold gain 7", "each":False, "majority":True, "affected_symbol":"Stronghold"}
card3 = {"name":"Eternal Palace", "symbol":"Palace", "text":"For each Library gain 3", "each":True, "majority":False, "affected_symbol":"Library"}
card4 = {"name":"The Great Library of Ahm", "symbol":"Library", "text":"For majority in Temple gain 7", "each":False, "majority":True, "affected_symbol":"Temple"}
card5 = {"name":"The Mana Well", "symbol":"Library", "text":"For each set of Palace, Stronghold, and Temple gain 9", "each":False, "majority":False, "affected_symbol":None}
card6 = {"name":"The Citadels of the Prophets", "symbol":"Library", "text":"For each Garden gain 3", "each":True, "majority":False, "affected_symbol":"Garden"}
card7 = {"name":"Golden Ziggurat", "symbol":"Garden", "text":"For majority in Palace gain 7", "each":False, "majority":True, "affected_symbol":"Palace"}
card8 = {"name":"Gods Baths", "symbol":"Garden", "text":"For each Stronghold gain 3", "each":True, "majority":False, "affected_symbol":"Stronghold"}
card9 = {"name":"The Maze of the Damned", "symbol":"Garden", "text":"For a set of Palace, Stronghold, Garden, Library, and Temple gain 13", "each":False, "majority":False, "affected_symbol":None}
card10 = {"name":"The Eye of the North", "symbol":"Stronghold", "text":"For each suit you don't have gain 3", "each":False, "majority":False, "affected_symbol":None}
card11 = {"name":"The Jinn Shackles", "symbol":"Stronghold", "text":"For each Temple gain 3", "each":True, "majority":False, "affected_symbol":"Temple"}
card12 = {"name":"Old Man's Pass", "symbol":"Stronghold", "text":"For majority in Library gain 7", "each":False, "majority":True, "affected_symbol":"Library"}
card13 = {"name":"Blood-tear Spring", "symbol":"Temple", "text":"For majority in Garden gain 7", "each":False, "majority":True, "affected_symbol":"Garden"}
card14 = {"name":"The Sky Pillars", "symbol":"Temple", "text":"For each set of Library and Garden gain 5", "each":False, "majority":False, "affected_symbol":None}
card15 = {"name":"The Vestibule", "symbol":"Temple", "text":"For each Palace gain 3", "each":True, "majority":False, "affected_symbol":"Palace"}
card16 = {"name":"The Molehill", "symbol":None, "text":"For majority in suits with only one card gain 8", "each":False, "majority":False, "affected_symbol":None}
card17 = {"name":"The Roof of the World", "symbol":None, "text":"Double the amount of your most numberous suits", "each":False, "majority":False, "affected_symbol":None}
card18 = {"name":"The Sapphire Port", "symbol":None, "text":"For scoring the highest with a single card gain 8", "each":False, "majority":False, "affected_symbol":None}


CardList = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18]
CardSymbols = ["Palace", "Library", "Garden", "Temple", "Stronghold"]


def BalanceCheck(CardList):
	issue = False
	print "Total Number of Cards: " + str(len(CardList))
	print "Total Number of Symbols: " + str(len(CardSymbols))

	for card in CardList:
		if card["symbol"] not in CardSymbols and card["symbol"] is not None:
			print "Card with weird symbol: " + card["name"]
			issue = True
	print "Checked symbols"

	for card in CardList:
		if card["affected_symbol"] not in CardSymbols and card["affected_symbol"] is not None:
			print "Card with weird affected_symbol: " + card["name"]	
			issue = True
	print "Checked affected_symbols"

	eachCount = 0
	for card in CardList:
		if card["each"] == True:
			eachCount += 1
	print str(eachCount) + " cards with an \"each\" ability"
	if eachCount != len(CardSymbols):
		issue = True
		print "Each abilities doesn't match the number of card symbols"

	majorityCount = 0
	for card in CardList:
		if card["majority"] == True:
			majorityCount += 1
	print str(majorityCount) + " cards with an \"majority\" ability"
	if majorityCount != len(CardSymbols):
		issue = True
		print "majority abilities doesn't match the number of card symbols"		

	if issue == True:
		print "There was at least one issue detected in the Balance Check"
	else:
		print "No issues found in the Balance Check"

# BalanceCheck(CardList)

# Takes in list of cards and a description to print list.
def print_card_list(card_list, description):
	print "\nPrinting: " + description
	if len(card_list) == 0:
		print "This list is empty. Sorry."
	else:
		for card_num in range(0, len(card_list)):
			print str(card_num + 1) + ": " + card_list[card_num].to_string()

rounds = 3
exchanges = 5

class Card(object):
	def __init__(self, name, symbol, text, each, majority, affected_symbol):
		self.name = name
		self.symbol = symbol
		self.text = text
		self.each = each
		self.majority = majority
		self.affected_symbol = affected_symbol

	def get_name(self):
		return self.name

	def get_symbol(self):
		return self.symbol

	def get_text(self):
		return self.text

	def get_each(self):
		return self.each

	def get_majority(self):
		return self.majority

	def get_affected_symbol(self):
		return self.affected_symbol

	def to_string(self):
		return self.name + " | " + str(self.symbol) + " | " + self.text

class Player(object):
	def __init__(self, number):
		self.number = number
		self.points = 0
		self.hand = []
		self.played_cards = []
		self.kept_cards = []
		self.win_ties = False
		self.highest_card_score = 0

	def get_number(self):
		return self.number

	# Drawing cards/getting hand
	def new_cards(self, cards):
		self.hand = cards

	def get_hand(self):
		return self.hand

	def print_hand(self):
		print_card_list(self.hand, "Player " + str(self.number) + " hand")

	# Playing cards/getting played cards
	def play_card(self):
		return self.choose_card("play", self.hand, self.played_cards)

	def get_played_cards(self):
		return self.played_cards

	def print_played_cards(self):
		print_card_list(self.played_cards, "Player " + str(self.number) + " played cards")

	def reset_played_cards(self):
		self.played_cards = []

	# Keeping card/getting kept cards
	def keep_card(self):
		return self.choose_card("keep", self.played_cards, self.kept_cards)

	def get_kept_cards(self):
		return self.kept_cards

	def print_kept_cards(self):
		print_card_list(self.kept_cards, "Player " + str(self.number) + " kept cards")

	# Choose a card to discard
	def discard_card(self):
		return self.choose_card("discard", self.played_cards, None)
		
	# Adding points at end of round/getting points
	def add_points(self, points):
		self.points += points

	def get_points(self):
		return self.points

	# Choose a card from one list and add to another
	def choose_card(self, action, chosen_from, inserted_into):
		print "\nNow, player " + str(self.number) + " will " + action + " a card."
		print "Which card would you like to " + action + "?"

		# Length Check
		if len(chosen_from) <= 0:
			print "Nothing to choose from this list!"
			return

		for card_num in range(0, len(chosen_from)):
			print str(card_num + 1) + ": " + chosen_from[card_num].to_string()
		
		card_num_chosen = input("Type number of the card you'd like to discard.")
		while card_num_chosen < 1 or card_num_chosen > len(chosen_from):
			card_num_chosen = input("The valid numbers are in the list above. Please type number of the card you'd like to discard.")

		card_num_chosen -= 1
		print "You chose " + chosen_from[card_num_chosen].to_string()
		chosen_card = chosen_from[card_num_chosen]
		chosen_from.remove(chosen_card)
		if inserted_into != None:
			inserted_into.append(chosen_card)
		return chosen_card


class Game(object):
	def __init__(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		self.deck = []
		for card in CardList:
			new_card = Card(card["name"], card["symbol"], card["text"], card["each"], card["majority"], card["affected_symbol"])
			self.deck.append(new_card)
		self.discarded_cards = []
		self.round = 1

	def start_round(self):
		print "Welcome to Round " + str(self.round) + "!"
		print "Now, you'll draw cards:"

		# Player will draw cards to add to current hand
		player1_cards = [] + self.player1.get_played_cards()
		player2_cards = [] + self.player2.get_played_cards()
		self.player1.reset_played_cards()
		self.player2.reset_played_cards()
		
		number_to_draw = 5
		if self.round > 1:
			number_to_draw = 2
		# Alternate drawing cards
		for draw in range(0, number_to_draw):
			card_to_draw = random.choice(self.deck)
			player1_cards.append(card_to_draw)
			self.deck.remove(card_to_draw)

			card_to_draw = random.choice(self.deck)
			player2_cards.append(card_to_draw)
			self.deck.remove(card_to_draw)

		# Set drawn cards + old used cards
		self.player1.new_cards(player1_cards)
		self.player2.new_cards(player2_cards)

	def play_round(self):
		for exchange in range(0, exchanges):
			self.player1.play_card()
			self.player2.play_card()

			# Exchange occurs
			player1_hand = game.player1.get_hand()
			player2_hand = game.player2.get_hand()
			self.player1.new_cards(player2_hand)
			self.player2.new_cards(player1_hand)

	def end_round(self):
		self.tally_points()

		if round != 3:
			self.player1.keep_card()
			self.player2.keep_card()

			self.discarded_cards.append(game.player1.discard_card())
			self.discarded_cards.append(game.player2.discard_card())

		self.round += 1

	def tally_points(player):
		player1_played_cards = self.player1.get_played_cards() + self.player1.get_kept_cards()
		player2_played_cards = self.player2.get_played_cards() + self.player2.get_kept_cards()
		print "Player 1 has these cards: "
		for card in player1_played_cards:
			print card.to_string()
		print ""
		print "Player 2 has these cards: "
		for card in player2_played_cards:
			print card.to_string()

		player1_symbols = {"Palace": 0, "Library": 0, "Garden": 0, "Temple": 0, "Stronghold": 0}
		player2_symbols = {"Palace": 0, "Library": 0, "Garden": 0, "Temple": 0, "Stronghold": 0}

		player1_wins_ties = False
		player2_wins_ties = False

		doubling = False
		for card in player1_played_cards:
			if card.get_name() == "Kings Nest":
				player1_wins_ties = True

			card_symbol = card.get_symbol()
			if card_symbol is not None:
				player1_symbols[card_symbol] += 1
			elif card.get_name() == "The Roof of the World":
				pass
				doubling = True # comment here ignores all doubling

		if doubling == True:
			most_numerous_symbols = []
			current_high = 0
			for symbol in player1_symbols:
				if player1_symbols[symbol] > current_high:
					most_numerous_symbols = []
					most_numerous_symbols.append(symbol)
				if player1_symbols[symbol] == current_high:
					most_numerous_symbols.append(symbol)
			for double_symbol in most_numerous_symbols:
				player1_symbols[double_symbol] = player1_symbols[double_symbol] * 2	


		doubling = False
		for card in player2_played_cards:
			if card.get_name() == "Kings Nest":
				player2_wins_ties = True

			card_symbol = card.get_symbol()
			if card_symbol is not None:
				player2_symbols[card_symbol] += 1
			elif card.get_name() == "The Roof of the World":
				pass
				doubling = True # comment here ignores all doubling

		if doubling == True:
			most_numerous_symbols = []
			current_high = 0
			for symbol in player2_symbols:
				if player2_symbols[symbol] > current_high:
					most_numerous_symbols = []
					most_numerous_symbols.append(symbol)
				if player2_symbols[symbol] == current_high:
					most_numerous_symbols.append(symbol)
			for double_symbol in most_numerous_symbols:
				player2_symbols[double_symbol] = player2_symbols[double_symbol] * 2	
		doubling = False

		print "Done with calculating the symbols"
		print "Player 1 Symbols: " + str(player1_symbols)
		print "Player 2 Symbols: " + str(player2_symbols)



		player1_score = 0
		
		for card in player1_played_cards:
			if card.each == True:
				affected_symbol = card.affected_symbol
				if affected_symbol == None:
					print "Found a card with each ability that has no affected symbol?!"
				else:
					player1_count = player1_symbols[affected_symbol]
					player1_score += 3 * player1_count
					print "player1 scores " + str(3 * player1_count) + " for " + card.get_name()

			elif card.majority == True:
				affected_symbol = card.affected_symbol
				if affected_symbol == None:
					print "Found a card with majority ability that has no affected symbol?!"
				else:
					player1_count = player1_symbols[affected_symbol]
					player2_count = player2_symbols[affected_symbol]
					if player1_count > player2_count:
						player1_score += 7
						print "player1 scores " + str(7) + " for " + card.get_name()
					elif player1_count == player2_count and player1_wins_ties == True:
						player1_score += 7
						print "player1 scores " + str(7) + " for " + card.get_name()
					else:
						print "Failed to score any points for " + card.get_name()									

			else:
				print "choose not to account for " + card.get_name() + " yet"
			print "Current player1 score " + str(player1_score)





		player2_score = 0


		print "Player 1 score: " + str(player1_score)
		print "Player 2 score: " + str(player2_score)


	def get_deck(self):
		return self.deck

	def print_deck(self):
		print_card_list(self.deck, "deck")


game = Game()

for round in range(0, rounds):
	game.start_round()
	game.play_round()
	game.end_round()


# Plays cards for number of exchanges









