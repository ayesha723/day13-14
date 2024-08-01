def matrix_add(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return "error"
    
    for row1 , row2 in zip(matrix1 , matrix2):
        if len (row1) != len(row2):


            return "error"
     
    result_matrix=[]

    for row1 , row2 in zip(matrix1 , matrix2):
        result_row=[]
        for elm1 , elm2 in zip(matrix1 , matrix2):
            result_row.append(elm1+elm2)

    
        result_matrix.append(result_row)
    return result_matrix

matrix1=[[1,2] , [3,5]]
matrix2=[[4,9],[1,7]]
result = matrix_add(matrix1, matrix2)
print(result)