from django.db import models
import uuid
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class UUID(models.Model):
    """ Contain special number for each product """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

class Pizza(models.Model):
    
    def get_number(*args, **kwargs):
        """ Add next number to number field in admin panel """
        try:
            t=Pizza.objects.latest('number').number 
            t+=1
        except ObjectDoesNotExist:
            t=1
        return t

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ Create UUID object and assign to created model """

        if not self.pk:
            self.uuid=UUID.objects.create()
        super().save(*args, **kwargs)
    

    number=models.IntegerField(verbose_name=u'Numer', default=get_number, unique=True)
    name=models.CharField(verbose_name=u'Nazwa', max_length=30, unique=True)
    description=models.CharField(verbose_name=u'Opis', max_length=200)

    class Meta:
        verbose_name_plural=u'Pizze' 
  
    
class Pizza_SIZE(models.Model):
    
    SIZES=[ 
            ( 'GIGA' , 'Gigant'),
            ( 'MEGA' , 'Mega'),
            ( 'BIG' , 'Duża'), 
            ( 'SMALL' , 'Mała'), ]

    uuid=models.OneToOneField(UUID, related_name="uuid_Pizza", on_delete=models.CASCADE)  
    model=models.ForeignKey(Pizza, related_name='pizza_product', on_delete=models.CASCADE)  
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2)
    size=models.CharField(verbose_name=u'Rozmiar', max_length=20, choices=SIZES, default='SIZES.GIGA')
    sauce=models.IntegerField(verbose_name=u'Ilość sosów', default=1)

    def __str__(self):
        return self.model.name

    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.uuid=UUID.objects.create()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name=u'Rozmiar i cena'
        verbose_name_plural=u'Rozmiar i cena'
        unique_together=['model', 'size']


class Additives(models.Model):

    name=models.CharField(verbose_name=u'Dodatkowy składnik', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural=u'Dodatkowe składniki'
        verbose_name=u"Dodatkowy składnik"

    
class Additives_SIZE(models.Model):
    SIZES=[ 
            ( 'GIGA' , 'Gigant'),
            ( 'MEGA' , 'Mega'),
            ( 'BIG' , 'Duża'), 
            ( 'SMALL' , 'Mała'), ]

    uuid=models.OneToOneField(UUID, related_name="uuid_additives", on_delete=models.CASCADE)
    model=models.ForeignKey( Additives, related_name="additives_product", on_delete=models.CASCADE )
    size=models.CharField(verbose_name=u'Dodatek do porcji', max_length=20, choices=SIZES, default='SIZES.GIGA')
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.uuid=UUID.objects.create()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model.name

    class Meta:
        verbose_name=u'Rozmiar i cena'
        verbose_name_plural=u'Rozmiar i cena'
        unique_together=['model', 'size']


class Food(models.Model):

    MEAL=[
          ('CASSEROLES' ,'Zapiekanki'),
          ('PASTAS', 'Makarony'),
          ('DINNERS' ,'Dania obiadowe'),
          ('PANCAKES' ,'Naleśniki'),
          ('SOUPS' ,'Zupy'),
          ('SALADS' ,'Sałatki'), 
          ('SNACKS' ,'Przekąski'), 
          ('KEBAB' ,'Kebab'),
          ('FASTFOODS' ,'Fast food'),

        ]

    name=models.CharField(verbose_name=u'Nazwa', max_length=30, unique=True)
    category=models.CharField(verbose_name=u'Kategoria', max_length=20, choices= MEAL, default='MEAL.CASSEROLES')
    description=models.CharField(verbose_name=u'Opis', max_length=200, blank=True)
    change_meat=models.BooleanField(verbose_name=u"Wybór mięsa", default=False)
    change_chips=models.BooleanField(verbose_name=u"Wybór frytek", default=False)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Potrawa'
        verbose_name_plural=u'Potrawy'
     


class Food_SIZE(models.Model):
     
    SIZES=[ 
            ( 'BIG' , 'Duża'), 
            ( 'SMALL' , 'Mała'), ]

    uuid=models.OneToOneField(UUID, related_name="uuid_Food", on_delete=models.CASCADE)
    model=models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_product')
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2)
    size=models.CharField(verbose_name=u'Porcja', max_length=20, choices=SIZES, default='SIZES.BIG')
    sauce=models.IntegerField(verbose_name=u'Ilość sosów', default=0)

    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.uuid=UUID.objects.create()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.model.name

    class Meta:
        verbose_name=u'Rozmiar i cena'
        verbose_name_plural=u'Rozmiar i cena'
        unique_together=['model', 'size']

class Drink(models.Model):

    name=models.CharField(verbose_name=u'Nazwa', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Napój'
        verbose_name_plural=u'Napoje'


class Drink_SIZE(models.Model):

    uuid=models.OneToOneField(UUID, related_name="uuid_Drink", on_delete=models.CASCADE)
    model=models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='drink_product')
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2)
    capacity=models.CharField(verbose_name=u'Pojemność [ ml ]', max_length=5, default='500')

    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.uuid=UUID.objects.create()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model.name

    class Meta:
        verbose_name=u'Pojemność i cena'
        verbose_name_plural=u'Pojemność i cena'
        unique_together=['capacity', 'model']



class Sauce(models.Model):
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2, unique=True)

    def clean(self):
        """ Sauce model can contain only one object """

        if not self.pk and Sauce.objects.exists():
            raise ValidationError('Może istnieć tylko jeden obiekt klasy "Sos"')
        super().clean()

    def __str__(self):
        return "Sos_" + str(self.price) + "_zł"
        
    class Meta:
        verbose_name=u'Sos'
        verbose_name_plural=u'Sosy'

class Sauce_SIZE(models.Model):
 
    model=models.ForeignKey( Sauce, related_name="sauce_product", on_delete=models.CASCADE )
    name=models.CharField(verbose_name=u'Nazwa', max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Sos'
        verbose_name_plural=u'Sosy'

