class Muebles():
    def __init__ (self,tmaterial,cant,precio,color):
         self.__material=tmaterial
         self.__cantidad=cant
         self.__precio=precio
         self.__color=color 
         self.__mesa=False
    def set_material(self,tmaterial):
        self.__material=tmaterial
    def get_material(self):
        return self.__material
    def set_cantidad(self,cant):
         self.__cantidad=cant
    def get_cantidad(self):
        return self.__cantidad
    def set_precio(self,precio):
        self.__precio=precio
    def get_precio(self):
        return self.__precio
    def set_color(self,color):
        self.__color=color 
    def get_color(self):
        return self.__color
    def mesa(self):
        self.__mesa=True
class Mesa(Muebles):
    def __init__(self,npatas,tmaterial,cant,precio,color ):
        self_patas=npatas
        super().__init__(tmaterial,cant,precio,color)
    def set_patas (self,npatas):
        self.__patas=npatas
    def get_patas (self):
        return self.__patas
if __name__=="__main__":
    muebles=[]
    pregunta=input("Desea hacer un pedido de un mueble:")
    while pregunta.lower()=="si":
        material=input("De que material es tu mueble:")
        cantidad=input("Cuantos muebles quieres:")
        precio=input("Cuanto desea gastarse:")
        color=input("De que color es tu mueble:")
        mesa=input("Que quieres pedir una mesa o un mueble ")
        if mesa.lower()=="mesa":
            patas=input("Cuantas patas tiene su mesa:")
        mueble=Muebles
        muebles.append(mueble)
        pregunta=input("Quieres añadir mas muebles o mesas:")
    for x in range(0,len(mueble)):
        if 
        print(mueble[x].get_material())
        print(mueble[x].get_cantidad())
        print(mueble[x].get_precio())
        print(mueble[x].get_color())
        print(mueble[x].get_patas())





    
