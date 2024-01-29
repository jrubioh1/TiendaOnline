from Tienda.models import Producto
class Carro:

    def __init__(self, request):

        self.request=request
        self.session=request.session
        self.carro={}
        if not self.session.get('carro'):
             self.carro=self.session["carro"]={}
        else:
            self.carro=self.session.get("carro")

    

        
           
        

    def agregar(self, producto):
            print('principio')

            if (str(producto.id) not in self.carro.keys()):
                print('1.1')
                self.carro[str(producto.id)]={

                    'producto_id': producto.id,
                    "nombre":producto.nombre,
                    'precio': str(producto.precio),
                    'cantidad': 1,
                    'imagen':producto.imagen.url,
                    
                    }
                
                
            else:
                
                for key, value in self.carro.items():
                  
                    if key==str(producto.id):
                       
                        value['cantidad']+=1
                        value['precio']= float(value['precio'])+ producto.precio
                        break
                
                    
            self.guardar_carro()


    def guardar_carro(self):

        self.session['carro']= self.carro
        self.session.modified= True
    
    def eliminar(self, producto):

        producto_id=str(producto.id)

        if producto_id in self.carro:

            del self.carro[producto_id]
            self.guardar_carro()
    
    def restar_producto(self, producto):

        for key, value in self.carro.items():
                if key==str(producto.id):
                    value['cantidad']-=1
                    if value['cantidad']<1:
                         self.eliminar( Producto.objects.get(id=value['producto_id']))
                    else:
                        value['precio']= float(value['precio'])-producto.precio
                    break
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.carro = self.session['carro']={}
        self.session.modified= True