from django.db import models
    
class Stock(models.Model):
    category = (
        ('equipments', 'equipments'),
        ('materials', 'materials'),
        ('tools', 'tools')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=50, choices=category, default='materials')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1000)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name