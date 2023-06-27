from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Window(models.Model):
    number = models.CharField(max_length=50)
    operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='window_operator')
    is_available = models.BooleanField(default=True)
    current_ticket = models.OneToOneField('ticket.Ticket', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.operator} - {self.current_ticket}'

class Queue(models.Model):
    operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Queue_operator')
    ticket = models.ForeignKey('ticket.Ticket', on_delete=models.CASCADE, related_name='Queue_ticket')
    is_served = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Очередь: {self.id}, Билет: {self.ticket.number}, Оператор: {self.operator.username}"