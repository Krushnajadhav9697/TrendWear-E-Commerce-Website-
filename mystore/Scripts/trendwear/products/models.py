from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='category'
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    SECTION_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('home','home'),
        ('Kids', 'Kids'),
        ('Baby', 'Baby'),
        ('Sports', 'Sports'),
        
    ]
    image=models.ImageField(upload_to='image',default='')
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=SECTION_CHOICES,default='men')
    

    class Meta:
        db_table='product'
    
    def __str__(self):
        return self.name