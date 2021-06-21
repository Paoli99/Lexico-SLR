import time 
from tkinter import * 
from tkinter import ttk 
from config import default 

config = default 

Flag = 1 
Stack = ['0']
Rules = ['a', 'b', '$', 'A', 'S']
S_R = ['S3', 'S4', 'R1', 'R2', 'R3']
Product = ['AA', 'aA', 'b']
Replace = ['S', 'A', 'A']
Parser_Table = [
['S3', 'S4', 'Error', '2', '1'],
['Error', 'Error', 'Accept', 'Error', 'Error'], 
['S3', 'S4', 'Error', '5', 'Error'], 
['S3', 'S4', 'Error', '6', 'Error'], 
['R3','R3','R3', 'Error', 'Error'], 
['R1','R1','R1', 'Error', 'Error'], 
['R2','R2','R2', 'Error', 'Error']] 

text = input('Ingrese la expresion regular: ')
global p, pop, temp, i, a, row, lista, canvas 
temp = 0 

print('Tamaño del la expresion: ', len(text))

#def SLR(tk, canvas, lista):
    #Reduce(msg, Product, a, tk, canvas, lista)

def Reduce(msg, Product, a):
    pass 
    global p, pop, post, temp, i, row 

    #lista.insert(lista.index('end'), "Iniciando SLR... ")

    if text[a] == Rules[i]: 
        temp = Stack[len(Stack)-1]
        post = int(temp)
        print("Inicio del nuevo stack es: ", post)
        print("Nuevo SR es: ", Parser_Table[post][i])

        for j in range(0, len(S_R),1):
            if Parser_Table[post][i] == S_R[j]:
                print('Condition match is: ', S_R[j])
                msg = S_R[j]
                if msg[0] == 'S':
                    Stack.append(text[a])
                    Stack.append(msg[1])
                    print("Product rule second value is: ", msg[1])
                    print(Stack)

                    if Flag == 1:
                        i = i + 1
                    
                elif msg[0] == 'R':
                    print(Stack)
                    temp = Stack[len(Stack)-1]
                    post = int(temp)
                    p = int(msg[1])
                    print('Product rule second value is: ', p) 
                    pop = len(Product[p-1])*2
                    print('pop values: ', pop)
                    for k in range(0, pop,1):
                        Stack.pop()
                    Stack.append(Replace[p-1])
                    ss = Replace[p-1]
                    row = int(Stack[len(Stack)-2])
                    for i in range(0, len(Rules), 1):
                        if ss == Rules[i]:
                            print('new stack is: ', post)
                            print('last value of stack is: ', Stack)
                            print('new SR is After Reduce: ', Parser_Table[row][i])
                            Stack.append(Parser_Table[row][i])
                            print(Stack)

                    if Stack[len(Stack)-2] == 'S':
                        print(Stack)

                    else: 
                        Reduce(msg, Product, a)

a = 0 
check = 2 
stop = len(text)
print('While loop is going to stop on: ', stop)

while a < stop:
    print("-------------------------")
    print('your a is: ' , a, 'and input is: ', text[a])
    
    for i in range(0, len(Rules),1):

        if text[a] == Rules[i]:
            temp = Stack[len(Stack)-1]
            post = int(temp)
            print('Start new stack is: ', post)
            print('new SR is: ', Parser_Table[post][i])

            if Parser_Table[post][i] == 'Accept':
                Stack.append(Parser_Table[post][i])
                print(Stack)
                a=a+1
                break 

            if Parser_Table[post][i] == 'Error':
                print('Sorry! Invalid Input Grammar not pass it')
                a=a+1 
                break 

            else: 
                for j in range (0, len(S_R),1): 
                    if Parser_Table[post][i] == S_R[j]:
                        print('Condition match is: ', S_R[j])
                        msg = S_R[j]

                        if msg[0] == 'S':
                            Stack.append(text[a])
                            Stack.append(msg[1])
                            print('Product rule second value is: ', msg[1])
                            print(Stack)
                            if Flag == 1:
                                a=a+1

                        elif msg[0] == 'R': 
                            Flag = 0
                            Reduce(msg, Product,a)

                        else: 
                            print("Error")

        if Stack[len(Stack)-check] == 'S':
            a=a+1
            check=check+1 
            break 

