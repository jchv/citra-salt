from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


error_messages = {
    'alphanum': _('Please use only alpha-numeric characters.')
}

help_text = {
    'username': _('An alpha-numeric identifier for an account.'),
    'password': _('A secret string of characters to authenticate with.'),
    'email': _('An e-mail address.'),
    'display_name': _('Name shown to other users.'),
    'personal_name': _('Optional; a user\'s personal name.'),
    'location': _('Optional; a user\'s location.'),
    'birth_date': _('Optional; a user\'s birthday.'),
    'gender': _('Optional; a phrase representing a user\'s gender.'),
    'pronouns': _('Pronouns to use to refer to the user.'),
    'is_staff': _('Designates whether the user can log into this admin site.'),
    'is_active': _('Designates whether this user should be treated as active. '
                   'Deselect this instead of deleting accounts.'),
}

username_validator = RegexValidator(regex='[a-zA-Z0-9]+', message=error_messages['alphanum'])


class User(AbstractBaseUser, PermissionsMixin):
    PRONOUNS_NEUTRAL = 'n'
    PRONOUNS_MALE = 'm'
    PRONOUNS_FEMALE = 'f'
    PRONOUNS_PLURAL = 'p'
    PRONOUNS_CHOICES = (
        (PRONOUNS_NEUTRAL, 'Neutral (they, them, their, theirs)'),
        (PRONOUNS_MALE, 'Male (he, him, his)'),
        (PRONOUNS_FEMALE, 'Female (she, her, hers)'),
    )

    username = models.CharField(_('username'), max_length=20, unique=True, validators=[username_validator], help_text=help_text['username'])
    email = models.EmailField(_('e-mail'), unique=True, help_text=help_text['email'])
    display_name = models.CharField(_('display name'), max_length=48, unique=True, help_text=help_text['display_name'])
    personal_name = models.CharField(_('personal name'), max_length=64, blank=True, help_text=help_text['personal_name'])
    location = models.CharField(_('location'), max_length=64, blank=True, help_text=help_text['location'])
    birth_date = models.DateField(_('birth date'), blank=True, null=True, help_text=help_text['birth_date'])
    gender = models.CharField(_('gender'), max_length=32, blank=True, help_text=help_text['gender'])
    pronouns = models.CharField(_('pronouns'), max_length=2, choices=PRONOUNS_CHOICES, help_text=help_text['pronouns'])
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=help_text['is_staff'])
    is_active = models.BooleanField(_('active'), default=True, help_text=help_text['is_active'])
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'display_name']

    objects = UserManager()

    def get_full_name(self):
        if self.personal_name != '':
            return self.personal_name
        else:
            return self.display_name

    def get_short_name(self):
        return self.display_name

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.username)

    # Gender pronouns are complicated. For example:
    #  - Her bike, his bike
    #  - Talk to her, talk to him
    # Do not replace this with something more naive.
    # Heavily skewed to romance languages.

    PR_NOMINATIVE = 'nominative'
    PR_OBLIQUE = 'oblique'
    PR_POS_DETERM = 'pos_determiner'
    PR_POSSESSIVE = 'pos_pronoun'

    PRONOUNS = {
        PRONOUNS_NEUTRAL: {
            PR_NOMINATIVE: _('neutral subject',               'they'),
            PR_OBLIQUE:    _('neutral object',                'them'),
            PR_POS_DETERM: _('neutral possessive determiner', 'their'),
            PR_POSSESSIVE: _('neutral possessive pronoun',    'theirs')
        },
        PRONOUNS_MALE: {
            PR_NOMINATIVE: _('male subject',               'he'),
            PR_OBLIQUE:    _('male object',                'him'),
            PR_POS_DETERM: _('male possessive determiner', 'his'),
            PR_POSSESSIVE: _('male possessive pronoun',    'his')
        },
        PRONOUNS_FEMALE: {
            PR_NOMINATIVE: _('female subject',               'she'),
            PR_OBLIQUE:    _('female object',                'her'),
            PR_POS_DETERM: _('female possessive determiner', 'her'),
            PR_POSSESSIVE: _('female possessive pronoun',    'hers')
        },
        PRONOUNS_PLURAL: {
            PR_NOMINATIVE: _('plural subject',               'they'),
            PR_OBLIQUE:    _('plural object',                'them'),
            PR_POS_DETERM: _('plural possessive determiner', 'their'),
            PR_POSSESSIVE: _('plural possessive pronoun',    'theirs')
        }
    }

    @classmethod
    def get_pronoun(cls, role, gender):
        return cls.PRONOUNS[gender][role]

    @property
    def nominative_pronoun(self):
        return self.get_pronoun(self.PR_NOMINATIVE, self.pronouns)
