matrix = f"""
1. Matrix 2 x 2
2. Matrix 3 x 3"""
print("Operation Matrix :", matrix)
print()

masukan = int(input("Select the orde matrix operation you want : "))
print()

#matrix ordo 2x2
if masukan  == 1 :
    print("input your matrix A :")
    a11 = int(input("a11 = "))
    a12 = int(input("a12 = "))
    a21 = int(input("a21 = "))
    a22 = int(input("a22 = "))
    print()
    print("input your matrix B :")
    b11 = int(input("b11 = "))
    b12 = int(input("b12 = "))
    b21 = int(input("b21 = "))
    b22 = int(input("b22 = "))
    print()
    A = f"""
    A = {a11, a12}
        {a21, a22}

    B = {b11, b12}
        {b21, b22}"""
    print("The Matrix your input :", A)
    print()

    List = f"""
    1. add matrix (+)
    2. subtraction matrix (-)
    3. Multiplication matrix (x)
    4. Transpose Matrix
    5. Determinant Matrix
    6. Invers Matrix"""
    print("List Matrix operation =",List)
    print( )
    operation = (int(input("What matrix operation do you want to do : ")))
    if operation == 1 :
        print()
        AB11 = a11 + b11
        AB12 = a12 + b12
        AB21 = a21 + b21
        AB22 = a22 + b22
        AB = f"""
        A+B = {AB11, AB12}
              {AB21, AB22}"""
        print("Result of the matrix add (+):", AB)
        print()
    elif operation == 2 :
        print()
        AB11 = a11 - b11
        AB12 = a12 - b12
        AB21 = a21 - b21
        AB22 = a22 - b22
        AB = f"""
        A-B = {AB11, AB12}
              {AB21, AB22}"""
        print("Result of the subtraction matrix (-) :", AB)
        print()
    elif operation == 3 :
        print()
        AB11 = (a11 * b11) + (a12 * b21)
        AB12 = (a11 * b12) + (a12 * b22)
        AB21 = (a21 * b11) + (a22 * b21)
        AB22 = (a21 * b12) + (a22 * b22)
        AB = f"""
        AB = {AB11, AB12}
             {AB21, AB22}"""
        print("Result of the Multiplication Matrix :", AB)
        print()
    elif operation == 4:
        print()
        AB = f"""
        A(^T) = {a11, a21}
                {a12, a22}
        B(^T) = {b11, b21}
                {b12, b22}"""
        print("Result of the Transpose Matrix :",AB)
        print()
    elif operation == 5:
        print()
        determine_A = (a11*a22)-(a21*a12)
        determine_B = (b11*b22)-(b21*b12)
        AB = f"""
        |A| = {determine_A}
        |B| = {determine_B}"""
        print("Result of the determine Matrix :", AB)
        print()
    elif operation == 6 :
        determine_A = (a11*a22)-(a21*a12)
        determine_B = (b11*b22)-(b21*b12)

        Invers_A_11 = {(1/determine_A)*a11} 
        Invers_A_12 = {(1/determine_A)*(-(a12))} 
        Invers_A_21 = {(1/determine_A)*(-(a21))} 
        Invers_A_22 = {(1/determine_A)*a22}

        Invers_B_11 = {(1/determine_B)*b11} 
        Invers_B_12 = {(1/determine_B)*(-(b12))} 
        Invers_B_21 = {(1/determine_B)*(-(b21))} 
        Invers_B_22 = {(1/determine_B)*b22}

        AB = f"""
        A^(-1)= {Invers_A_22, Invers_A_12}
                {Invers_A_21, Invers_A_11}

         B^(-1)= {Invers_B_22, Invers_B_12 }
                 {Invers_B_21, Invers_B_11}"""
        print("Result of the Invers Matrix :", AB)
        print()
    else :
        print("Your input must be a number and the number must be in the list")

#matrix ordo 3x3
if masukan  == 2 :
    print("input your matrix A : ")
    a11 = int(input("a11 = "))
    a12 = int(input("a12 = "))
    a13 = int(input("a13 = "))
    a21 = int(input("a21 = "))
    a22 = int(input("a22 = "))
    a23 = int(input("a23 = "))
    a31 = int(input("a31 = "))
    a32 = int(input("a32 = "))
    a33 = int(input("a33 = "))
    print()
    print("input your matrix B : ")
    b11 = int(input("b11 = "))
    b12 = int(input("b12 = "))
    b13 = int(input("b13 = "))
    b21 = int(input("b21 = "))
    b22 = int(input("b22 = "))
    b23 = int(input("b23 = "))
    b31 = int(input("b31 = "))
    b32 = int(input("b32 = "))
    b33 = int(input("b33 = "))
    print()
    A = f"""
    A = {a11, a12, a13}
        {a21, a22, a23}
        {a31, a32, a33}
    
    B = {b11, b12, b13}
        {b21, b22, b23} 
        {b31, b32, b33}"""
    print("The Matrix your input : ", A)
    print()

    List = f"""
    1. add matrix (+)
    2. subtraction matrix (-)
    3. Multiplication matrix (x)
    4. Transpose Matrix
    5. Determinant Matrix
    6. Invers Matrix"""
    print("List Matrix operation =",List)
    print( )
    operation = (int(input("What matrix operation do you want to do : ")))
    if operation == 1 :
        print()
        AB11 = a11 + b11
        AB12 = a12 + b12
        AB13 = a13 + b13
        AB21 = a21 + b21
        AB22 = a22 + b22
        AB23 = a23 + b23
        AB31 = a31 + b31
        AB32 = a32 + b32
        AB33 = a33 + b33
        AB = f"""
        A+B = {AB11, AB12, AB13}
              {AB21, AB22, AB23}
              {AB31, AB32, AB33}"""
        print("Result of the matrix add (+) :", AB)
        print()
    elif operation == 2 :
        print()
        AB11 = a11 - b11
        AB12 = a12 - b12
        AB13 = a13 - b13
        AB21 = a21 - b21
        AB22 = a22 - b22
        AB23 = a23 - b23
        AB31 = a31 - b31
        AB32 = a32 - b32
        AB33 = a33 - b33
        AB = f"""
        A-B = {AB11, AB12, AB13}
              {AB21, AB22, AB23}
              {AB31, AB32, AB33}"""
        print("Result of the subtraction matrix (-) :", AB)
        print()
    elif operation == 3 :
        print()
        AB11 = (a11 * b11) + (a12 * b21) + (a13 * b31)
        AB12 = (a11 * b12) + (a12 * b22) + (a13 * b32)
        AB13 = (a11 * b13) + (a12 * b23) + (a13 * b33)
        AB21 = (a21 * b11) + (a22 * b21) + (a23 * b31)
        AB22 = (a21 * b12) + (a22 * b22) + (a23 * b32)
        AB23 = (a21 * b13) + (a22 * b23) + (a23 * b33)
        AB31 = (a31 * b11) + (a32 * b21) + (a33 * b31)
        AB32 = (a31 * b12) + (a32 * b22) + (a33 * b32)
        AB33 = (a31 * b13) + (a32 * b23) + (a33 * b33)
        AB = f"""
        AB = {AB11, AB12, AB13}
             {AB21, AB22, AB23}
             {AB31, AB32, AB33}"""
           
        print("Result of the Multiplication Matrix :", AB)
        print()
    elif operation == 4:
        print()
        AB = f"""
        A(^T) = {a11, a21, a31}
                {a12, a22, a32}
                {a13, a23, a33}

        B(^T) = {b11, b21, b31}
                {b12, b22, b32}
                {b13, b23, b33}"""
        print("Result of the Transpose Matrix :",AB)
        print()
    elif operation == 5:
        print()
        determine_A = ((a11*a22*a33)+(a12*a23*a31)+(a13*a21*a32))-((a13*a22*a31)+(a11*a23*a32)+(a12*a21*a33))
        determine_B = ((b11*b22*b33)+(b12*b23*b31)+(b13*b21*b32))-((b13*b22*b31)+(b11*b23*b32)+(b12*b21*b33))
        AB = f"""
        |A| = {determine_A}
        |B| = {determine_B}"""
        print("Result of the determine Matrix :", AB)
        print()
    elif operation == 6 :
        determine_A = ((a11*a22*a33)+(a12*a23*a31)+(a13*a21*a32))-((a13*a22*a31)+(a11*a23*a32)+(a12*a21*a33))
        determine_B = ((b11*b22*b33)+(b12*b23*b31)+(b13*b21*b32))-((b13*b22*b31)+(b11*b23*b32)+(b12*b21*b33))
        print()
        AB = f"""
        |A| = {determine_A}
        |B| = {determine_B}"""
        print("Result of the determine Matrix :", AB)
        print()

        m11 = (a33*a22) - (a32*a23)
        m12 = (a21*a33) - (a23*a31)
        m13 = (a21*a32) - (a22*a31)

        m21 = (a12*a33) - (a13*a32)
        m22 = (a11*a33) - (a13*a31)
        m23 = (a11*a32) - (a12*a31)

        m31 = (a12*a23) - (a13*a22)
        m32 = (a11*a23) - (a13*a21)
        m33 = (a11*a22) - (a12*a21)

        n11 = (b33*b22) - (b32*b23)
        n12 = (b21*b33) - (b23*b31)
        n13 = (b21*b32) - (b22*b31)

        n21 = (b12*b33) - (b13*b32)
        n22 = (b11*b33) - (b13*b31)
        n23 = (b11*b32) - (b12*b31)

        n31 = (b12*b23) - (b13*b22)
        n32 = (b11*b23) - (b13*b21)
        n33 = (b11*b22) - (b12*b21)

        m11_ = (+(m11))
        m12_ = (-(m12))
        m13_ = (+(m13))
        m21_ = (-(m21))
        m22_ = (+(m22))
        m23_ = (-(m23))
        m31_ = (+(m31))
        m32_ = (-(m32))
        m33_ = (+(m33))

        n11_ = (+(m11))
        n12_ = (-(m12))
        n13_ = (+(m13))
        n21_ = (-(m21))
        n22_ = (+(m22))
        n23_ = (-(m23))
        n31_ = (+(m31))
        n32_ = (-(m32))
        n33_ = (+(m33))

        cof_a = f"""
        COF(A) = {m11_, m12_, m13_}
                 {m21_, m22_, m23_}
                 {m31_, m32_, m33_}

        COF(B) = {n11_, n12_, n13_}
                 {n21_, n22_, n23_}
                 {n31_, n32_, n33_}""" 
        print("then cofaktor matrix =", cof_a)
        print()

        adj_a = f"""
        ADJ(A) = {m11_, m21_, m31_}
                 {m12_, m22_, m32_}
                 {m13_, m23_, m33_}

        ADJ(B) = {n11_, n21_, n31_}
                 {n12_, n22_, n32_}
                 {n13_, n23_, n33_}""" 
        print("then adjoin matrix =", adj_a)
        print()

        I_m11 = {(1/determine_A)*m11_} 
        I_m12 = {(1/determine_A)*m21_} 
        I_m13 = {(1/determine_A)*m31_} 
        I_m21 = {(1/determine_A)*m12_} 
        I_m22 = {(1/determine_A)*m22_} 
        I_m23 = {(1/determine_A)*m32_} 
        I_m31 = {(1/determine_A)*m13_} 
        I_m32 = {(1/determine_A)*m23_} 
        I_m33 = {(1/determine_A)*m33_} 
        
        I_n11 = {(1/determine_A)*n11_} 
        I_n12 = {(1/determine_A)*n21_} 
        I_n13 = {(1/determine_A)*n31_} 
        I_n21 = {(1/determine_A)*n12_} 
        I_n22 = {(1/determine_A)*n22_} 
        I_n23 = {(1/determine_A)*n32_} 
        I_n31 = {(1/determine_A)*n13_} 
        I_n32 = {(1/determine_A)*n23_} 
        I_n33 = {(1/determine_A)*n33_} 

        AB = f"""
        A^(-1)= {I_m11, I_m12, I_m13}
                {I_m21, I_m22, I_m23}
                {I_m31, I_m32, I_m33}
        B^(-1)= {I_n11, I_n12, I_n13}
                {I_n21, I_n22, I_n23}
                {I_n31, I_n32, I_n33}"""
        print("Result of the Invers Matrix :", AB)
        print()
    else :
            print("Your input must be a number and the number must be in the list")
            print()
else :
     print("Your input must be a number and the number must be in the list")
     print()


