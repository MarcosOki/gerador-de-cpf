#by Over.exe
#gerador de cpf

import random
import time
quantidadeCpf = int(input("quantidade de cpf a ser gerada "))
vezes = 0
def randomizar():
	cpf = random.randint(10000000000,99999999999)
	cpf = str(cpf)
	cpf = list(cpf)
	cpf.insert(3,".")
	cpf.insert(7,".")
	cpf.insert(11,"-")
	return "".join(cpf)
	

while vezes < quantidadeCpf:
	randomizar()
	time.sleep(0.01)
	cpf = randomizar()
	vezes += 1
	print(cpf)
	
