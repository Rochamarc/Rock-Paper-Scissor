from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from random import choice

player_points = 0
pc_points = 0

class Interface (BoxLayout):

    
    def Rock (self):

        global player_points
        global pc_points

        player = 'rock'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'
            
        
        elif player != computer:
            if computer == 'paper':
                
                self.ids.action.text = ''
                self.ids.action.text = 'You lose'
                pc_points += 1

            else:
                
                self.ids.action.text = ''
                self.ids.action.text = "You win"
                player_points += 1

    def Paper (self):

        global player_points
        global pc_points

        player = 'paper'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'

        elif player != computer:
            if computer == 'rock':
                
                self.ids.action.text = ''
                self.ids.action.text = 'You Win'
                player_points += 1

            else:
                
                self.ids.action.text = ''
                self.ids.action.text = "You Lose"
                pc_points += 1

    def Scissor (self):

        global player_points
        global pc_points

        player = 'scissor'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'

        elif player != computer:
            if computer == 'paper':
                
                self.ids.action.text = ''
                self.ids.action.text = 'You Win'
                player_points += 1

            else:
                
                self.ids.action.text = ''
                self.ids.action.text = "You Lose"
                pc_points += 1
    
    def Points (self):

        global player_points
        global pc_points

        player_points_2 = str(player_points)
        pc_points_2 = str(pc_points)

        self.ids.lbl_points.text = "Your points: %s | Pc points: %s" %(player_points,pc_points) 




class Test (App):
    
    def build (self):

        return Interface()


Test().run()