class Pet:
    def __init__(self, name):
        self.__name = name
        self.__hunger = 5
        self.__energy = 5

    # Method to feed the pet
    def feed(self):
        if self.__hunger > 0:
            self.__hunger -= 1
        else:
            print(f"{self.__name} is not hungry!")

    # Method to play with the pet
    def play(self):
        if self.__energy > 0:
            self.__energy -= 1
            self.__hunger += 1
        else:
            print(f"{self.__name} is too tired to play!")

    # Method to let the pet rest
    def rest(self):
        if self.__energy < 10:
            self.__energy += 2
            if self.__energy > 10:
                self.__energy = 10
        else:
            print(f"{self.__name} is fully rested!")

    # Method to display the pet's current status
    def status(self):
        print(f"Pet Name: {self.__name}")
        print(f"Hunger Level: {self.__hunger}")
        print(f"Energy Level: {self.__energy}")

# Create a new pet instance
my_pet = Pet("chunchunmaru")

# Initial status
print("Initial Status:")
my_pet.status()

# Feed the pet
print("\nAfter feeding:")
my_pet.feed()
my_pet.status()

# Play with the pet
print("\nAfter playing:")
my_pet.play()
my_pet.status()

# Rest the pet
print("\nAfter resting:")
my_pet.rest()
my_pet.status()
