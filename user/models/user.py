from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, Group, Permission


class CustomUserManager(UserManager):
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_moderator", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField("first-name",max_length=50)
    last_name = models.CharField("last-name",max_length=50)
    nickname = models.CharField("nickname", max_length=50, unique=True)
    email = models.EmailField("email",max_length=254, unique=True)
    password = models.CharField("password",max_length=250)
    avatar = models.ImageField("avatar", upload_to='upload/images/users/avatar/')
    
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    
    is_active = models.BooleanField("is_active", default=True)
    is_superuser = models.BooleanField("is_superuser", default=False)
    is_staff = models.BooleanField("is_staff", default=False)
    is_moderator = models.BooleanField("is_moderator", default=False)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def save(self, *args, **kwargs) -> None:
        self.nickname = self.email[:self.email.index("@")]
        return super().save(*args, **kwargs)   

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
