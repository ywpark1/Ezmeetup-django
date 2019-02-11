from django.db import models
from django.contrib.auth.models \
    import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, phone_number,
                    password=None, **extra_fields):

        """ Creates and saves a new user """
        if not email:
            raise ValueError('Users must have an email address.')

        if not first_name or not last_name:
            raise ValueError('Users must have first name and last name.')

        if not phone_number:
            raise ValueError('Users must have a phone number.')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Creates and saves a new superuser """

        user = self.create_user(
            email,
            'Admin_first',
            'admin_last',
            '000-000-0000',
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_logged_in = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
