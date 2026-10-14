class Player:
    def __init__(self):
        self.name = "Default Mofo" # DEFAULT NAME
        self.age = 24 # DEFAULT AGE
        self.hp = 100 # BASE HP
        self.atk = 10 # BASE ATK

def createMofo():
    newMofo = Player()
    newMofo.name = input("\n Insert Name:")
    print("The mofo named {newMofo.name} is created.")

