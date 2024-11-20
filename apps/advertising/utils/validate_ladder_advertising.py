from datetime import timedelta
import random
from typing import List

from django.utils import timezone

from apps.advertising.models import Advertising


class ValidateLadderAdvertising:
    __slots__ = ('queryset', 'create_at', 'delete_at', 'ladder_count', 'category_id')

    _LADDER_ADVERTISING_MODEL = {}
    _LADDER_INSTANCE = []

    def __new__(cls, queryset, *args, **kwargs):
        if queryset.id not in cls._LADDER_ADVERTISING_MODEL:
            instance = super().__new__(cls)
            cls._LADDER_ADVERTISING_MODEL[queryset.id] = instance
            return instance
        return cls._LADDER_ADVERTISING_MODEL[queryset.id]

    def __init__(self, queryset, category):
        if not hasattr(self, 'queryset'):
            self.queryset = queryset
            self.category_id = category
            self.create_at = timezone.now()
            self.delete_at = timezone.now() + timedelta(hours=24)
            self.ladder_count = 1
            self.__class__._LADDER_INSTANCE.append(self)
            print("hamid")

    @staticmethod
    def _random_item():
        try:
            random_items = random.sample(ValidateLadderAdvertising._LADDER_INSTANCE, 3)
            return random_items
        except ValueError:
            return ValidateLadderAdvertising._LADDER_INSTANCE.copy()

    @staticmethod
    def get_ladder_advertising(categories_id:list=None):
        if ValidateLadderAdvertising._LADDER_INSTANCE:
            random_items = ValidateLadderAdvertising._random_item()
            if categories_id:
                random_items = [i for i in random_items if i.category_id in categories_id]
            for item in random_items:
                if item.ladder_count > 3:
                    random_items.remove(item)
                    advertise = Advertising.objects.get(id=item.queryset.id)
                    advertise.ladder = False
                    advertise.save()
                    ValidateLadderAdvertising._LADDER_INSTANCE.remove(item)
                    ValidateLadderAdvertising._LADDER_ADVERTISING_MODEL.pop(item.queryset.id)
            if len(random_items) < 3:
                if len(ValidateLadderAdvertising._LADDER_INSTANCE) >= 3:
                    return ValidateLadderAdvertising.get_ladder_advertising()

            for item in random_items:
                item.ladder_count += 1
            return [i.queryset for i in random_items]
