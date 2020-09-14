from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    marital_status = models.CharField(
        choices=(
            ('Single', 'Single'),
            ('Married', 'Married'),
            ('Divorced', 'Divorced'),
            ('Widowed', 'Widowed'),
        ),
        max_length=20, null=True, blank=True
    )
    religion = models.CharField(
        choices=(
            ('Agnostic', 'Agnostic'),
            ('Atheist', 'Atheist'),
            ('Buddhism', 'Buddhism'),
            ('Christianity', 'Christianity'),
            ('Hinduism', 'Hinduism'),
            ('Islam', 'Islam'),
            ('Judaism', 'Judaism'),
            ('Nonreligious', 'Non-religious'),
            ('Rastafarianism', 'Rastafarianism'),
            ('Other', 'Other')
        ),
        max_length=20, null=True, blank=True
    )
    gender = models.CharField(
        choices=(('Male', 'Male'), ('Female', 'Female')),
        max_length=6, null=True, blank=False
    )

    def __str__(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance).save()
