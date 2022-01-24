#-- coding: utf-8 --
print("Bem vindo a pizzaria!")
print("Cardapio:\n --- 1.Quatro queijos\n --- 2.Calabreza\n --- 3.Frango com catupiry\n --- 0.Sair")
sabor = int(input("Digite o sabor desejado: "))
queijo = 30
calabreza = 32
frango = 35
if sabor ==1:
	sabor = queijo
elif sabor ==2:
	sabor = calabreza
elif sabor ==3:
	sabor = frango
else:
	print("Comando invalido")
	
#Tamanho da pizza

print ("Digite o tamanho da pizza:")
tamanho = int(input("1.P\n2.M\n3.G\n4.GG: "))
if tamanho ==1:
	sabor = 1*sabor
elif tamanho ==2:
	sabor = 1.2*sabor
elif tamanho ==3:
	sabor = 1.5*sabor
elif tamanho ==4:
	sabor = 1.9*sabor
else:
	print ("Comando invalido")
	
#Acrescimo de refrigerante
	
coca1l=5.00
coca3l=10.00
lata=4.00

refri = str(input("Deseja refrigerante? (S/N): "))
if refri == "S":
	print ("Refrigerantes\n1. --- Coca 1L\n2. --- Coca 3L\n3. --- Refri Lata")
	tiporefri=int(input("Digite qual refrigerante deseja: "))
	if tiporefri ==1:
		tiporefri==coca1l
		total = sabor+tiporefri
		print ("Total a pagar: ",total)
	elif tiporefri ==2:
		tiporefri==coca3l
		total = sabor+tiporefri
		print ("Total a pagar: ",total)
	elif tiporefri ==3:
		tiporefri==lata
		total = sabor+tiporefri
		print ("Total a pagar: ",total)
	else:
		print ("Comando incorreto!")
elif refri == "N":
	print("Total a pagar: ", sabor)
else:
	print ("Comando incorreto!")
print ("Obrigado e volte sempre! :D")
