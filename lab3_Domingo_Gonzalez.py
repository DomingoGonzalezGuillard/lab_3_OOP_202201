
#Lab 1
#nombre, autor, numero de serie, categoria
from collections import Counter
from abc import ABC, abstractmethod

from matplotlib.style import available
#Usar getters y setters
salir="no"
nuevo_libro='no'
#La biblioteca empieza con 2 libros
biblioteca={233:["dune","Frank Herbert","ciencia ficcion","Sin dueño","No arrendado","En biblioteca","En biblioteca","Disponible"],234:["el perfume","Patrick Suskind","realismo magico","Sin dueño","No arrendado","En biblioteca","En biblioteca","Disponible"]}
nombres=["dune","el perfume"]
bib=[]
#Al ingresar un libro nuevo, los datos de este se almacenan en una lista del diccionario con el siguiente orden:
        #[nombre,autor,genero,arrendador,fecha arriendo,fecha que debe ser entregado,fecha entrega] 
    
print("Esta biblioteca empieza con 2 libros:")
print("Dune y El perfume")

class Person():

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def checkout(self):
        pass

    

class Employee(Person):
    def get_type(self):
        return "Employee"

    def checkout(self,libro):
        pass

    def discount(self,price):
        return price*0.6
        

    

class Book():
    def __init__(self,name,author,genre,available,owner,rent_date,price,serie):
        self.name=name
        self.author=author
        self.genre=genre
        self.available=available
        self.owner=owner
        self.rent_date=rent_date
        self.price=price
        self.serie=serie
    def show_data(self):
        print("--Nombre: ",self.name,"--Autor: ",self.author,"--Serie: ",self.serie,"\n")
    

class BookCopy():
     def __init__(self):
        self.list=[]
        pass
     def add_copy(self,name):
         self.list.append(name)
     def remove_copy(self,name):
         self.list.remove(name)
     def copies(self):
         n=Counter(self.list)
         for a in n:
            print("==Nombre: ",a,"==Ejemplares: ",n[a])

       

class Customer(Person):

    def get_type(self):
        return "Customer"

    def checkout(self):
        self.book=input("Ingrese serie del libro para arrendar: ")
        return self.book
        pass

    def checkin(self,libro):
        pass

    pass

class Rental():
    def __init__(self,list):
        self.list=list


    def availables(self):
        print("===Disponibilidad===\n")
        for b in self.list:
            print("--Nombre: ",b.name,"--Disponible: ",b.available,"--Serie: ",b.serie,"--Precio: ",b.price)
            if b.available=="no":
                print("Devolucion esperada: ",b.rent_date,"--Arrendatario: ",b.owner,"\n")
            else:
                print("\n")

    def add_book(self,book):
        self.list.append(book)

    def remove_book(self,r_book):
        self.list.remove(r_book)
        
      

    def categorie_author(self,author):
        print(f"===Autor: {author}===")
        for b in self.list:
            if b.author==author:
                print("Nombre: ",b.name, "Serie: ",b.serie, "Disponibilidad: ",b.available,"\n")
    def categorie_genre(self,genre):
        print(f"===Genero: {genre}===")
        for b in self.list:
            if b.genre==genre:
                print("Nombre: ",b.name, "Serie: ",b.serie, "Disponibilidad: ",b.available,"\n")

    pass





rental=Rental(bib) #Creamos biblioteca inicial
b233=Book("dune","Frank Herbert","ciencia ficcion","si","nadie","disponible",500,"233") #Creamos los primeros libros con su serie
b234=Book("el perfume","Patrick Suskind","realismo magico","si","nadie","disponible",600,"234")

rental.add_book(b233) #Anadimos los primeros libros
rental.add_book(b234)


copies=BookCopy()
copies.add_copy(b233.name)
copies.add_copy(b234.name)  #Agregamos los nombres de los libros a la clase copy

while salir!="si":

    #Menu
    print("(1) Inventario")
    print("(2) Anadir libro")
    print("(3) Disponibilidad (Ver numero serie y precio) ")
    print("(4) Arrendar")
    print("(5) Devolver libro")
    print("(6) Quitar libro")
    print("(7) Categorias")
    print("(8) Salir")
    menu=input("¿Qué desea hacer?\n")
   # menu=1

    if menu=="1":
        copies.copies()
    #    for b in rental.list:
    #         print("--Nombre: ",b.name,"--Ejemplares ",copies.copies(b.name))
        
    if menu=="2":
        a=1
        name=input("Ingrese nombre del libro: ")
        author=input("Ingrese autor del libro: ")
        genre=input("Ingrese genero del libro: ")
        price=int(input("Ingrese valor del libro: "))
        serie=input("Ingrese serie del libro: ")
        for b in rental.list:
            if b.serie==serie:
                print("No se pueden repetir las series de los libros")
                print(f"Serie del libro {b.name}, ya existente: {b.serie}")
                a=0
        if a==1:
            book=Book(name,author,genre,"si","nadie","disponible",price,serie)
            rental.add_book(book)
            copies.add_copy(book.name) #Guardamos la copia
            print("Libro anadido\n")

    if menu=="3":
        rental.availables()
        pass
    if menu=="4":
        
        customer=Customer()
        book=customer.checkout()
        for b in rental.list:
            if book== b.serie:
                if b.available=="si":
                    name=input("Ingrese nombre arrendatario: ")
                    date1=input("Ingrese fecha devolucion (dd/mm): ")
                    b.available="no"
                    b.owner=name
                    b.rent_date=date1
                    print(f"Se arrendo exitosamente {b.name} \n")
                    
                else:
                    print(f"Libro {b.name} ya arrendado")

                

        
    if menu=="5":
        serie=input("Indique serie de libro a devolver: ")
        for b in rental.list:
            if book== b.serie:
                if b.available=="no":
                    date=input("Ingrese fecha de hoy (dd/mm): ")
                    b.available="si"
                    days=float(input("Indique por cuantos dias lo arrendo: "))
                    who=input("Seleccione segun corresponda: \n(1)Cliente\n(2)Empleado\n")
                    if who=="1":
                        print("Total a pagar: ",b.price*days)
                        b.owner="nadie"
                        print("Fecha esperada de devolucion: ",b.rent_date)
                        print("Fecha de devolucion: ",date)
                        b.rent_date="Disponible"
                        print(f"Libro {b.name} devuelto")
                   
                    elif who=="2":
                        employee=Employee()
                        print("Total a pagar: ",employee.discount(float(b.price*days)))
                        b.owner="nadie"
                        print("Fecha esperada de devolucion: ",b.rent_date)
                        print("Fecha de devolucion: ",date)
                        b.rent_date="Disponible"
                        print(f"Libro {b.name} devuelto")
                    else:
                        print("Error de typeo")
                        b.available="no"
                        break
                else:
                    print("El libro esta en la biblioteca")
                            
        pass
    if menu=="6":
        r_book=input("Indique serie de libro que quiere remover: ")
        for b in rental.list:
            if b.serie==r_book:
                copies.remove_copy(b.name)
                rental.remove_book(b)
                print(f"Libro {b.name} removido")
                
       
       
        
        
    if menu=="7":
        cat=input("Ingrese:\n (1) Genero\n (2) Autor\n ")
        if cat == "1":
            genre=input("Ingrese genero: ")
            rental.categorie_genre(genre)
        elif cat == "2":
            author=input("Ingrese autor: ")
            rental.categorie_author(author)
        else:
            print("Error de typeo")
    if menu=="8":
        salir="si"
    




