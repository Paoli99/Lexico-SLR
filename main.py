from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from config import default 

import lexer 
#from  SLR import SLR 

config = default 
window = tk.Tk()
window.title("Compilador")
window.config(bg = 'white')
window.geometry(f'{config["reference_width"] + 30}x{config["reference_height"]+230}')
window.wm_maxsize(config["reference_width"] + 30, config["reference_height"]+230)

ttk.Label(window,
		text = "Compilador",
		font = ("Times New Roman", 15),).grid(column = 0,row = 0)

def click():
	errorCanvas.delete("all") 
	code = codeText.get('1.0', 'end-1c')   
	print(code)

	#text = input('basic > ')
	result, error = lexer.run('<archivo>', code)

	if error: 
		print(error.as_string())
		errorMessage = error.as_string()

		#lista.insert(lista.index('end'), str(errorMessage))
		errorCanvas.create_text(200,100, text = errorMessage)
	else: 
		print(result)
		results = result 
		errorCanvas.create_text(200,80, text = 'Analisis correcto!')
		errorCanvas.create_text(200,100, text = results)

def abrirTxt():
	Flag = 1 
	Stack = ['0']
	Reglas = ['a', 'b', '$', 'A', 'S']
	S_R = ['S3', 'S4', 'R1', 'R2', 'R3']
	Producciones = ['AA', 'aA', 'b']
	Replace = ['S', 'A', 'A']
	Tabla = [
	['S3', 'S4', 'Error', '2', '1'],
	['Error', 'Error', 'Accept', 'Error', 'Error'], 
	['S3', 'S4', 'Error', '5', 'Error'], 
	['S3', 'S4', 'Error', '6', 'Error'], 
	['R3','R3','R3', 'Error', 'Error'], 
	['R1','R1','R1', 'Error', 'Error'], 
	['R2','R2','R2', 'Error', 'Error']] 

	text = codeText.get('1.0', 'end-1c')
	global p, pop, temp, i, a, row, lista, canvas 
	temp = 0 

	print('Tamaño del la expresion: ', len(text))
	a = ('Tamaño del la expresion: ', len(text))
	errorCanvas.create_text(100 ,100, text = a)
	def Reduce(msg, Producciones, a):
		pass 
		global p, pop, post, temp, i, row 

		#lista.insert(lista.index('end'), "Iniciando SLR... ")

		if text[a] == Reglas[i]: 
			temp = Stack[len(Stack)-1]
			post = int(temp)
			print("Inicio del nuevo stack es: ", post)
			txt =("Inicio del nuevo stack es: ", post)
			errorCanvas.create_text(100,150, text = txt)


			print("Nuevo SR es: ", Tabla[post][i])

			txt =("Nuevo SR es: ", Tabla[post][i])
			errorCanvas.create_text(100,200, text = txt)

			for j in range(0, len(S_R),1):
				if Tabla[post][i] == S_R[j]:
					print('La condicion es: ', S_R[j])
					msg = S_R[j]
					if msg[0] == 'S':
						Stack.append(text[a])
						Stack.append(msg[1])
						print("Regla a seguir del segundo valor: ", msg[1])
						txt =("Regla a seguir del segundo valor: ", msg[1])
						errorCanvas.create_text(100,210, text = txt)
						
						print(Stack)
						txt = Stack 
						errorCanvas.create_text(100,220, text = Stack)


						if Flag == 1:
							i = i + 1
						
					elif msg[0] == 'R':
						print(Stack)
						temp = Stack[len(Stack)-1]
						post = int(temp)
						p = int(msg[1])
						print('Regla a seguir del segundo valor: ', p) 
						pop = len(Producciones[p-1])*2
						print('Valores para el pop: ', pop)
						for k in range(0, pop,1):
							Stack.pop()
						Stack.append(Replace[p-1])
						ss = Replace[p-1]
						row = int(Stack[len(Stack)-2])
						for i in range(0, len(Reglas), 1):
							if ss == Reglas[i]:
								print('Nuevo stack es: ', post)
								print('Ultimo valor del stack: ', Stack)
								print('Nuevo SR luego del reduce: ', Tabla[row][i])
								Stack.append(Tabla[row][i])
								print(Stack)

						if Stack[len(Stack)-2] == 'S':
							print(Stack)

						else: 
							Reduce(msg, Producciones, a)

	a = 0 
	check = 2 
	stop = len(text)
	#print('While loop is going to stop on: ', stop)

	while a < stop:
		print("-------------------------")
		print('El valor de lambda es: ' , a, 'y el input es: ', text[a])
		
		for i in range(0, len(Reglas),1):

			if text[a] == Reglas[i]:
				temp = Stack[len(Stack)-1]
				post = int(temp)
				print('Principio del nuevo stack: ', post)
				print('Nuevo SR es: ', Tabla[post][i])

				if Tabla[post][i] == 'Accept':
					Stack.append(Tabla[post][i])
					print(Stack)
					a=a+1
					break 

				if Tabla[post][i] == 'Error':
					print('Gramatica invalida')
					a=a+1 
					break 

				else: 
					for j in range (0, len(S_R),1): 
						if Tabla[post][i] == S_R[j]:
							print('Condicion es: ', S_R[j])
							msg = S_R[j]

							if msg[0] == 'S':
								Stack.append(text[a])
								Stack.append(msg[1])
								print('Regla a seguir del segundo valor: ', msg[1])
								print(Stack)
								if Flag == 1:
									a=a+1

							elif msg[0] == 'R': 
								Flag = 0
								Reduce(msg, Producciones,a)

							else: 
								print("Error")

			if Stack[len(Stack)-check] == 'S':
				a=a+1
				check=check+1 
				break 


#-------------------------------------------------------
#----------------GUI------------------------------------
#-------------------------------------------------------

codeText = scrolledtext.ScrolledText(window,
									wrap = tk.WORD,
									width = int(config["reference_width"]),
									height = 20,
									font = ("Times New Roman",
											10))

codeText.grid(row = 1, column = 0, pady = 10, padx = 10)
codeText.columnconfigure(0, weight=1)
codeText.columnconfigure(1, weight=3)


errorFrame= Frame(window, width = int(config["reference_width"]), height= int(config["reference_height"]),  bg = "black")
errorFrame.grid(row = 2, column = 0, sticky="EWNS")
errorCanvas = Canvas(errorFrame, bg = "light gray", width = int(config["reference_width"]), height= int(config["reference_height"]))
errorCanvas.grid(row = 2, column = 0, sticky="EWNS")


tool_bar_frame = Frame(window, width = 40, height = 10, bg = config["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, sticky=W)

btnRun = Button(tool_bar_frame, text = 'Run Lexer',  font= config["fuente_fields"], command = click, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
btnRun.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

btnOpenTxt = Button(tool_bar_frame, text = 'Run SLR', font= config["fuente_fields"], command = abrirTxt, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
btnOpenTxt.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)


codeText.focus()
window.mainloop()