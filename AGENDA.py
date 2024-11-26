##Sin la libreria panda:

##class Agenda:
##    def __init__(self):
##        self.contactos = []
##    
##    def correo(self, correo):
##        if "@" in correo:
##            dominio = correo.split("@")[-1]
##            if dominio == "hotmail.com" or dominio == "gmail.com":
##                return True
##        return False
##
##    def añadir_contacto(self):
##        nombre = input("Ingrese el nombre del usuario: ")
##
##        while True:
##            try:
##                telefono = int(input("Ingrese el teléfono (10 dígitos): "))
##                if len(str(telefono)) == 10:
##                    break
##                else:
##                    print("El teléfono debe tener exactamente 10 dígitos.")
##            except ValueError:
##                print("El teléfono debe contener solo números enteros.")
##        
##        while True:
##            correo = input("Ingrese el correo electrónico (solo hotmail.com o gmail.com): ")
##            if self.correo(correo):
##                break
##            else:
##                print("El correo no es válido. Debe ser de hotmail.com o gmail.com.")
##        
##        contacto = {
##            "nombre": nombre,
##            "telefono": telefono,
##            "correo": correo
##        }
##        self.contactos.append(contacto)
##        print(f"{contacto['nombre']} añadido con éxito.")
##    
##    def lista(self):
##        if self.contactos:
##            print("Lista de contactos:")
##            for i, contacto in enumerate(self.contactos, 1):
##                print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")
##        else:
##            print("No hay contactos en la agenda.")
##    
##    def buscar(self):
##        nombre = input("Ingrese el nombre del usuario: ")
##        correo = input("Ingrese el correo del usuario: ")
##        for contacto in self.contactos:
##            if contacto['nombre'] == nombre and contacto['correo'] == correo:
##                print(f"Contacto encontrado: {contacto['nombre']} - {contacto['telefono']} - {contacto['correo']}")
##                return
##        print("Contacto no encontrado.")
##    
##    def editar(self):
##        correo = input("Ingrese el correo del contacto a editar: ")
##        for contacto in self.contactos:
##            if contacto['correo'] == correo:
##                print("""Opciones de edición:
##                1. Nombre
##                2. Teléfono
##                3. Correo
##                """)
##                opcion = input("¿Qué desea editar?: ")
##                
##                if opcion == "1":
##                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
##                    contacto['nombre'] = nuevo_nombre
##                
##                elif opcion == "2":
##                    while True:
##                        try:
##                            nuevo_telefono = int(input(f"Ingrese el nuevo teléfono para {contacto['nombre']}: "))
##                            if len(str(nuevo_telefono)) == 10:
##                                contacto['telefono'] = nuevo_telefono
##                                break
##                            else:
##                                print("El teléfono debe tener 10 dígitos.")
##                        except ValueError:
##                            print("El teléfono debe contener solo números.")
##                
##                elif opcion == "3":
##                    nuevo_correo = input(f"Ingrese el nuevo correo electrónico: ")
##                    while not self.correo(nuevo_correo):
##                        print("El correo electrónico no es válido. Intente nuevamente.")
##                        nuevo_correo = input(f"Ingrese el nuevo correo electrónico: ")
##                    contacto['correo'] = nuevo_correo
##                
##                print("Contacto actualizado con éxito.")
##                return
##        print("Correo no encontrado.")
##    
##    def eliminar(self):
##        correo = input("Ingrese el correo del contacto a eliminar: ")
##        for i, contacto in enumerate(self.contactos):
##            if contacto['correo'] == correo:
##                self.contactos.pop(i)
##                print("Contacto eliminado.")
##                return
##        print("Contacto no encontrado.")
##    
##    def menu(self):
##        while True:
##            print("""Menú:
##                1. Añadir contacto
##                2. Lista de contactos
##                3. Buscar contacto
##                4. Editar contacto
##                5. Eliminar contacto
##                6. Cerrar agenda
##            """)
##            opcion = input("¿Qué desea hacer?: ")
##            if opcion == "1":
##                self.añadir_contacto()
##            elif opcion == "2":
##                self.lista()
##            elif opcion == "3":
##                self.buscar()
##            elif opcion == "4":
##                self.editar()
##            elif opcion == "5":
##                self.eliminar()
##            elif opcion == "6":
##                print("Cerrando agenda...")
##                break
##            else:
##                print("Opción no válida. Intente nuevamente.")
##
##if __name__ == "__main__":
##    agenda = Agenda()
##    agenda.menu()













#Con la libreria panda
import pandas as pd

class Agenda:
    def __init__(self):
        self.contactos = pd.DataFrame(columns=["nombre", "telefono", "correo"])

    def validar_correo(self, correo):
        if "@" in correo:
            dominio = correo.split("@")[-1]
            return dominio in ["hotmail.com", "gmail.com"]
        return False

    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del usuario: ")

        while True:
            try:
                telefono = int(input("Ingrese el teléfono (10 dígitos): "))
                if len(str(telefono)) == 10:
                    break
                else:
                    print("El teléfono debe tener exactamente 10 dígitos.")
            except ValueError:
                print("El teléfono debe contener solo números enteros.")
        
        while True:
            correo = input("Ingrese el correo electrónico (solo hotmail.com o gmail.com): ")
            if self.validar_correo(correo):
                break
            else:
                print("El correo no es válido. Debe ser de hotmail.com o gmail.com.")
        
        nuevo_contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
        self.contactos = self.contactos.append(nuevo_contacto, ignore_index=True)
        print(f"{nombre} añadido con éxito.")

    def lista(self):
        if not self.contactos.empty:
            print("Lista de contactos:")
            print(self.contactos.to_string(index=False))
        else:
            print("No hay contactos en la agenda.")

    def buscar(self):
        nombre = input("Ingrese el nombre del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        contacto = self.contactos[(self.contactos["nombre"] == nombre) & (self.contactos["correo"] == correo)]
        
        if not contacto.empty:
            print(f"Contacto encontrado:\n{contacto.to_string(index=False)}")
        else:
            print("Contacto no encontrado.")

    def editar(self):
        correo = input("Ingrese el correo del contacto a editar: ")
        contacto_idx = self.contactos[self.contactos["correo"] == correo].index

        if not contacto_idx.empty:
            print("""Opciones de edición:
                1. Nombre
                2. Teléfono
                3. Correo
            """)
            opcion = input("¿Qué desea editar?: ")
            
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                self.contactos.at[contacto_idx[0], "nombre"] = nuevo_nombre
            elif opcion == "2":
                while True:
                    try:
                        nuevo_telefono = int(input("Ingrese el nuevo teléfono (10 dígitos): "))
                        if len(str(nuevo_telefono)) == 10:
                            self.contactos.at[contacto_idx[0], "telefono"] = nuevo_telefono
                            break
                        else:
                            print("El teléfono debe tener exactamente 10 dígitos.")
                    except ValueError:
                        print("El teléfono debe contener solo números enteros.")
            elif opcion == "3":
                while True:
                    nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
                    if self.validar_correo(nuevo_correo):
                        self.contactos.at[contacto_idx[0], "correo"] = nuevo_correo
                        break
                    else:
                        print("El correo no es válido.")
            print("Contacto editado con éxito.")
        else:
            print("Contacto no encontrado.")

    def eliminar(self):
        correo = input("Ingrese el correo del contacto a eliminar: ")
        contacto_idx = self.contactos[self.contactos["correo"] == correo].index

        if not contacto_idx.empty:
            self.contactos = self.contactos.drop(contacto_idx)
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

    def menu(self):
        while True:
            print("""Menú:
                1. Añadir contacto
                2. Lista de contactos
                3. Buscar contacto
                4. Editar contacto
                5. Eliminar contacto
                6. Cerrar agenda
            """)
            opcion = input("¿Qué desea hacer?: ")
            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.lista()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.editar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                print("Cerrando...")
                break
            else:
                print("Error. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
