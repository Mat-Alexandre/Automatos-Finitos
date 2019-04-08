class Estado:
	def __init__(self, nome):
		self.nome = nome
		self.transicao = {}
		self.final = False
		self.inicial = False

def criar_estados(alfabeto, qtd_estados):
	"""
	Criação de um dict auxiliar com todos os símbolos do alfabeto.
	Inicialmente, todos os estados levam à um estado "vazio",
	independente de qual símbolo tenha sido processado.
	"""
	estados = []
	for i in range(0, qtd_estados):
		nome = 'q'+str(i)
		estados.append(Estado(nome))

	return estados

def setTransicao(lista_estados, alfabeto):
	"""
	Recebe o alfabeto e define, para cada estado, a transição do mesmo
	"""
	for estado in lista_estados:
		for simbolo in alfabeto:
			index = input(estado.nome+"--"+simbolo+"-->")
			estado.transicao[simbolo] = index

def setInicial(estados):
	"""
	Lista inicialmente todos os estados existentes
	O usuário entra com a id ".nome" do estado desejado
	"""
	for i in estados:
		print(i.nome)
	index = input("Qual estado inicial? ")

	for elem in estados:
		if elem.nome == index:
			elem.inicial = True

def setFinal(estados):
	"""
	AFDs/AFNs podem ter mais de um estado final
	Sendo assim, é requerido uma quantidade para definir o loop
	*obs: fazer tratamento de entrada. 
		*Verificar se a quantidade de estados finais desejada é menor ou igual 
		à quantidade de estados existentes
		*Caso o estado já possua o atributo "final" igual a True, pedir para que o usuário 
		entre com um valor diferente
	"""
	qtd = int(input("Quantidade de estados finais:"))

	for i in estados:
		print(i.nome)
	while qtd != 0:
		index = input("Estado final: ")
		for e in estados:
			if e.nome == index:
				e.final = True
		qtd -= 1

def getPalavra(alfabeto):
	ok = False
	while ok == False:
		palavra = input("Digite a palavra a ser preocessada: ")
		for simb in palavra:
			if alfabeto.count(simb) == 0:
				print("A palavra contém símbolos não existentes no alfabeto")
			else:
				ok = True
	return palavra

def processa_palavra(lista_estados, palavra):
	"""
	Busca pelo estado inicial do autômato
	A cada símbolo da palavra, verificar no dict de transição do estado atual
	qual é o nome do próximo estado e armazenar esse valor em 'nome_prox'.
	Procurar na lista de estados qual estado possui o '.nome' igual ao 'nome_prox' e torná-lo o atual
	Se o último estado for final, então o atômato aceita a palavra
	"""
	for e in lista_estados:
		if e.inicial == True:
			e_atual = e

	for simb in  palavra:
		nome_prox = e_atual.transicao[simb]
		for e in lista_estados:
			if e.nome == nome_prox:
				e_atual = e
	return "é aceita" if e_atual.final is True else "não é aceita"

def main():
	alfabeto	  = input("Entre com o alfabeto: ")
	qtd_estados   = int(input("Digite a quantidade de estados: "))
	lista_estados = criar_estados(alfabeto, qtd_estados)
	setInicial(lista_estados)
	setTransicao(lista_estados, alfabeto)
	setFinal(lista_estados)
	palavra       = getPalavra(alfabeto)
	print("A palavra", palavra, processa_palavra(lista_estados, palavra), "pelo autômato")

if __name__ == '__main__':
	main()
