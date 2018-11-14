from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from random import choice
from time import sleep

player_points = 0
pc_points = 0
match = 1

class Interface (BoxLayout):

    def Wait (self):

        sleep(0.2)
    
    def Rock (self):

        global player_points
        global pc_points
        global match
        match += 1

        player = 'rock'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.Wait()
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'
            
        
        elif player != computer:
            if computer == 'paper':
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = 'You Lose'
                pc_points += 1

            else:
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = "You Win"
                player_points += 1

    def Paper (self):

        global player_points
        global pc_points
        global match
        match += 1

        player = 'paper'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.Wait()
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'

        elif player != computer:
            if computer == 'rock':
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = 'You Win'
                player_points += 1

            else:
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = "You Lose"
                pc_points += 1

    def Scissor (self):

        global player_points
        global pc_points
        global match 
        match  += 1

        player = 'scissor'
        computer_choice = ('rock','paper','scissor')
        computer = choice(computer_choice)
        if player == computer:
            
            self.Wait()
            self.ids.action.text = ''
            self.ids.action.text = 'You Drew'

        elif player != computer:
            if computer == 'paper':
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = 'You Win'
                player_points += 1

            else:
                
                self.Wait()
                self.ids.action.text = ''
                self.ids.action.text = "You Lose"
                pc_points += 1
    
    def Points (self):

        global player_points
        global pc_points
        global match

        self.ids.lbl_points.text = "Match: %s | Your points: %s | Pc points: %s" %(match,player_points,pc_points) 




class Test (App):
    
    def build (self):

        return Interface()


Test().run()