#user_input_nine_element_of_3*3_matrix
#Matrix_A
a11 = int(input('a11: '))
a12 = int(input('a12: '))
a13 = int(input('a13: '))
a21 = int(input('a21: '))
a22 = int(input('a22: '))
a23 = int(input('a23: '))
a31 = int(input('a31: '))
a32 = int(input('a32: '))
a33 = int(input('a33: '))
#Adjoint_before_tranpose_start
adja11 = a22*a33-a23*a32
adja12 = a21*a33-a31*a23
adja13 = a33*a21-a31*a23
adja21 = a33*a12-a32*a13
adja22 = a33*a11-a31*a13
adja23 = a32*a11-a31*a12
adja31 = a23*a12-a22*a13
adja32 = a23*a11-a21*a13
adja33 = a22*a11-a21*a12
#Adjoint_before_transpose_end
#modulus_of_A
mod_A = a11*(adja11)

    
    
    


    
    
    

