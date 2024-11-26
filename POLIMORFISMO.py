# Clase base
class UISBucaramanga:
    def __init__(self, nombre, apellido, identidad, fnacimiento, profesion, horas):
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.fnacimiento = fnacimiento
        self.profesion = profesion
        self.horas = horas

    def mostrar(self):
        return f"nombre: {self.nombre} {self.apellido}, doc: {self.identidad}, profesión: {self.profesion}"

class Vigilancia(UISBucaramanga):
    def __init__(self, nombre, apellido, identidad, fnacimiento, profesion, horas, turno, lugar, sueldo):
        super().__init__(nombre, apellido, identidad, fnacimiento, profesion, horas)  
        self.turno = turno
        self.lugar = lugar
        self.sueldo = sueldo

    def mostrar(self):
        return f"{super().mostrar()}, Turno: {self.turno}, Lugar: {self.lugar}, Sueldo: {self.sueldo}"

class Administrativos(UISBucaramanga):
    def __init__(self, nombre, apellido, identidad, fnacimiento, profesion, horas, dependencia, sueldo, funciones):
        super().__init__(nombre, apellido, identidad, fnacimiento, profesion, horas)  
        self.dependencia = dependencia
        self.sueldo = sueldo
        self.funciones = funciones

    def mostrar(self):
        return f"{super().mostrar()}, Dependencia: {self.dependencia}, Sueldo: {self.sueldo}, Funciones: {self.funciones}"

class Auxiliares(UISBucaramanga):
    def __init__(self, nombre, apellido, identidad, fnacimiento, profesion, horas, funciones):
        super().__init__(nombre, apellido, identidad, fnacimiento, profesion, horas) 
        self.funciones = funciones

    def mostrar(self):
        return f"{super().mostrar()}, Funciones: {self.funciones}"

vigilante = Vigilancia("Maria", "Pérez", "123456789", "04/05/2005", "Vigilante", 40, "Nocturno", "Puerta 1", 1000)
admin = Administrativos("Laura", "Gómez", "987654321", "15/05/1975", "Administrativo", 35, "Finanzas", 1500, "Gestión presupuestaria")
auxiliar = Auxiliares("Luis", "Martínez", "654321987", "20/10/1990", "Auxiliar", 20, "Mantenimiento")

print(vigilante.mostrar())
print(admin.mostrar())
print(auxiliar.mostrar())
