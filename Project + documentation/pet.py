import random

class Pet:
    def __init__(self, species, price):
        self.__species= species
        self.__price= price
        self.__hunger= 50  
        self.__happiness= 50  
        self.__name= None  
    def feed(self, food):
        self.__hunger= max(0, self.__hunger - food)
        return f"{self.__species} has been fed. Hunger level: {self.__hunger}"

    def play(self, time):
        self.__happiness= min(100, self.__happiness + time)
        return f"{self.__species} is playing. Happiness level {self.__happiness}"

    def check_health(self):
        return f"{self.__species} Hunger {self.__hunger} Happiness {self.__happiness}"

    def set_name(self, name):
        self.__name = name
        return f"Your {self.__species} has been named {self.__name}"

    def get_species(self):
        return self.__species

    def get_price(self):
        return self.__price

    def get_hunger(self):
        return self.__hunger

    def get_happiness(self):
        return self.__happiness

    def get_name(self):
        return self.__name

    def set_hunger(self, hunger):
        self.__hunger = hunger

    def set_happiness(self, happiness):
        self.__happiness = happiness

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return self.__species
