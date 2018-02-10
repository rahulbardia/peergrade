from mongoengine import *
from peergrade.settings import DBNAME

connect(DBNAME)

# Create your models here.


class Notification(Document):
    sender = StringField(max_length=64, required=True)
    content = StringField(max_length=500, required=True)
    created_at = DateTimeField(required=True)
    active = BooleanField()
    request_moderation = BooleanField(default=False)

