# list = [[2,8,4,7,5,3,1,9,6],       # exemple for test :
#         [3,9,6,2,1,8,7,4,5],
#         [1,5,7,4,9,6,8,3,2],
#         [6,7,2,5,3,1,9,8,4],
#         [8,3,1,6,4,9,2,5,7],
#         [5,4,9,8,2,7,6,1,3],
#         [4,1,5,9,6,2,3,7,8],
#         [7,6,3,1,8,5,4,2,9],
#         [9,2,8,3,7,4,5,6,1]]

# **********************************function************************************
def fill_list(ligne,colonne,nomber):             # pour remplir les cas :
    list[ligne][colonne] = nomber

def validation(TABLE):                           # pour valider les colonnes et les lignes et les bloc:
    for i in range(len(TABLE)):
        for j in range( len(TABLE[i]) - 1):
            for k in range(j+1 , len(TABLE[i]) ):
                if TABLE[i][j] == TABLE[i][k]:
                    # print("----------------> No valider <----------------")
                    # print("---> Nomber repeter est " ,TABLE[i][k] ,".")
                    return False
                    
    return True  

def list_colonne(table_col):             # pour identifier les colonnes :
    for j in range(9): 
        s = []
        for i in range(9):
            s.append(list[i][j])
        table_col.append(s) 

def bloc(list,table_bloc):              # pour identifier les bloc :
    for i in range(0,9,3):
        for j in range(0,9,3):    
            bloc1 = []
            for k in range(i,i+3):
                for m in range(j,j+3):
                    bloc1.append(list[k][m])
            table_bloc.append(bloc1)    

def affichage(list):                # pour l'affichage :
    for i in range(9):
        for j in range(9):
            if j == 0 :
                print("|" , end=" ")
            print(list[i][j] , end=" ")
            if j in [2,5,8]:
                print("|" , end=" ")
        print()  
        if i in [2,5]:
            print("| _ _ _ _ _ _ _ _ _ _ _ |")  
            print('|                       |') 


def resultat_validation(table):
    return_validation = validation(table)
    if return_validation == False:
        print("|--------------> No valider <--------------|")
    else:
        print("|----------------> valider <---------------|")


# **********************************body************************************

list = [[0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],]

table_col  = [] 
table_bloc = []

print()
print("                                            *** SUDOKU GAME ***                                            ")
print()

while True :                                                               # pour stockage :
    print()
    print(" _ _ _ _ _ _ _ _ _ _ _ _ ")  
    print('|                       |')
    affichage(list)
    print("|_ _ _ _ _ _ _ _ _ _ _ _|")  
    print()
    print(' -------------------------> Pour arreter entrer le nomber "99" :')
    ligne = int(input(' -------> Entrer le nomber de ligne (0 ---> 8): '))
    if ligne == 99 :
        break
    while ligne > 8 or ligne < 0 and ligne != 99:
        print('-------> no valider :')
        ligne = int(input(' -------> Entrer le nomber de ligne (0 ---> 8): '))
        if ligne == 99 :
            break
        
    colonne = int(input(' -------> Entrer le nomber de colonne (0 ---> 8): '))
    if colonne == 99 :
        break
    while colonne > 8 or colonne < 0 and colonne != 99:
        print('-------> no valider :')
        colonne = int(input(' -------> Entrer le nomber de colonne (0 ---> 8): '))
        if colonne == 99 :
            break

    nomber = int(input(' -------> Entrer le nomber prefirer (1 ---> 9): '))
    if nomber == 99 :
        break
    while nomber > 9 or nomber < 1 and nomber != 99:
        print('-------> no valider :')
        nomber = int(input(' -------> Entrer le nomber prefirer (1 ---> 9): '))
        if nomber == 99 :
            break

    fill_list(ligne,colonne,nomber)

   


list_colonne(table_col)                                   
bloc(list,table_bloc)
print(' __________________________________________')
print('|                                          |')
print('|       *** validation des linges ***      |')
resultat_validation(list)
print('|                                          |')

print('|      *** validation des colonnes ***     |')
resultat_validation(table_col)
print('|                                          |')

print('|      *** validation des blocs ***        |')
resultat_validation(table_bloc)
print('|                                          |')
print('|__________________________________________|')
print()


   






