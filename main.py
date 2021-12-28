def getMatrix():

    rows = int(input("Enter No Of Rows : "))
    cols = int(input("Enter No of Columns : "))
    print()

    matrix = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            print('For matrix [',i,']','[',j,']')
            matrix[i][j] = int(input("Enter Element : "))

    return matrix


def addMatrices(matrix1,matrix2):

    if len(matrix1) != len(matrix2) and len(matrix1[0]) != len(matrix2[0]):
        print("Addition Not Possible ")
        return

    else:
        additionMatrix = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                additionMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

        print("\nAddition of Matrices : ")
        displayMatrix(additionMatrix)
        return additionMatrix


def subtractMatrices(matrix1,matrix2):

    #print(len(matrix1))
    #print("\n",len(matrix2))

    if len(matrix1) != len(matrix2) and len(matrix1[0]) != len(matrix2[0]):
        print("Substraction Not Possible ")
        return

    else:
        subtractionMatrix = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                subtractionMatrix[i][j] = matrix1[i][j] - matrix2[i][j]

        print("\nSubtraction of Matrices : ")
        displayMatrix(subtractionMatrix)
        return subtractionMatrix

def multiplyMatrices(matrix1,matrix2):

    if len(matrix1[0]) != len(matrix2):
        print("Multiplication is Not Possible "
              "\n Doesn't Satisfy The rule for Matrix Multiplication")
        return

    multiplicationMatrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplicationMatrix[i][j] += (matrix1[i][k] * matrix2[k][j])

    print("\nMultiplication of Matrices : ")
    displayMatrix(multiplicationMatrix)
    return multiplicationMatrix


def transpose(matrix):

    transposeMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix1[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposeMatrix[j][i] = matrix[i][j]

    print("\nTranspose of Matrix :")
    displayMatrix(transposeMatrix)
    return transposeMatrix



def displayMatrix(matrix):
    for row in matrix:
        print(row)
    print()


# main

print("\nFor Matrix 1 :")
matrix1 = getMatrix()

print("\nFor Matrix 2 :")
matrix2 = getMatrix()

print("\nEntered Matrix 1 : ")
displayMatrix(matrix1)

print("\nEntered Matrix 2 :")
displayMatrix(matrix2)

toContinue = 1

while(toContinue == 1):

    print("1->Addition\n2->Subtraction\n3->Multiplication\n4->Transpose")
    choice = int(input("Select Choice : "))

    if choice == 1:
        addMatrices(matrix1,matrix2)
    elif choice == 2:
        subtractMatrices(matrix1,matrix2)
    elif choice == 3:
        multiplyMatrices(matrix1,matrix2)
    elif choice == 4:
        print("\n1->Transpose of Matrix 1\n1->Transpose of Matrix 2")
        choice = int(input("Select Matrix : "))
        if choice == 1:
            transpose(matrix1)
        else:
            transpose(matrix2)
    else:
        print("\nInvalid Choice:")
        toContinue = 1.

    print("\n\t Do you want to continue [y/n] [1/0]")
    choice = int(input())




