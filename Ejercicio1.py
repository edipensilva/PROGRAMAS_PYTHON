print("***************************************")
print("**SISTEMA CONTROL DE VACACIONES RAPPI**")
print("***************************************\n")

nombre = input("Ingrese su nombre: ")
clave = int(input("Ingrese la clave del departamento[1,2,3]: "))
anos = float(input("Ingrese el número de años laborados: "))

if clave == 1:
    if anos == 1:
        print("El empleado ",nombre, "tiene 6 días de vacaciones.")
    elif anos >= 2 and anos <= 6:    
        print("El empleado ",nombre, "tiene 14 días de vacaciones.")
    elif anos >= 7:   
        print("El empleado ",nombre, "tiene 20 días de vacaciones.")
    else:
        print("El empleado ",nombre, " Sin derecho a vacaciones")
        
elif clave == 2:
    if anos == 1:
        print("El empleado ",nombre, "tiene 7 días de vacaciones.")
    elif anos >= 2 and anos <= 6:    
        print("El empleado ",nombre, "tiene 15 días de vacaciones.")
    elif anos >= 7:   
        print("El empleado ",nombre, "tiene 22 días de vacaciones.")
    else:
        print(nombre, " Sin derecho a vacaciones")

elif clave == 3:
    if anos == 1:
        print("El empleado ",nombre, "tiene 10 días de vacaciones.")
    elif anos >= 2 and anos <= 6:    
        print("El empleado ",nombre, "tiene 20 días de vacaciones.")
    elif anos >= 7:   
        print("El empleado ",nombre, "tiene 30 días de vacaciones.")
    else:
        print(nombre, " Sin derecho a vacaciones")

else:
    print(nombre, " La clave no existe.")
    
print("Fin.")
