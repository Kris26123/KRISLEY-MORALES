def numero_mas_alto():


    nu_1= float(input("Ingrese el primer:"))
    nu_2= float(input("Ingrese el segundo numero:"))
    nu_3= float(input("Ingrse el tercer numero:"))

    if   (nu_1 > nu_2) and (nu_1 > nu_3): 
     numero_alto=nu_1
     print("El numero mas alto es:",numero_alto)
    elif (nu_2 == nu_1) and (nu_2 == nu_3):
     numero_alto=nu_2
     print("El numero mas alto es:",numero_alto)
    elif (nu_3 > nu_1) and (nu_3 > nu_1):
       numero_alto=nu_3
       print("El numero mas alto es:",numero_alto)
    elif (nu_1== nu_2) and (nu_1== nu_3):
       numero_alto=nu_1
       print("El numero mas alto es:",numero_alto)
    elif (nu_1 > nu_3) and (nu_1 > nu_2):
       numero_alto=nu_1
       print("El numero mas alto es:",numero_alto)
    elif (nu_2 == nu_3) and (nu_2 == nu_1):
       numero_alto=nu_2
       print("El numero mas alto es:",numero_alto)
    return
 

numero_mas_alto()
