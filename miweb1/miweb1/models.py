from django.db import models


class Usuarios(models.Model):
    rut= models.CharField(max_length= 13, primary_key=True)
    nombre= models.CharField(max_length= 50, null=False)
    direccion= models.CharField(max_length= 50, null=False)
    usuario= models.CharField(max_length= 15, null=False)
    contrasena= models.CharField(max_length= 15,null=False) 

    def __str__(self):
        return self.rut

class Residuos(models.Model):
    idr= models.CharField(max_length= 13, primary_key=True)
    nombre= models.CharField(max_length= 13, null=False)
    puntaje= models.CharField(max_length= 13, null=False)
    

    def __str__(self):
        return self.idr
    
class Registroresiduos(models.Model):
    idr = models.ForeignKey(Residuos, on_delete=models.CASCADE,default='DEFAULT VALUE')
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,default='DEFAULT VALUE')
    kilos= models.CharField(max_length= 13)
    fecha= models.CharField(max_length= 13)
    puntosobtenidos= models.CharField(max_length=13)
  
    

    def __str__(self):
        return self.idr_id