
"""

   For Exercise B - Tolos Interview
   __author__: Shiri Rave, 01/04/2021  
   
"""
   


class XOBoard:

	def __init__(self):

 		self.size = 3;
 		self.count = 0;

 		self.board = {'7': ' ' , '8': ' ' , '9': ' ' , '4': ' ' , '5': ' ' , '6': ' ' , '1': ' ' , '2': ' ' , '3': ' ' }

 		self.turn='o'
 		self.next_turn='x'


	def __switch_turn(self):
 	
 		if self.turn == 'x':
 			self.turn='o'
 		else:
   			self.turn='x'

	
	def put(self, id):  
		
   		self.__switch_turn()
   		self.board[id] = self.turn	
   		self.count = self.count+1
   		

	def find_winner(self,key_a,key_b,key_c):
   		theBoard = self.board
   		# If neither X nor O wins and the board is full, we'll declare the result as 'tie'.

   		if theBoard[key_a] == theBoard[key_b] == theBoard[key_c] != ' ': # across the top
   				self.display()              
   				print(" **** Player:" +self.turn + " has won. ****")
   				print("\nGame Over.\n")                  
   				return True
   		else: 
   			return False		

	def status(self):
   		if self.count == 9:               
   			print("It's a Tie!!")
   			print("\nGame Over.\n") 
   			return 'Draw'
   		#	Now we will check if player X or O has won,for every move after 3 moves. 
   		if self.count >= 5:
   			if self.find_winner('7','8','9'): # across the top               
   				return self.turn;
   			elif self.find_winner('4','5','6'): # across the middle
   				return self.turn;
   			elif self.find_winner('1','2','3'): # across the bottom
   				return self.turn;
   			elif self.find_winner('1','4','7'): # down the left side
   				return self.turn;
   			elif self.find_winner('2','5','8'): # down the middle
   				return self.turn;
   			elif self.find_winner('3','6','9'):# down the right side
   				return self.turn;
   			elif self.find_winner('7','5','3'): # diagonal
   				return self.turn;
   			elif self.find_winner('1','5','9'): # diagonal
   				return self.turn;
   		else:
   			return 'None';		

#// ***Display to Web Page **//

	def displayToHTML(self):

		str_board='<p>'
		#str_board=str_board+("\n--Board Status:--\n")
		str_board=str_board+('&nbsp'+self.board['7'] + '&nbsp|' + '&nbsp'+self.board['8'] + '|&nbsp'+ self.board['9']+'&nbsp</br>')
		# str_board.append('-+-+-')
		str_board=str_board+('&nbsp'+self.board['4'] + '&nbsp|&nbsp'+ self.board['5'] + '&nbsp|&nbsp'+ self.board['6']+'&nbsp</br>')
		# str_board.append('-+-+-')
		str_board=str_board+('&nbsp'+self.board['1'] + '|&nbsp'+ self.board['2'] + '&nbsp|&nbsp' + self.board['3']+'&nbsp</br>')
		# str_board.append('-----')
		str_board=str_board+('</p>')
		return str_board
   


#// ***Print to Web Page **//

	def display(self):

		print("\n--Board Status:--\n")
		print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
		print('-+-+-')
		print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
		print('-+-+-')
		print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])
		print('-----')


if __name__ == '__main__':
    xo = XOBoard()
    xo.put('7');
    xo.put('5');
    xo.put('9');
    xo.status();
    xo.display();
    xo.put('1');
    xo.put('8');
    xo.status();


    #### App.py code

from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

xo = XOBoard()
xo.put('7');
xo.put('5');


@app.route('/')
def json():
  return xo.displayToHTML();