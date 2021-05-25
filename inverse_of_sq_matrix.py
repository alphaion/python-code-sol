#user_input_four_element_of_square_matrix
A11 = int(input('A11: '))
A12 = int(input('A12: '))
A21 = int(input('A21: '))
A22 = int(input('A22: '))
modA = (A11*A22)-(A12*A21)
if modA == 0:
    print('Matrix does not exist, because modulous of A = 0')
else:
    print('\t\t~~~Adjoint of Matrix A~~~')
    A11,A22 = A22,A11
    A21,A12 = (-A21),(-A12)
    print('A11: ',A11)
    print('A12: ',A12)
    print('A21: ',A21)
    print('A22: ',A22)
    print('\n\t\t\t A inverse')
    print('A11: ',A11,'/',modA)
    print('A12: ',A12,'/',modA)
    print('A21: ',A21,'/',modA)
    print('A22: ',A22,'/',modA)
    
    
    

