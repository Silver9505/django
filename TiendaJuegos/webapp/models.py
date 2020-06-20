from django.db import models

class Juego(models.Model):
    jue_id = models.CharField(primary_key=True, max_length=10)
    jue_titulo = models.CharField(max_length=50)
    jue_desarrollador = models.CharField(max_length=50)
    jue_editor = models.CharField(max_length=50)
    jue_franquicia = models.CharField(max_length=50)
    jue_precio = models.DecimalField(max_digits=50, decimal_places=2)
    

class Genero(models.Model):
    gen_id = models.CharField(primary_key=True, max_length=10)
    gen_nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.gen_nombre

class Genero_Juego(models.Model):
    gxj_gen = models.ForeignKey(Genero, on_delete=models.PROTECT)
    gxj_jue = models.ForeignKey(Juego, on_delete=models.PROTECT)

class Idioma(models.Model):
    idi_id = models.CharField(primary_key=True, max_length=10)
    idi_nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.idi_nombre

class Idioma_Juego(models.Model):
    ixj_idi = models.ForeignKey(Idioma, on_delete=models.PROTECT)
    ixj_jue = models.ForeignKey(Juego, on_delete=models.PROTECT)

class Cliente(models.Model):
    cli_id = models.CharField(primary_key=True, max_length=20)
    cli_nom = models.CharField(max_length=30, null=True)
    cli_ape = models.CharField(max_length=150, null=True)
    cli_email = models.CharField(max_length=254)
    cli_pais = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.cli_nom

class Modalidad(models.Model):
    mod_id = models.CharField(primary_key=True, max_length=10)
    mod_nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.mod_nombre

class Mod_Juego(models.Model):
    mxj_idi = models.ForeignKey(Modalidad, on_delete=models.PROTECT)
    mxj_jue = models.ForeignKey(Juego, on_delete=models.PROTECT)

class Pago(models.Model):
    pag_id = models.CharField(primary_key=True, max_length=10)
    pag_tipo = models.CharField(max_length=20)
    pag_permitido = models.BooleanField()


class Orden(models.Model):
    ord_id = models.CharField(primary_key=True, max_length=10)
    ord_cli_id = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ord_pag_id = models.ForeignKey(Pago, on_delete=models.PROTECT)
    ord_fecha_ord = models.DateField(auto_now=True)
    ord_fecha_pago = models.DateField(auto_now=False)

class Detalles_orden(models.Model):
    dxo_id = models.CharField(primary_key=True, max_length=10)
    dxo_jue_id = models.ForeignKey(Juego, on_delete=models.PROTECT)
    dxo_ord_id = models.ForeignKey(Orden, on_delete=models.PROTECT)
    


