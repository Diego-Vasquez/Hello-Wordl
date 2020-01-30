class carro ():

    def __init__ (self, nombre, fabricante):
        self.nombre = nombre
        self.fabricante = fabricante
        self.estado = 'Apagado'
        self.velocidad = 0


    def __str__ (self):
        

    def encender (self):
        if self.estado == 'Apagado':
            self.estado = 'Encendido'
            return '\nEl auto encendio.'
        
        else:
            return '\nEl auto ya está encendido.'
    

    def acelerar (self):
        if self.estado == 'Encendido':
            self.velocidad += 10
            return '\nEl auto ahora tiene una velocidad de ' + str(self.velocidad) + ' m/s².'
        
        else:
            return '\nEl auto no puede acelerar porque esta apagado.'
    

    def frenar (self):
        if self.estado == 'Encendido':
            if self.velocidad != 0:
                self.velocidad = 0
                return '\nEl auto frenó.'
            else:
                return '\nEl vehiculo ya está detenido.'

        else:
            return '\nEl carro no esta encendido. Ya esta detenido.'


    def apagar (self):
        if self.estado != 'Apagado':
            self.estado = 'Apagado'
            return '\nEl auto se apagó.'
        
        else:
            return '\nEl auto ya está apagado.'

carro_1 = carro ('Prototipo', 'Empresa_A')

print (carro_1.velocidad)
print (carro_1.estado)
print (carro_1.acelerar())
print (carro_1.encender())
print (carro_1.acelerar())
print (carro_1.acelerar())
print (carro_1.acelerar())
print (carro_1.frenar())
print (carro_1.acelerar())
print (carro_1.frenar())
print (carro_1.frenar())
print (carro_1.apagar())
print (carro_1.apagar())





