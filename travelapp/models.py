from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    usertype=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username
    
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()
    reg_date=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    compnay_name=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()
    proof=models.FileField(upload_to="company_proof/")
    reg_date=models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)   

class Accomodation(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100, null=True)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()
    proof=models.FileField(upload_to="accomodation_proof/")
    reg_date=models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)   

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="product_images/",null=True)
    weather=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,default='Pending',null=True)

    def __str__(self):
        return f"{self.name} - {self.supplier.compnay_name}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100, default='Pending')
    total_price = models.FloatField()
    cart_date = models.DateTimeField(auto_now_add=True)
    payment_date=models.DateTimeField(null=True)

    def __str__(self):
        return f"Booking by {self.user.name} for {self.product.name}"
    

class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()
    comments = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Booking ID {self.booking.id} - Rating: {self.rating}"
    

class Rooms(models.Model):
    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, null=True)
    bed_capacity = models.IntegerField()
    description = models.TextField()
    room_type=models.CharField(max_length=100)
    rate = models.FloatField()
    added_date = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,default='Available',null=True)

    def __str__(self):
        return f"{self.room_type} - {self.accomodation.name}"
    
class Roomimage(models.Model):
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    image=models.ImageField(null=True)

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    booking_date = models.DateField()
    to_date = models.DateField(null=True)
    description = models.TextField()
    status = models.CharField(max_length=100, default='Pending')
    booking_made_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room Booking by {self.user.name} for {self.room.room_type}"    