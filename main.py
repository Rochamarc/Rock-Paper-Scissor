from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from random import choice

class ROCK_PAPER_SCISSOR (App):

	def build (self):
		box = BoxLayout(orientation='vertical')
		button_rock = Button(text='Rock',font_size=30,on_press=self.rock)
		button_paper = Button(text='Paper',font_size=30,on_press=self.paper)
		button_scissor = Button(text='Scissor',font_size=30,on_press=self.scissor)
		self.label_result = Label(text='Rock, Paper and Scissor',font_size=40)
		self.label_type = Label(text='',font_size=40)
		box.add_widget(self.label_result)
		box.add_widget(self.label_type)
		box.add_widget(button_rock)
		box.add_widget(button_paper)
		box.add_widget(button_scissor)
		return box

	def rock(self,button_rock):
		player = 'rock'
		computer_choice = ('rock','paper','scissor')
		computer = choice(computer_choice)
		if computer == player:
			self.label_result.text = ''
			self.label_result.text = 'You Drew'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'paper':
			self.label_result.text = ''
			self.label_result.text = 'You Lost'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'scissor':
			self.label_result.text = ''
			self.label_result.text = 'You Won'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()

	def paper(self,button_paper):
		player = 'paper'
		computer_choice = ('rock','paper','scissor')
		computer = choice(computer_choice)
		if computer == player:
			self.label_result.text = ''
			self.label_result.text = 'You Drew'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'rock':
			self.label_result.text = ''
			self.label_result.text = 'You Won'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'scissor':
			self.label_result.text = ''
			self.label_result.text = 'You Lost'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
	
	def scissor(self,button_scissor):
		player = 'scissor'
		computer_choice = ('rock','paper','scissor')
		computer = choice(computer_choice)
		if computer == player:
			self.label_result.text = ''
			self.label_result.text = 'You Drew'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'rock':
			self.label_result.text = ''
			self.label_result.text = 'You lost'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()
		elif computer == 'paper':
			self.label_result.text = ''
			self.label_result.text = 'You Won'
			self.label_type.text = ''
			self.label_type.text = str('Computer choose %s - You choose %s' %(computer,player)).upper()


ROCK_PAPER_SCISSOR().run() 
