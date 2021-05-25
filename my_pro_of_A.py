#Taking_user_input_as_element
a11 = int(input('a11: '))
a12 = int(input('a12: '))
a13 = int(input('a13: '))
a21 = int(input('a21: '))
a22 = int(input('a22: '))
a23 = int(input('a23: '))
a31 = int(input('a31: '))
a32 = int(input('a32: '))
a33 = int(input('a33: '))
#user_input_end
#adjoint_of_each_element_start
A11 = a22*a33-a32*a23
A12 = -(a33*a21-a31*a23)
A13 = a32*a21-a31*a22
A21 = -(a33*a12-a32*a13)
A22 = a33*a11-a31*a13
A23 = -(a32*a11-a31*a12)
A31 = a23*a12-a22*a13
A32 = -(a23*a11-a21*a13)
A33 = a22*a11-a21*a12
#adjoint_of_each_element_end
#mod_of_A
mod = a11*(A11)-a12*(A12)+a13*(A13)
#end_of_mod_A
#swap_the_values
A12,A21=A21,A12
A13,A31=A31,A13
A23,A32=A32,A23
#swap_end
#to_print_adjoint_of_given_matrix
print('\n~~~~\t\tAdjoint of Matrix A\t\t~~~~')
print('A11:',A11)
print('A12:',A12)
print('A13:',A13)
print('A21:',A21)
print('A22:',A22)
print('A23:',A23)
print('A31:',A31)
print('A32:',A32)
print('A33:',A33)
#mod_of_A
print('\n~~~~\t\tA Inverse \t\t~~~~')
print(A11,'/',mod)
print(A12,'/',mod)
print(A13,'/',mod)
print(A21,'/',mod)
print(A22,'/',mod)
print(A23,'/',mod)
print(A31,'/',mod)
print(A32,'/',mod)
print(A33,'/',mod)
print('\n\n\t\tEnd of Program')








