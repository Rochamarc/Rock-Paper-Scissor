from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from random import choice

class Interface (BoxLayout):

    pontuacao = '0'

    def Rock (self):

        
        #self.ids.acao.text = 'Funcionou porra'
        player = 'rock'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.acao.text = ''
            self.ids.acao.text = 'You Drew'
            
        
        elif player != computer:
            if computer == 'paper':
                
                self.ids.acao.text = ''
                self.ids.acao.text = 'You lose'

            else:
                self.ids.acao.text = ''
                self.ids.acao.text = "You win"
    
    def Paper (self):

        #self.ids.acao.text = 'Funcionou porra'
        player = 'paper'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.acao.text = ''
            self.ids.acao.text = 'You Drew'

        elif player != computer:
            if computer == 'rock':
                
                self.ids.acao.text = ''
                self.ids.acao.text = 'You win'

            else:
                self.ids.acao.text = ''
                self.ids.acao.text = "You lose"

    def Scissor (self):

        #self.ids.acao.text = 'Funcionou porra'
        player = 'scissor'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.acao.text = ''
            self.ids.acao.text = 'You Drew'

        elif player != computer:
            if computer == 'paper':
                
                self.ids.acao.text = ''
                self.ids.acao.text = 'You Won'

            else:
                self.ids.acao.text = ''
                self.ids.acao.text = "You lose"





class Test (App):
    
    def build (self):

        return Interface()


Test().run()