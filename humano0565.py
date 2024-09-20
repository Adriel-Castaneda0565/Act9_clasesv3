print("Act 9 clase humano")
print("Adriel Castañeda mat: 22308051280565")
# Zona de clases
class Humano0565:

    #zona de atributos dentro de la clase
    edad=0
    peso=0
    color_pelo=""
    estatura=0
    genero=""
    ojos=""

    #zona de funciones dentro de la clase
    def caminar0565(self,n):
        print(f"{n} esta caminando uff....")
    def comer0565(self,n):
        print(f"{n} esta comiendo ñam ñam.....")
    def saltar0565(self,n):
        print(f"{n} esta saltando gihuuu....")
    def jugar0565(self,n):
        print(f"{n} esta juegando run run...")

#zona de creacion de objetos
Adriel=Humano0565()
Melany=Humano0565()
#zona de usando objetos
print(" Resultados para Adriel:")
Adriel.edad=16
Adriel.ojos="Cafes"
Adriel.peso=82
Adriel.color_pelo="Negro"
Adriel.estatura=1.75
Adriel.genero="Masculino"
print(f"Edad: {Adriel.edad}")
print(f"Ojos: {Adriel.ojos}")
print(f"Peso: {Adriel.peso}")
print(f"Color de pelo: {Adriel.color_pelo}")
print(f"Estatura: {Adriel.estatura}")
print(f"Genero: {Adriel.genero}")
Adriel.caminar0565("\nAdriel")
Adriel.comer0565("Adriel")
Adriel.saltar0565("Adriel")
Adriel.jugar0565("Adriel")



print(" \nResultados para Melany:")
Melany.edad=17
Melany.ojos="Cafes"
Melany.color_pelo="Negro"
Melany.estatura=1.65
Melany.genero="Femenino"
print(f"Edad: {Melany.edad}")
print(f"Ojos: {Melany.ojos}")
print(f"Color de pelo: {Melany.color_pelo}")
print(f"Estatura: {Melany.estatura}")
print(f"Genero: {Melany.genero}")
Melany.caminar0565("\nMelany")
Melany.comer0565("Melany")
Melany.jugar0565("Melany")