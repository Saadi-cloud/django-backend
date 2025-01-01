from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.name
    

# One-to-One Relationship: Product has a single unique detail.
class ProductDetail(models.Model):
    description = models.TextField()
    specifications = models.TextField()

    def __str__(self):
        return f"Detail: {self.description[:50]}"

# Product model with One-to-One, One-to-Many, and Many-to-Many relationships.
class Productwithmodel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_detail = models.OneToOneField(
        ProductDetail, on_delete=models.CASCADE, related_name="product"
    )

    def __str__(self):
        return self.name

# One-to-Many Relationship: A category can have multiple products.
class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return self.name

# Many-to-Many Relationship: Products can have multiple tags, and tags can belong to multiple products.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name="tags")

    def __str__(self):
        return self.name
    



class ChaiVarity (models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELACHI'),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.
  now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
  desacription = models.TextField(default='')

  def __str__(self):
        return self.name


# One to Many
class ChaiReview (models.Model):
  chai = models.ForeignKey(ChaiVarity, on_delete=models.
  CASCADE, related_name='reviews')
  user= models.ForeignKey(User, on_delete=models.
  CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField (default=timezone.now)
  def __str__(self):
    return f'{self.user.username} review for {self.chai.
    name}'
  

  # Many to many
class Store (models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVarity,
  related_name='stores')
  def __str__(self):
    return self.name
  

# One to one
class ChaiCertificate (models.Model):
  chai = models.OneToOneField(ChaiVarity,
  on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField (default=timezone.now)
  valid_untill = models.DateTimeField()
  def __str__(self):
    return f'Certificate for {self.chai}'
  
