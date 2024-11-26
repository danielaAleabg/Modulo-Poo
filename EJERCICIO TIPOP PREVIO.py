import pandas as pd
import re
from datetime import datetime, timedelta

class Biblioteca:
    def __init__(self, archivo_libros='Archivos/libros.csv', archivo_usuarios='Archivos/usuarios.csv', archivo_prestamos='Archivos/prestamos.csv'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.archivo_prestamos = archivo_prestamos

        # Diccionario para credenciales de administrador
        self.admin_credentials = {'usuario': 'admin', 'contraseña': 'admin1'}

        try:
            self.df_libros = pd.read_csv(self.archivo_libros)
        except FileNotFoundError:
            self.df_libros = pd.DataFrame(columns=['Código', 'Autor', 'Tema', 'Páginas', 'Cantidad', 'Precio'])
            self.df_libros.to_csv(self.archivo_libros, index=False)

        try:
            self.df_usuarios = pd.read_csv(self.archivo_usuarios)
        except FileNotFoundError:
            self.df_usuarios = pd.DataFrame(columns=['Nombre', 'Clave'])
            self.df_usuarios.to_csv(self.archivo_usuarios, index=False)

        try:
            self.df_prestamos = pd.read_csv(self.archivo_prestamos)
        except FileNotFoundError:
            self.df_prestamos = pd.DataFrame(columns=['Usuario', 'Código Libro', 'Fecha Préstamo', 'Fecha Entrega', 'Devuelto'])
            self.df_prestamos.to_csv(self.archivo_prestamos, index=False)

        self.Menu()

    def validar_codigo(self, codigo):
        """Valida que el código sea alfanumérico y tenga exactamente 6 caracteres"""
        if re.fullmatch(r'^[A-Za-z0-9]{6}$', codigo):
            return True
        else:
            print("Código inválido. Debe ser alfanumérico y tener exactamente 6 caracteres.")
            return False

    def AgregarLibro(self):
        codigo = input("Ingrese el código del libro (alfanumérico de 6 caracteres): ")
        if not self.validar_codigo(codigo):
            return  # Sale de la función si el código no es válido
        
        autor = input("Ingrese el autor: ")
        tema = input("Ingrese el tema: ")
        paginas = int(input("Ingrese el número de páginas: "))
        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        precio = float(input("Ingrese el precio: "))
        
        nuevo_libro = pd.DataFrame({
            'Código': [codigo],
            'Autor': [autor],
            'Tema': [tema],
            'Páginas': [paginas],
            'Cantidad': [cantidad],
            'Precio': [precio]
        })
        
        self.df_libros = pd.concat([self.df_libros, nuevo_libro], ignore_index=True)
        self.df_libros.to_csv(self.archivo_libros, index=False)
        print(f"Libro agregado correctamente en {self.archivo_libros}")
        self.Menu()

    def EliminarLibro(self):
        codigo = input("Ingrese el código del libro que desea eliminar: ")
        if codigo in self.df_libros['Código'].values:
            self.df_libros = self.df_libros[self.df_libros['Código'] != codigo]
            self.df_libros.to_csv(self.archivo_libros, index=False)
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")
        self.Menu()

    def AgregarUsuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        clave = input("Ingrese la clave de seguridad: ")
        
        nuevo_usuario = pd.DataFrame({
            'Nombre': [nombre],
            'Clave': [clave]
        })
        
        self.df_usuarios = pd.concat([self.df_usuarios, nuevo_usuario], ignore_index=True)
        self.df_usuarios.to_csv(self.archivo_usuarios, index=False)
        print(f"Usuario agregado correctamente en {self.archivo_usuarios}")
        self.Menu()

    def verificar_usuario(self):
        """Verifica que el nombre y la clave del usuario sean correctos"""
        nombre = input("Ingrese su nombre: ")
        clave = input("Ingrese su clave: ")
        
        usuario = self.df_usuarios[(self.df_usuarios['Nombre'] == nombre) & (self.df_usuarios['Clave'] == clave)]
        if not usuario.empty:
            print("\n✅ Acceso concedido ✅\n")
            return nombre
        else:
            print("\n❌ Usuario o clave incorrectos ❌\n")
            return None

    def verificar_admin(self):
        """Verifica las credenciales del administrador"""
        usuario = input("Ingrese el usuario de administrador: ")
        contraseña = input("Ingrese la contraseña de administrador: ")
        
        if usuario == self.admin_credentials['usuario'] and contraseña == self.admin_credentials['contraseña']:
            print("\n✅ Acceso de administrador concedido ✅\n")
            return True
        else:
            print("\n❌ Usuario o contraseña de administrador incorrectos ❌\n")
            return False

    def PrestarLibro(self):
        usuario = input("Ingrese el nombre del usuario: ")
        if usuario not in self.df_usuarios['Nombre'].values:
            print("Usuario no encontrado. Registre primero al usuario.")
            return

        codigo_libro = input("Ingrese el código del libro: ")
        if codigo_libro in self.df_libros['Código'].values:
            libro = self.df_libros[self.df_libros['Código'] == codigo_libro].iloc[0]
            if libro['Cantidad'] > 0:
                fecha_prestamo = datetime.now()
                fecha_entrega = fecha_prestamo + timedelta(days=15)

                nuevo_prestamo = pd.DataFrame({
                    'Usuario': [usuario],
                    'Código Libro': [codigo_libro],
                    'Fecha Préstamo': [fecha_prestamo.strftime('%Y-%m-%d')],
                    'Fecha Entrega': [fecha_entrega.strftime('%Y-%m-%d')],
                    'Devuelto': [False]
                })

                self.df_prestamos = pd.concat([self.df_prestamos, nuevo_prestamo], ignore_index=True)
                self.df_libros.loc[self.df_libros['Código'] == codigo_libro, 'Cantidad'] -= 1
                self.df_libros.to_csv(self.archivo_libros, index=False)
                self.df_prestamos.to_csv(self.archivo_prestamos, index=False)
                print(f"Libro prestado correctamente. Fecha de entrega: {fecha_entrega.strftime('%Y-%m-%d')}")
            else:
                print("No hay ejemplares disponibles de este libro.")
        else:
            print("Código de libro no encontrado.")
        self.Menu()

    def ConsultarPrestamosUsuario(self):
        nombre_verificado = self.verificar_usuario()
        if nombre_verificado:
            prestamos_usuario = self.df_prestamos[(self.df_prestamos['Usuario'] == nombre_verificado) & (self.df_prestamos['Devuelto'] == False)]
            if prestamos_usuario.empty:
                print("No hay préstamos pendientes para este usuario.")
            else:
                print("Préstamos pendientes:")
                print(prestamos_usuario[['Código Libro', 'Fecha Préstamo', 'Fecha Entrega']])
        self.Menu()

    def ConsultarPrestamosAdmin(self):
        if self.verificar_admin():
            print("Consulta de préstamos por parte del administrador:")
            for usuario in self.df_usuarios['Nombre'].unique():
                prestamos_usuario = self.df_prestamos[(self.df_prestamos['Usuario'] == usuario) & (self.df_prestamos['Devuelto'] == False)]
                if not prestamos_usuario.empty:
                    print(f"\nUsuario: {usuario}")
                    print(prestamos_usuario[['Código Libro', 'Fecha Préstamo', 'Fecha Entrega']])
        self.Menu()

    def MostrarLibros(self):
        """Muestra la información de los libros y estadísticas."""
        if self.verificar_admin():
            print("Información de los libros en la biblioteca:")
            for _, libro in self.df_libros.iterrows():
                codigo = libro['Código']
                cantidad_total = libro['Cantidad']
                cantidad_prestados = self.df_prestamos[self.df_prestamos['Código Libro'] == codigo].shape[0]
                cantidad_disponibles = cantidad_total - cantidad_prestados

                print(f"\nTítulo: {libro['Autor']} - Código: {codigo}")
                print(f"Cantidad total: {cantidad_total}")
                print(f"Libros prestados: {cantidad_prestados}")
                print(f"Libros disponibles: {cantidad_disponibles}")

        self.Menu()

    def Menu(self):
        while True:
            print("\nMenu:")
            print("\t1. Agregar Libro")
            print("\t2. Eliminar Libro")
            print("\t3. Agregar Usuario")
            print("\t4. Prestar Libro")
            print("\t5. Consultar Préstamos (Usuario)")
            print("\t6. Consultar Préstamos (Administrador)")
            print("\t7. Mostrar Información de Libros (Administrador)")
            print("\t8. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.AgregarLibro()
            elif opcion == '2':
                self.EliminarLibro()
            elif opcion == '3':
                self.AgregarUsuario()
            elif opcion == '4':
                self.PrestarLibro()
            elif opcion == '5':
                self.ConsultarPrestamosUsuario()
            elif opcion == '6':
                self.ConsultarPrestamosAdmin()
            elif opcion == '7':
                self.MostrarLibros()
            elif opcion == '8':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

while True:
    biblioteca = Biblioteca()