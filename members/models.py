from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    sex = models.CharField(_("Sex"), max_length=50, choices=(('male', 'Male'), ('female', 'Female')))
    

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Member_detail", kwargs={"pk": self.pk})

