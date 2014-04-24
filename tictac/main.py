#! /usr/bin/env python

import sys

class TicTac:
	""" my tic tac game """

	board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
	
	def Intro(self):
		print 'Welcome to my TicTacGame!'

	def Board(self):
		print '%s  %s  %s' % (self.board[6], self.board[7], self.board[8])
		print '%s  %s  %s' % (self.board[3], self.board[4], self.board[5])
		print '%s  %s  %s' % (self.board[0], self.board[1], self.board[2])
		print ' '

	def Update(self, move, value):
		self.board[move - 1] = value

	def Winner(self, value):
		if self.board[0] == self.board[1] and self.board[1] == self.board[2] or \
		   self.board[3] == self.board[4] and self.board[4] == self.board[5] or \
		   self.board[6] == self.board[7] and self.board[7] == self.board[8] or \
		   self.board[0] == self.board[3] and self.board[3] == self.board[6] or \
		   self.board[3] == self.board[4] and self.board[4] == self.board[5] or \
		   self.board[6] == self.board[7] and self.board[7] == self.board[8] or \
		   self.board[6] == self.board[4] and self.board[4] == self.board[2] or \
		   self.board[0] == self.board[4] and self.board[4] == self.board[8]: 
			print 'Winner %s ' % value
			self.Board()
			sys.exit(0)



def main():
	game = TicTac()
	game.Intro()
	game.Board()
	for i in xrange(1, 10):
		if i % 2 == 0:
			X = input('Enter move location for player X ')
			game.Update(X, 'X')
			game.Winner('X')
		elif i % 2 == 1:
			O = input('Enter move location for player 0 ')
			game.Update(O, 'O')
			game.Winner('O')
		game.Board()
	print 'Draw!'

if __name__ == "__main__":
	main()