class Valo():
    def __init__(self,agents,hours,winrate):
        #what we are doing using __init__(self) is we are creating our own ATTRIBUTES like re.findall which is an inbuilt attribute
        self.agents = agents
        self.hours = hours
        self.winrate = winrate
my_valoagents=Valo(agents="Omen",hours=300,winrate=45)
my_valoagents.agents


#%%
class Valo():
    # fav='Omen' is a CLASS OBJECT ATTRIBUTE as it does not fall under any instance like agent or hours, this remains constant no matter what value u assign to others and we dont use self. for assigning the class object attribute as it is going to be same throughout the class.
    fav='Omen'
    def __init__(self,agents,hours,winrate):
        self.agents = agents
        self.hours = hours
        self.winrate = winrate
my_valoagents=Valo(agents="Omen",hours=300,winrate=45)
my_valoagents.fav
#%%
class Valo():
    #MY CLASS OBJECT ATTRIBUTE
    fav='Omen'


    #MY INSTANCE ATTRIBUTES
    def __init__(self,agents,hours,winrate):
        self.agents = agents
        self.hours = hours
        self.winrate = winrate

    #MY CLASS METHODS--> WHICH BASICALLY MEANS FUNCTION UNDER A CLASS WHERE U CAN ASSIGN A FUNCTION AND IT CAN TAKE INSTANCE ATTRIBUTES AS INPUT.
    def Headshot(self,number='enter the number'):
       print('your headshot percentage for {}'.format(self.agents,number='enter the number'))

       #MY OBJECT CALL NAME
       my_valoagents=Valo(agents="Omen",hours=300,winrate=45)

       my_valoagents.Headshot()




#%%
class Valo():
    #MY CLASS OBJECT ATTRIBUTE
    fav='Omen'


    #MY INSTANCE ATTRIBUTES
    def __init__(self,agents,hours,winrate):
        self.agents = agents
        self.hours = hours
        self.winrate = winrate

    #MY CLASS METHODS--> WHICH BASICALLY MEANS FUNCTION UNDER A CLASS WHERE U CAN ASSIGN A FUNCTION AND IT CAN TAKE INSTANCE ATTRIBUTES AS INPUT.
    def Headshot(self,number='enter the number'):
        number=input('Enter your headshot')
        print('your headshot percentage for {} is {}'.format(self.agents,number))

       #MY OBJECT CALL NAME
my_valoagents=Valo(agents="Omen",hours=300,winrate=45)

my_valoagents.Headshot()