

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

class Comunidad:
    pass


# Crear 5 atributos y 6 metodos propios que diferencien a cada una de estas subclases . Demostrar 2 casos de polimorfismo en metodos.
class CondominioVertical(Terreno, Comunidad):
    pass

class CondominioHorizontal(Terreno, Comunidad):
    pass


input()