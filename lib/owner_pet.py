# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Ensure we only add Pet instances
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self  # Assign this owner to the pet

    def get_sorted_pets(self):
        # Return owner's pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Start with no owner
        Pet.all.append(self)  # Track all pets

        # Assign owner if provided
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            owner.add_pet(self)
