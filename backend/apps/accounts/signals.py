from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_related_profiles(sender, instance, created, **kwargs):
    """
    When a new user is created:
    1. Create VendorExtra ONLY if role is Vendor
    2. Send welcome email to ALL users
    """
    if created:
        if instance.role=='Vendor':
            try:
                from apps.vendors.models import VendorExtra
                VendorExtra.objects.create(user=instance)
                print(f"VendorExtra created for {instance.email}")
            except ImportError:
                print("VendorExtra model not found (vendors app not created yet)")
            except Exception as e:
                print(f"Error creating VendorExtra: {e}")
        try:
            full_name = instance.full_name
            display_name = full_name or instance.username
            subject = 'Welcome to SCM Pro'
            message = f"""
            Dear {display_name},
            Welcome to SCM Pro - Enterprise Supply Chain Management System!
            Your account has been created successfully.
            ──────────────────────────────────
            Account Details:
            Email: {instance.email}
            Role: {instance.role}
            ──────────────────────────────────
            Please login to access the system:
            Login URL: http://www.upayscm.com
            Thank you for joining SCM Pro!
            Best regards,
            SCM Pro Team
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL or 'noreply@upayscm.com',
                [instance.email],
                fail_silently=True,
            )
            print(f"Welcome email sent to {instance.email}")
        except Exception as e:
            print(f"Error sending email: {e}")