from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(email=email, username=username, **extra_fields)
        
        # Save the password as plain text (Do NOT use set_password for plain text)
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, username, **extra_fields)


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Returns True if the user has the specified permission."
        return True

    def has_module_perms(self, app_label):
        "Returns True if the user has permissions to view the app `app_label`."
        return True

# Product Model with unique identifier for each product
class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Unique product ID
    user_email = models.EmailField()  # Storing email directly
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) 
    vehicle_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    manufacturer_name = models.CharField(max_length=200)
    product_condition = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_video = models.FileField(upload_to='product_videos/', blank=True, null=True)
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_name


# Chat Model
class Chat(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_chats", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_chats", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Request Model to send a request for a product
class Request(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="requested_products", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.product.vehicle_name} by {self.requester.username}"
