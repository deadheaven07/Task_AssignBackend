import random
import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as needed
class Game(models.Model):
    string = models.CharField(max_length=255)
    game_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def append_char(self, char):
        self.string += char
        self.string += str(random.randint(0, 9))
        self.save()

    def is_palindrome(self):
        return self.string == self.string[::-1]
