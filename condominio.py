

# Utilizar encapsulamiento
# Discutir en grupo sobre el uso de variables de esta forma
# Que es name mangling 
# ¿Es   posible   acceder   un   atributo   definido como:
#                           self.__nombre_atributo  desde   una subclase o desde el programaprincipal? 
#                           Experimente y muestre ejemplos


''' Crear 2 instancias de edificios y 2 de condominios horizaontales y demuestre la utilizacion de atributos y metodos '''

class Condominio:
    __direccion = "Las blancas palomas 1457, Buin"
    lista_administrador = []
    lista_guardias = []
    num_unidades_habitacionales = 0
    lista_unidades = []
    cuenta_corriente = ""
    # Agregar 4 atributos adicionales (Walter)


    def __init__(self):
        pass

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
    # 3 atributos y 4 metodos

    empresa_contratista = 'Tus guardias'
    tipo_contrato = 'Contrato de plata'
    sueldo_bruto = '800.000 mil pesos'

    
    def __init__(self, nombre, rut, sexo):
        self.nombre = nombre
        self.rut = rut
        self.sexo = sexo

    def desayunar(self):
        print("8:00 am hora de desayunar en el casino")

    def almuerzo(self):
        print('13:00 pm hora de almorzar en el casino')

    def fin_jornada(self):
        print('17:00 pm hora de fin de jornada')



class UnidadHabitacional:
    # 3 atributos y 4 metodos

    tipo = 'Material sólido'
    cantidad_habitaciones = 6
    extras = 'calefaccion central y aire acondicionado'

    def __init__(self, numero):
        self.numero = numero 

    def abrir_puerta(self):
        print('Se abre la puerta del hogar numero', self.numero)

    def cerrar_puerta(self):
        print('Se cierra la puerta del hogar numero', self.numero)

    def prender_luces(self):
        print('Prender luces')



class CuentaCorriente:
    # 3 atributos y 4 metodos

    banco = 'Banco Terra'
    tipo = 'Cuenta Corriente'
    beneficios = 'No se cobra comision en ninguna operación'
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo =saldo

    def girar(self, giro):
        self.saldo -= giro
        print('Se ha efectuado un giro por el monto de', giro)

    def abono(self, abono):
        self.saldo += abono
        print('Se ha abonado la cantidad de', abono)

    def consulta_saldo(self):
        print('El saldo actual es', self.saldo)


class Terreno:
    # 6 atributos y 6 metodos

    nombre_dueño_terreno = 'Metropolis'
    seguros = 'terreno con seguros comprometidos'
    tipo = 'terreno privado'
    sector = 'urbano'
    finalidad = 'Habitacional'
    extensiones = 'Para fines de contruccion horizontal y vertical'
    
    def __init__(self, nombre_terreno):
        self.nombre_terreno = nombre_terreno

    def consulta_hta(self):
        print('Las hectareas edificafles consisten en 10 hectareas')

    def factibilidad_agua_potable(self):
        print('100 por ciento de factibilidad de agua potable')

    def factibilidad_electricidad(self):
        print('100 por ciento de factibilidad de electricidad')

    def factiilidad_servicios_digitales(self):
        print('100 por ciento de factibilidad de servicios digitales')

    def seguridad_terreno(self):
        print('El terreno cuenta con todas las normas de seguridad para construir')




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
    print(condominio1.get_guardias()) # Imprimo lista de guardias, para verificacion
