from django.db import models



class Domicile(models.Model):
    nom = models.CharField(max_length=255)
    cote = models.FloatField()
    image = models.ImageField(default='eqp.jpg', upload_to='equipe_pics')

    def __str__(self):
        return self.nom


class Exterieure(models.Model):
    nom = models.CharField(max_length=255)
    cote = models.FloatField()
    image = models.ImageField(default='eqp.jpg', upload_to='equipe_pics')

    def __str__(self):
        return self.nom


class Champ(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Battle(models.Model):
    dom = models.ForeignKey(Domicile, on_delete=models.CASCADE)
    ext = models.ForeignKey(Exterieure, on_delete=models.CASCADE)
    cham = models.ForeignKey(Champ, on_delete=models.CASCADE)
    dom_but = models.IntegerField()
    ext_but = models.IntegerField()





