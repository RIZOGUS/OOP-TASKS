from simulator import VirtualPetSimulator
from pet import Pet
import random

simulator = VirtualPetSimulator()
simulator.load_from_csv()

pet_species = ["Dog", "Cat", "Parrot", "Snake", "Raccoon", "Goat", "Camel", "Pigeon", "Rabbit", "Horse"]
for species in pet_species:
    price = random.randint(1000, 5000)
    pet = Pet(species, price)
    simulator.add_pet(pet)

while True:
    print("--- Menu ---")
    print("1. Available Pets")
    print("2. Buy Pet")
    print("3. Feed Pet")
    print("4. Pet Health")
    print("5. Play with Pet")
    print("6. Save and Exit")
    print(f"Current Balance: {simulator.get_balance()} Rupees")

    choice = input("Choose an option: ")

    if choice == "1":
        print(simulator.display_pets())

    elif choice == "2":
        species = input("Enter the species name of the pet you want to buy: ")
        print(simulator.buy_pet(species))

    elif choice == "3":
        species = input("Enter the species name of the pet you want to feed: ")
        food = int(input("Enter food amount: "))
        print(simulator.feed_pet(species, food))

    elif choice == "4":
        species = input("Enter the species name of the pet to check health: ")
        print(simulator.pet_health(species))

    elif choice == "5":
        species = input("Enter the species name of the pet to play with: ")
        time = int(input("Enter playtime in minutes: "))
        print(simulator.play_with_pet(species, time))

    elif choice == "6":
        simulator.save_to_csv()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
