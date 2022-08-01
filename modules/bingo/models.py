from uuid import uuid4

from django.db.models import CharField, UUIDField

from core.shared.models import BaseModel


class User(BaseModel):
    id = UUIDField(primary_key=True, default=uuid4)
    first_name = CharField(max_length=256, null=False, unique=False)
