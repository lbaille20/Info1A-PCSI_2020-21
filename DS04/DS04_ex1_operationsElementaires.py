#Affichage des matrices
def cprint(A):
    lg_max=1
    for ligne in A:
        for coefficient in ligne:
            if len(str(coefficient))>lg_max:
                lg_max= len(str(coefficient))
    for ligne in A:
        print ("|",end='')
        for coefficient in ligne:
            espaces=(lg_max-len(str(coefficient)))
            avant,après=espaces-espaces//2,espaces//2
            print(" "*avant+str(coefficient)+" "*après+" ",end='')
        print ("|")

#Opérations élémentaires
def permutation(A,i1,i2):
    A[i1],A[i2]=A[i2],A[i1]
#ou bien
def permutation0(A,i1,i2):
    temp=A[i1]
    A[i1]=A[i2]
    A[i2]=temp
#ou bien
def permutation1(A,i1,i2):
    #nombre de colonnes de la matrice :
    #len(A[0])
    for j in range(len(A[0])):
        A[i1][j],A[i2][j]=A[i2][j],A[i1][j]

def permutation2(A,i1,i2):
    #nombre de colonnes de la matrice :
    #len(A[0])
    for j in range(len(A[0])):
        temp=A[i1][j]
        A[i1][j]=A[i2][j]
        A[i1][j]=temp
    
###########################

def dilatation(A,i,a):
    #nombre de colonnes de la matrice :
    #len(A[0])
    for j in range(len(A[0])):
        A[i][j]=a*A[i][j]


def transvection(A,i1,b,i2):
    for j in range(len(A[0])):
        A[i1][j]=A[i1][j]+b*A[i2][j]

#matrice de test
A=[[2,4,-4,8],[3,9,-6,9],[4,17,-11,41]]







