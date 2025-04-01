# FAÇA UMA CLASSE PARA REPRESENTAR UM CACHORRO COM OS ATRIBUTOS:
# nome, raca, peso, pedigree, cor, idade
# E OS MÉTODOS:
# comer(comida)
# brincar(brincadeira)
# dormir()
# acordar()

# INSTANCIE 2 CACHORROS E TESTE OS MÉTODOS.






class Cachorro:
    def __init__(self, nome:str, raca:str, peso: float, pedigree:bool, cor:str, idade:int):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.pedigree = pedigree
        self.cor = cor
        self.idade = idade
        
    def comer(self, comida:str):
        return f"O doguinho {self.nome} está comendo {comida}"
    
    def brincar(self, brincadeira:str):
        return f"O doguinho {self.nome} está brincando de {brincadeira}"

    def dormir(self):
        return f"O doguinho {self.nome} dormiu"
    
    def acordar(self):
        return f"O doguinho {self.nome} acordou"
    

cachorrim1 = Cachorro(nome="Spike", raca="Pitbull", peso=13.5, pedigree=True, cor="Branco", idade=4)

outro_cachorro = Cachorro(nome="Fifi", raca="Vira-Lata", peso=4.8, pedigree=False, cor="Caramelo", idade=6)


print(cachorrim1.acordar())
print(cachorrim1.brincar(brincadeira="Pegar Bolinha"))
print(cachorrim1.comer(comida="Ração"))
print(cachorrim1.dormir())




print(outro_cachorro.acordar())
print(outro_cachorro.brincar(brincadeira="Correr atrás do rabo"))
print(outro_cachorro.comer(comida="Carne"))
print(outro_cachorro.dormir())
