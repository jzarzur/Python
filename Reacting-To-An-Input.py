def valoresAB():
    A = int(input("Enter A value:"))
    B = int(input("Enter B value:"))

    while B > A:
        print("A:", A, "B:", B, "- B greater than A.End of algorithm.")
        return
    if B == A:
        print("A:", A, "B:", B, "- A and B are equal!")
        valoresAB()
    else:
        valoresAB()

valoresAB()
    
