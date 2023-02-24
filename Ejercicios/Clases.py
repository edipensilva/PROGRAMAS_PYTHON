
class Lenguaje:
    def __init__(self,nombre:str,año:int):
        self.nombre = nombre
        self.año = año

    #método descripción
    def descripcion(self):
        print('%s fue creado en %s' % (self.nombre,self.año))

javascript = Lenguaje('JavaScript',1995)
javascript.descripcion()


    
