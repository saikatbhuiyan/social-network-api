from django.db import models

from core.models import TimestampedModel

class Profile(TimestampedModel):
  # There is an inherent relationship between the Profile and
  # User models. By creating a one-to-one relationship between the two, we
  # are formalizing this relationship. Every user will have one -- and only
  # one -- related Profile model.
  user = models.OneToOneField(
    'users.User', on_delete=models.CASCADE
  )

  bio = models.TextField(blank=True)
  # In addition to the `bio` field, each user may have a profile image or
  # avatar. This field is not required and it may be blank.
  image = models.URLField(blank=True)
  # A timestamp representing when this object was created.
 
  def __str__(self):
    return self.user.username
