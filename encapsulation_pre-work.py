class Dog:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def bark(self):
        if self.weight > 100:
            print("WOOF")
        else:
            print("woof")


class PetStore:

    def __init__(self, pets):
        if len(pets) > 8:
            raise Exception("Too many dogs!")
        self.pets = pets

    def add_pet(self, pet):
        if type(pet) != Dog:
            raise Exception("Not a dog, only dogs allowed.")
        self.pets.append(pet)

    def pets_for_sale(self):
        for pet in self.pets:
            print(pet.name)


berty = Dog("Berty", 105)
berty.bark()
