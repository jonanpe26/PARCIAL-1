#PARCIAL 1
empleados={}

cantidad=int(input("cuantos trabajadores desea ingresar"))
for i in range(cantidad):


    codigo=int(input("Ingrese el codigo del trabajador"))
    nombre =(input("ingrese el nombre del empleado"))
    departamento =(input("ingrese el departamento en el que trabaja"))
    antiguedad=int(input("ingrese los anos trabajados"))
    telefono=int(input("ingrese un numero de telefono"))
    correo = (input("ingrese correo electronico"))



    puntualidad = int(input("ingrese calificacion de puntualidad"))
    equipo = int(input("ingrese calificacion de trabajo en equipo"))
    productividad = int(input("ingrese calificacion de productividad"))
    observaciones = (input("escriba alguna observacion"))

    promedio = (puntualidad + equipo + productividad) / 3

    estado = "SATISFACTORIO" if promedio >= 7 else "NO SATISFACTORIO"



    empleados[codigo]={
        "nombre": nombre,
        "departamento": departamento,
        "antiguedad": antiguedad,
        "contacto": {
            "telefono": telefono,
            "correo": correo
        },
        "evaluacion": {
            "puntualidad": puntualidad,
            "equipo": equipo,
            "productividad": productividad,
            "promedio": promedio,
            "estado": estado,
            "observaciones": observaciones
        }
    }

print(f"total de empleados registrados: {len(empleados)}")
buscar = int(input("ingrese codigo de empleado "))

if buscar in empleados:
    emp = empleados[buscar]
    print("NOMBRE:", emp["nombre"])
    print("DEPARTAMENTO:", emp["departamento"])
    print("ANTIGUEDAD:", emp["antiguedad"])
    print("TELEFONO:", emp["contacto"]["telefono"])
    print("CORREO:", emp["contacto"]["correo"])
    print("PUNTUALIDAD:", emp["evaluacion"]["puntualidad"])
    print("EQUIPO:", emp["evaluacion"]["equipo"])
    print("PRODUCTIVIDAD:", emp["evaluacion"]["productividad"])
    print("PROMEDIO:", round(emp["evaluacion"]["promedio"], 2))
    print("ESTADO:", emp["evaluacion"]["estado"])
    print("OBSERVACIONES:", emp["evaluacion"]["observaciones"])
else:
    print("EMPLEADO NO ENCONTRADO.")
