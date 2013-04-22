
#funcion que calcula la edad que tendran en el anio en curso
def calcula_antiguedad(anio_curso, persona) :    
    print "%s,  cumplira %s anios" % (persona['nombre'], str(anio_curso - int(persona['fecha'])))
    
anio_curso = ""
print "**********Instrucciones**********"
print "a) Ingresa el anio en curso (4 digitos Ej. 1970)."
print "b) Ingresa Nombre y anio de nacimiento de 3 personas, 1 a la vez."
print "c) El programa calculara la edad que cumpliran en el anio en curso."
#validacion para asegurarse que el Anio tiene 4 digitos
while len(anio_curso) != 4 :
    anio_curso = raw_input("Anio en curso : ")
#inicialia una lista para las personas
personas = []
i = 0
#loop para capturar los datos en la lista
while i < 3 :
    nombre = raw_input('Nombre: ')
    fecha = raw_input('Fecha Nacimiento: ')    
    #misma validacion para la fecha de nacimiento
    if len(fecha) == 4 :
        #si pasa la validacion, agrega un diccionario a la lista
        personas.append( {'nombre' : nombre, 'fecha' : fecha} )        
        i += 1
    else :
        #sino pasa la validacion, pide que vuelva a introducir los datos
        print "Vuelve a introducir los datos..."

#loop para desplegar la informacion de CADA persona en particular
for persona in personas :
    #manda llamar la funcion que calcula la edad en el anio en curso
    calcula_antiguedad(int(anio_curso) , persona)


raw_input()
