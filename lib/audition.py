class Audition: #the actor/actress trying out for the character

    all_auditions = []

    def __init__(self, role, actor, location, phone):
        self.actor = actor
        self.location = location
        self.phone = phone
        self._hired = False
        self._role = role

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, actor):
        if  type(actor) == str and ((len(actor) > 3) and (len(actor) < 20)):
            self._actor = actor
        else:
            raise Exception("Actor must be a string greater than 0 characters and less than 20 characters")
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, role):
        from role import Role
        if isinstance(role, Role):
            self._role = role
            Audition.all_auditions.append(self)
        else:
            raise Exception("Role must be an instance of Role")
        
    def call_back(self):
        self._hired = True
    pass


print 