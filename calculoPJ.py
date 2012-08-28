#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  calculoPJ.py
#  
#  Copyright 2012 Victor <victor@vfreitas>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 

from datetime import date

def catch_data():
	"""
	Função que faz o calculo de salário de Pessoa Jurídica.
	
	Não precisa de parâmetros.
	Calculo baseado em 30 dias de trabalho.
	
	Após efetuar o calculo é feita uma pergunta para saber 
	se você deseja salvar o resultado em um arquivo.
	
	O arquivo é denominado listaPGTO.txt e fica localizado 
	na mesma pasta que o arquivo .PY deste programa.
	"""
	
	print("Olá, bem vindo ao programa de calculo de salários PJ")
	data_entrada = int(raw_input('Qual dia do mês começa o calculo? (digite 0 para o mês inteiro) : '))
	salario_bruto = float(raw_input("Qual valor total do salário? ( formato : XXXX.XX ) : "))
	c = raw_input("Confirma entrada no dia %i e o salário de %s?  [y/n] : " % (data_entrada, salario_bruto))
	
	if c == "y":
		total = str(round((30 - data_entrada) * (salario_bruto / 30), 2))
		print(" ------------ Salário total de : "+ total)
		record = raw_input("Deseja gravar esta informação no arquivo listaPGTO.txt? [y/n] : ")
		
		if record == "y":
			data = date.today()
			texto = "Data : %s --> R$ %s \n" % (data, total)
			
			with open("listaPGTO.txt", "a") as arq:
				arq.write(texto)
				arq.close
			
			print("Arquivo salvo com sucesso! Obrigado por usar nosso programa!");
		else:
			print("Obrigado por usar nosso programa!");
	
	else:
		print("\n \n Por favor, tente novamente")
		catch_data()
		
print "\n ---------------------------- ** ---------------------------- \n"
print catch_data.__doc__
print "\n ---------------------------- ** ---------------------------- \n"
catch_data()
