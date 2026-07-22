from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid 

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Super Admin', 'Super Admin'),
        ('Senior Manager', 'Senior Manager'),
        ('Junior Manager', 'Junior Manager'),
        ('Vendor', 'Vendor'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Vendor')
    is_active = models.BooleanField(default=True)
    is_frozen = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']
    
    class Meta:
        db_table = 'users'  
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            models.Index(fields=['role']),
        ]
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.email} - {self.role}"
    

    @property
    def is_super_admin(self):
        return self.role == 'Super Admin'
    
    @property
    def is_senior_manager(self):
        return self.role == 'Senior Manager'
    
    @property
    def is_junior_manager(self):
        return self.role == 'Junior Manager'
    
    @property
    def is_vendor(self):
        return self.role == 'Vendor'
    
    @property
    def is_manager(self):
        return self.role in ['Super Admin', 'Senior Manager', 'Junior Manager']
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    def freeze(self):
        self.is_frozen = True
        self.save(update_fields=['is_frozen'])
    
    def unfreeze(self):
        self.is_frozen = False
        self.save(update_fields=['is_frozen'])
    
    def activate(self):
        self.is_active = True
        self.save(update_fields=['is_active'])
    
    def deactivate(self):
        self.is_active = False
        self.save(update_fields=['is_active'])