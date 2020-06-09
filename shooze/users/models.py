from django.contrib.auth.models import AbstractUser
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    OneToOneField,
    Q,
    SlugField,
    CASCADE,
    SET_NULL,
    URLField
)
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)

# from django_countries.fields import CountryField
# from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    terms           = BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
