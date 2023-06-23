import random
import string
from django.db import models
from django.contrib.auth import get_user_model

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
    
# class OfflineTicket(models.Model):
#     terminal = models
#     pass 

class Ticket(models.Model):

    # transaction_list = [('money_transfers', 'Money transfers'), ('bank_cards','Bank cards'), ('account_maintenance','Account maintenance')]
    # status_list = [('not_active', 'Not active'), ('active', 'Active')]

    executant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executans', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE) # область
    area = models.ForeignKey(Area, on_delete=models.CASCADE) # район
    city = models.ForeignKey(City, on_delete=models.CASCADE) # город
    department = models.ForeignKey(Department, on_delete=models.CASCADE) #отделение
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transaction') # тип операции
    
    date = models.DateField()
    time = models.TimeField()

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