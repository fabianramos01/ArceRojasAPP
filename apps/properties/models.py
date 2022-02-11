from django.db.models import Model, CharField, PositiveSmallIntegerField, ManyToManyField

from django.core.validators import MinLengthValidator


class Owner(Model):
    identification = CharField(
        'Identificación',
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(10)]
    )

    name = CharField(
        'Nombre',
        max_length=250,
        null=True,
        blank=True
    )

    PERSON = 1
    COMPANY = 2
    TYPES = (
        (PERSON, 'Persona'),
        (COMPANY, 'Empresa'),
    )

    type = PositiveSmallIntegerField(
        'Tipo',
        choices=TYPES,
        default=PERSON,
    )

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

    def __str__(self):
        return self.name


class Property(Model):
    registration_number = CharField(
        'Número de matricula',
        max_length=30,
        unique=True
    )

    cadastral_id = CharField(
        'Cédula catastral',
        max_length=30
    )

    address = CharField(
        'Dirección',
        max_length=250,
        null=True,
        blank=True
    )

    name = CharField(
        'Nombre',
        max_length=250,
        null=True,
        blank=True
    )

    URBAN = 1
    RURAL = 2
    TYPES = (
        (URBAN, 'Urbano'),
        (RURAL, 'Rural'),
    )

    type = PositiveSmallIntegerField(
        'Tipo',
        choices=TYPES,
        default=URBAN,
    )

    owners = ManyToManyField(
        Owner
    )

    class Meta:
        verbose_name = 'Predio'
        verbose_name_plural = 'Predios'

    def __str__(self):
        return self.registration_number
