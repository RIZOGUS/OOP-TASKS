import csv
import random
from pet import Pet

class VirtualPetSimulator:
    def __init__(self):
        self.__pets = []
        self.__balance = random.randint(10000, 100000)

    def add_pet(self, pet):
        self.__pets.append(pet)

    def save_to_csv(self, pets_file="pets.csv"):
        with open(pets_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["species", "price", "hunger", "happiness", "name"])
            for pet in self.__pets:
                writer.writerow([pet.get_species(), pet.get_price(), pet.get_hunger(), pet.get_happiness(), pet.get_name()])

    def load_from_csv(self, pets_file="pets.csv"):
        try:
            with open(pets_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    species = row["species"]
                    price = float(row["price"])
                    hunger = int(row["hunger"])
                    happiness = int(row["happiness"])
                    name = row["name"]
                    pet = Pet(species, price)
                    pet.set_hunger(hunger)
                    pet.set_happiness(happiness)
                    pet.set_name(name)
                    self.__pets.append(pet)
        except FileNotFoundError:
            pass

    def display_pets(self):
        if not self.__pets:
            return "No pets available"
        result = "Available Pets"
        for pet in self.__pets:
            result += f"{pet.get_species()}  Price: {pet.get_price()} Rupees"
        return result

    def buy_pet(self, species):
        pet = next((p for p in self.__pets if p.get_species().lower() == species.lower()), None)

        if not pet:
            return "Pet not found"

        if self.__balance >= pet.get_price():
            self.__balance -= pet.get_price()
            name = input(f"Enter a name for your new {species}: ")
            pet.set_name(name)
            return f"Successfully bought {species}! Remaining balance: {self.__balance} Rupees\n{pet.set_name(name)}"
        else:
            return "Insufficient balance!"

    def feed_pet(self, species, food):
        pet = next((p for p in self.__pets if p.get_species().lower() == species.lower()), None)
        if pet:
            return pet.feed(food)
        return "Pet not found."

    def play_with_pet(self, species, time):
        pet = next((p for p in self.__pets if p.get_species().lower() == species.lower()), None)
        if pet:
            return pet.play(time)
        return "Pet not found."

    def pet_health(self, species):
        pet = next((p for p in self.__pets if p.get_species().lower() == species.lower()), None)
        if pet:
            return pet.check_health()
        return "Pet not found."

    def get_balance(self):
        return self.__balance

