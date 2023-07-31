from operator import attrgetter

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    all = []


    def __init__(self, name, pet_type, owner = None):
        if pet_type in Pet.PET_TYPES:
            self._name = name
            self.pet_type = pet_type
            self._owner = owner
            Pet.all.append(self)
        else:
            raise Exception("Pet must be in PET_TYPES")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property 
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise Exception("Owner must be an instance of Owner class")

    

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all
        
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
      
        else:
            raise Exception("pet not a Pet instance")
    def get_sorted_pets(self):
        sorted_pet_list = self.pets()
        sorted_pet_list.sort(key = attrgetter('name'))
        return sorted_pet_list
         


    
