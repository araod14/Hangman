import os
import random

def select_words():
    words=[]
    with open("./data.txt", "r", encoding="utf-8") as f:
        words=[line.rstrip() for line in f]          
        palabra=random.choice(words)
        acentos={"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
        
        for acen in acentos:
            if acen in palabra:
                palabra=palabra.replace(acen, acentos[acen])
    return palabra
    
def hagman():
    palabra=select_words()
    list_=[]
    b=len(palabra)
    for n in range (b):
        list_.append("-")

    list=[]
    for i in palabra:
        list.append(i)

    while "-" in list_:
        print("\n \n Juego del ahorcado, elige letra por letra para hallar la palabra!")
        print(*list_, sep = " ")
        
        letra=str(input("Ingresa una letra ",))
        z=palabra.count(letra)
        b=len(palabra)
        list_l=[]

        if letra in list:
            d=list.index(letra)
            list_l.append(d)
            if z >1:
                d=list.index(letra,d+1,b)
                list_l.append(d)

        for w in list_l:
            list_[w]=letra
        list_l.clear()    
        os.system("cls")

    palabra=palabra.upper()
    print("\n \n Ganaste! la palabra era: ", palabra)

if __name__=="__main__":
    hagman()