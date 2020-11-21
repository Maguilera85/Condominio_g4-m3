

# Utilizar encapsulamiento
# Discutir en grupo sobre el uso de variables de esta forma
# Que es name mangling 
# ¿Es   posible   acceder   un   atributo   definido como:
#                           self.__nombre_atributo  desde   una subclase o desde el programaprincipal? 
#                           Experimente y muestre ejemplos


''' Crear 2 instancias de edificios y 2 de condominios horizaontales y demuestre la utilizacion de atributos y metodos '''

class Comdominio:
    direccion = ""
    lista_administrador = []
    lista_guardias = []
    num_unidades_habitacionales = ""
    lista_unidades = []
    cuenta_corriente = ""
    # Agregar 4 atributos adicionales


    def __init__(self):
        pass

    def get_direccion(self):
        pass

    def set_direccion(self):
        pass

    def set_administrador(self):
        pass

    def get_administrador(self):
        pass

    def add_guardia(self):
        pass

    def del_guardia(self):
        pass

    def get_guardias(self):
        pass

    def get_unidades(self):
        pass

    # Agregar 4 metodos adicionales

class Guardia:
    # Crear 3 atributos y 4 metodos
    pass

class UnidadHabitacional:
    # Crear 3 atributos y 4 metodos
    pass

class CuentaCorriente:
    # Crear 3 atributos y 4 metodos
    pass


class Terreno:
    # Crear 6 atributos y 6 metodos
    pass


# Crear dos clases con herencia multiple de las clases Terreno y Comunidad, que se llamen CondominioVertical y CondominioHorizontal

class Comunidad:
    pass

# Crear 5 atributos y 6 metodos propios que diferencien a cada una de estas subclases . Demostrar 2 casos de polimorfismo en metodos.
class CondominioVertical(Terreno, Comunidad):
    pass

class CondominioHorizontal(Terreno, Comunidad):
    pass
