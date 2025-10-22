from dataclasses import dataclass

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

@dataclass
class PersonaDto:
    nombre : str
    edad: int 
    cat : str

person = PersonaDto("Ilse", 25, "Trainee")     

print(person)
        