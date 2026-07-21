from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
class User(AbstractUser):

    ROLE_CHOICES=[
        ('SUPER_ADMIN','Super Admin'),
        ('SENIOR_MANAGER','Senior Manager'),
        ('JUNIOR_MANAGER','Junior Manager'),
        ('VENDOR','Vendor'),
    ]
    id =models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15,unique=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='VENDOR')
    is_active=models.BooleanField(default=True)
    is_frozen=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    last_login_ip=models.GenericIPAddressField(null=True,blank=True)
    last_login_device=models.CharField(max_length=255,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profiles/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','phone']
    
    class Meta:
        db_table='users'
        ordering=['-created_at']
        indexes=[
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            models.Index(fields=['role']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return f"{self.email}-{self.get_role_display()}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    @property
    def is_super_admin(self):
        return self.role=='SUPER_ADMIN'
    
    @property
    def is_senior_manager(self):
        return self.role=='SENIOR_MANAGER'
    
    @property
    def is_junior_manager(self):
        return self.role=='JUNIOR_MANAGER'
    
    @property
    def is_vendor(self):
        return self.role=='VENDOR'
    
    @property
    def is_manager(self):
        return self.role in ['SENIOR_MANAGER','JUNIOR_MANAGER']