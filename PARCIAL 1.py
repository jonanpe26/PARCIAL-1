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



empleados={"codigo":{
    "nombre": nombre,
    "departamento": departamento,
    "antiguedad": antiguedad,
    "evaluacion":{
        "puntualidad": puntualidad,
        "equipo": equipo,
        "productividad": productividad,
        "promedio": promedio,
        "estado":"satisfacortio"
    },
    "contacto":{
        "telefono": telefono,
        "correo": correo
    }
}}
print(f"total de empleados registrados: {len(empleados)}")

buscar=int(input("ingrese el codigo del empleado que desea buscar"))



