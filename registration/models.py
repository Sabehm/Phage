from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, given_name, first_surname, second_surname, phone_number, password=None):
        if not username:
            raise ValueError('Nombre de Usuario obligatorio.')
        if not email:
            raise ValueError('Correo Electrónico obligatorio.')
        if not given_name:
            raise ValueError('Nombre obligatorio')
        if not first_surname:
            raise ValueError('Apellido Paterno obligatorio')
        if not phone_number:
            raise ValueError('Número Telefónico obligatorio')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            given_name = given_name,
            first_surname = first_surname,
            second_surname = second_surname,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, given_name, first_surname, second_surname, phone_number, password):
        user = self.create_user(
            username = username,
            password = password,
            email = email,
            given_name = given_name,
            first_surname = first_surname,
            second_surname = second_surname,
            phone_number = phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    username        = models.CharField(verbose_name='Usuario', max_length=20, primary_key=True)
    email           = models.EmailField(verbose_name='Correo Electrónico', max_length=255, unique=True)
    given_name      = models.CharField(verbose_name='Nombre(s)', max_length=100)
    first_surname   = models.CharField(verbose_name='Apellido Paterno', max_length=50)
    second_surname  = models.CharField(verbose_name='Apellido Materno', max_length=50, null=True, blank=True)
    phone_number    = models.IntegerField(verbose_name='Número Telefónico')
    date_joined     = models.DateTimeField(verbose_name='Se Unió', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='Último inicio de Sesión', auto_now=True)
    is_admin        = models.BooleanField(verbose_name='Administrador', default=False)
    is_active       = models.BooleanField(verbose_name='Activo', default=True)
    is_staff        = models.BooleanField(verbose_name='Staff', default=False)
    is_superuser    = models.BooleanField(verbose_name='Superusuario', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'given_name', 'first_surname', 'second_surname', 'phone_number']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def get_full_name(self):
        full_name = '%s %s %s' % (self.given_name, self.first_surname, self.second_surname)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.username)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True










'''from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, givenName, firstSurname, secondSurname, phoneNumber, password=None, commit=True):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Nombre de usuario obligatorio')
        if not email:
            raise ValueError('Correo electrónico obligatorio')
        if not givenName:
            raise ValueError('Nombre obligatorio')
        if not firstSurname:
            raise ValueError('Apellido paterno obligatorio')
        if not secondSurname:
            raise ValueError('Apellido materno obligatorio')
        if not phoneNumber:
            raise ValueError('Número telefónico obligatorio')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            givenName=givenName,
            firstSurname=firstSurname,
            secondSurname=secondSurname,
            phoneNumber=phoneNumber,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, givenName, firstSurname, secondSurname, phoneNumber, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
            email=email,
            givenName=givenName,
            firstSurname=firstSurname,
            secondSurname=secondSurname,
            phoneNumber=phoneNumber,
            commit=False,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='Usuario', max_length=20, primary_key=True)
    email = models.EmailField(verbose_name='Correo Electrónico', max_length=255, unique=True)
    givenName = models.CharField(verbose_name='Nombre(s)', max_length=100)
    firstSurname = models.CharField(verbose_name='Apellido Paterno', max_length=50)
    secondSurname = models.CharField(verbose_name='Apellido Materno', max_length=50)
    phoneNumber = models.IntegerField(verbose_name='Número Telefónico', max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'givenName', 'firstSurname', 'secondSurname', 'phoneNumber']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin'''
