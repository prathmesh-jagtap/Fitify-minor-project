from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Fitify.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(unique=True, max_length=254)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
