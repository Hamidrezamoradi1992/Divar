from typing import Any, Callable, Type
from django.core import mail
from django.core import validators
from django.conf import settings
from django.template.loader import render_to_string, get_template


class EmailService:
    __slots__ = ('subject', 'context', 'template_name', 'from_emil', 'to_email', 'html_content')

    @staticmethod
    def _field_validation(field_type: Type,
                          value: Any,
                          default_value: Any = None,
                          validator: Callable = None, ) -> Any:
        assert not validator or callable(validator), 'Validator must be callable!'
        assert value or default_value is not None, 'default_value must be None !'
        value = value or default_value
        assert isinstance(value, field_type), 'value must be {}!'.format(field_type)
        assert not validator or validator(value), 'Validator Error'
        return value

    def __init__(self,
                 subject: str,
                 template_name: str,
                 to_email: list,
                 from_emil: str = settings.DEFAULT_FROM_EMAIL,
                 context: dict | None = None) -> None:
        self.context = self._field_validation(dict, context, default_value={})
        self.template_name = self._field_validation(str, template_name, validator=get_template)
        self.from_emil = self._field_validation(str, from_emil,
                                                validator=lambda v: validators.EmailValidator(v) or True)
        self.to_email = self._field_validation(str, to_email, validator=lambda v: validators.EmailValidator(v) or True)
        self.subject = self.context.get('subject', subject)
        self.html_content: str = render_to_string(self.template_name, self.context)

    def send(self, ) -> None:
            mil = mail.EmailMultiAlternatives(subject=self.subject, body=self.html_content, from_email=self.from_emil,
                                              to=[self.to_email])
            mil.attach_alternative(self.html_content, 'text/html')
            mil.send()
            del self

    def __str__(self):
        return self.subject
