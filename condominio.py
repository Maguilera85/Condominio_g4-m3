

# Utilizar encapsulamiento
# Discutir en grupo sobre el uso de variables de esta forma
# Que es name mangling 
# ¿Es   posible   acceder   un   atributo   definido como:
#                           self.__nombre_atributo  desde   una subclase o desde el programaprincipal? 
#                           Experimente y muestre ejemplos


''' Crear 2 instancias de edificios y 2 de condominios horizaontales y demuestre la utilizacion de atributos y metodos '''

class Condominio:

    def __init__(self):
        self.__direccion = "Las blancas palomas 1457, Buin"
        self.lista_administrador = []
        self.lista_guardias = []
        self.num_unidades_habitacionales = 0
        self.lista_unidades = []
        self.cuenta_corriente = ""
        # Agregar 4 atributos adicionales

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, new_adress):
        self.__direccion = new_adress

    def set_administrador(self, admin):
        self.lista_administrador = admin

    def get_administrador(self):
        return self.lista_administrador

    def add_guardia(self, new_guard):
        self.lista_guardias.append(new_guard)

    def del_guardia(self, del_guard):
        if del_guard in self.lista_guardias:
            self.lista_guardias.remove(del_guard)
        else:
            print("No se puede eliminar, guardia no existe en registros")

    def get_guardias(self):
        return self.lista_guardias

    def get_unidades(self):
        return self.num_unidades_habitacionales

    # Agregar 4 metodos adicionales (Walter)

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

class Comunidad: #Sebastian
    pass

# Crear 5 atributos y 6 metodos propios que diferencien a cada una de estas subclases . Demostrar 2 casos de polimorfismo en metodos.
class CondominioVertical(Terreno, Comunidad):
    pass

class CondominioHorizontal(Terreno, Comunidad):
    pass



if __name__ == "__main__":
    # Pruebas de la clase Condominio
    condominio1 = Condominio() # Creo instancia de condominio
    print(condominio1.get_direccion()) # muestra direccion
    condominio1.set_direccion("Esta es la nueva direccion") # cambio direccion
    print(condominio1.get_direccion()) # imprimo direccion nueva
    condominio1.set_administrador("Inserte aquí un administrador") # Agrego administrador
    print(condominio1.get_administrador()) # imprimo nombre del administrador agregado
    condominio1.add_guardia("Inserte aquí un guardia") # Agrego guardia a lista
    print(condominio1.get_guardias()) # Imprimo lista de guardias
    condominio1.add_guardia("Guardia a eliminar") # crear guardia para ser eliminado
    print(condominio1.get_guardias()) # Imprimo lista de guardias, para verificacion
    condominio1.del_guardia("Guardia a eliminar") # elimino guarida de lista
    print(condominio1.get_guardias())