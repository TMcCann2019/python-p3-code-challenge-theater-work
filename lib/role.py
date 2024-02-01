from audition import Audition

class Role: #the character in the play

    all_roles = []

    def __init__(self, character_name):
        self.character_name = character_name
        
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, character_name):
        if  type(character_name) == str and (len(character_name) > 0):
            self._character_name = character_name
            Role.all_roles.append(self)
        else:
            raise Exception("Character name must be a string greater than 0 characters")
        
    def auditions(self):
        return Audition.all_auditions
    pass

ceclia = Role("Juliet")

print(ceclia.character_name)
print(Role.all_roles[0])

print(ceclia.auditions())