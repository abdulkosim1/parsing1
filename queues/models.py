from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class Operator(models.Model):
    number = models.IntegerField()
    operator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.operator} - {self.number}'

class Window(models.Model):
    number = models.CharField(max_length=50)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='window_operator')
    is_available = models.BooleanField(default=True)
    current_ticket = models.OneToOneField('ticket.Ticket', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.operator} - {self.current_ticket}'

