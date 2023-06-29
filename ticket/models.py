import random
import string
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()

class Region(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=50, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Area(models.Model):
    title = models.CharField(max_length=50, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='areas', blank=True, null=True)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=50, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='areas', blank=True, null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Transaction(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title
    

# class Queue(models.Model):
#     ticket_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     ticket_id = models.PositiveIntegerField()
#     ticket = GenericForeignKey('ticket_type', 'ticket_id')


class Ticket(models.Model):

    executant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executans', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    region = models.ForeignKey(Region, verbose_name="Область", on_delete=models.CASCADE) # область
    area = models.ForeignKey(Area, help_text="", on_delete=models.CASCADE) # район
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # категория
    city = models.ForeignKey(City, on_delete=models.CASCADE) # город
    department = models.ForeignKey(Department, on_delete=models.CASCADE) #отделение
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transaction') # тип операции
    
    date = models.DateField()
    time = models.TimeField()

    # queue = GenericForeignKey('queue_type', 'queue_id')
    # queue_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    # queue_id = models.PositiveIntegerField(null=True)

    status = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=7, unique=True, blank=True)
    number = models.CharField(max_length=6, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.activation_code:
            random_digits = ''.join(random.choices(string.digits, k=5))
            city_first_letter = self.department.city.title[0]
            department_first_letter = self.department.title[0]
            activation_code = f'{city_first_letter}{department_first_letter}{random_digits}'

            self.activation_code = activation_code

        if not self.number:
            transaction_code = self.transaction.title[0].upper()
            last_ticket_number = Ticket.objects.order_by('-id').first()
            if last_ticket_number:
                last_number = int(last_ticket_number.number[2:])
            else:
                last_number = -1
            new_number = f'{transaction_code}{str(last_number + 1).zfill(3)}'
            self.number = new_number
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Билет: {self.number}, Владелец: {self.owner.email}, Операция: {self.transaction.title}"
    

class OffileTicket(models.Model):
    executant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offline_ticket', blank=True, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='offline_ticket') # тип операции
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # категория
    date = models.DateTimeField(auto_created=True, auto_now=True)
    number = models.CharField(max_length=6, unique=True, blank=True)
    status = models.BooleanField(default=True)

    # queue = GenericForeignKey('queue_type', 'queue_id')
    # queue_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    # queue_id = models.PositiveIntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.number:
            transaction_code = self.transaction.title[0].upper()
            last_ticket_number = OffileTicket.objects.order_by('-id').first()
        if last_ticket_number:
            last_number = int(last_ticket_number.number[2:])
        else:
            last_number = -1
        new_number = f'{transaction_code}{str(last_number + 1).zfill(3)}'
        self.number = new_number
        self.status = True
        
        super().save(*args, **kwargs)

    

    def __str__(self) -> str:
        return f"Билет: {self.number} Операция: {self.transaction.title}"



# @receiver(post_save, sender=Ticket)
# def add_ticket_to_queue(sender, instance, created, **kwargs):
#     if created:
#         # Создание объекта очереди
#         queue = Queue.objects.create()
#         # Привязка созданного билета к очереди
#         instance.queue_id = queue.id 
#         instance.queue = queue
#         instance.save()


# class TicketQueue(models.Model):
    
#     """queue simultaneously for offline and online tickets"""

#     operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queues')
#     online_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
#     offline_ticket = models.ForeignKey(OffileTicket, on_delete=models.CASCADE, null=True)
#     number = models.CharField(max_length=6)
#     is_served = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = ['online_ticket', 'offline_ticket', 'number']


