import random

class Game:
    
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        self.name = name
        self.fund = 0
        self.round = 1
        self.user = int(input('Welcome to the game choose a number: '))
        self.comp = random.randint(4, 10)
        self.quit = False
        
               
        
    def deposit(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        amount = float(input(f'Hi {self.name}, how much do you want to deposit'))
        
        if amount > 10:
            self.fund += amount
            
        else:
            return f'oops {self.name}, Minimum deposit is $10'
        
        return f'You now have {self.fund}'
    
    def play(self):
        
        """_summary_
        """
        while True:
            print('do you want to continue the game')
            choice = input()
            if choice.lower == 'no':
                self.quit = True
            
            if self.quit == True:
                print(f'Thanks for playing you left with {self.fund}')
                break
            else:
                if self.fund <= 0:
                    print(f'Not enough funds, you have ${self.fund}')
                    break
                else:
                    print('ROUND {self.round}')
                    print(f'after round one original panadol extra..')
                    user_num = int(input())
                    comp_num = random.randint(1,comp)

                    if user_num + comp_num == self.user:
                        self.fund += amount * 0.25
                        print(f'You won {self.fund * 0.25}')
                        self.round += 1
                    elif user_num + comp_num  == self.comp:
                        self.fund -= amount * 0.25
                        print(f'You lost {self.fund * 0.25}')
                        self.round += 1
                    else:
                        print('It is a tie')
                        self.round += 1
                
    
        
    
        
        
        
        
        
        
        