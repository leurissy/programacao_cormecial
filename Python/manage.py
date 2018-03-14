class MinhaClasse:
	"""docstring for MinhaClasse"""
	
	atributo_publico = None
	__atributo_privado = 5

	def __init__(self):
		self.atributo_publico= 10

	def metodo(self):
		return self.atributo_publico *2

	def get_atributo_privado(self):
		return self.__atributo_privado
		
		