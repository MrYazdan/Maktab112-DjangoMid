import threading
from typing import Any, Callable, Type

from django.core import mail, validators
from django.conf import settings
from django.template.loader import render_to_string, get_template


class MailProvider:

    @staticmethod
    def _field_initializer(
            field_type: Type,
            value: Any = None,
            validator: Callable = None,
            default: Any = None
    ) -> Any:
        assert not validator or callable(validator), "Validator must be callable !"
        assert value or default is not None, "Value or default must be set !"

        value = value or default

        assert isinstance(value, field_type), f"Value must be {field_type} type !"
        assert not validator or validator(value), f"Value {value} is not valid !"
        return value

    def __init__(
            self,
            subject: str,
            to: str,
            template_name: str,
            context: dict | None = None,
            from_namespace: str = settings.DEFAULT_FROM_EMAIL
    ) -> None:
        self.subject = self._field_initializer(str, subject)
        self.to = self._field_initializer(str, to, validator=lambda v: validators.validate_email(v) or True)
        self.template_name = self._field_initializer(str, template_name, validator=get_template)
        self.context = self._field_initializer(dict, context, default={})
        self.from_namespace = self._field_initializer(str, from_namespace,
                                                      validator=lambda v: validators.validate_email(v) or True)

        # custom vars
        self.html_content: str = render_to_string(self.template_name, self.context)
        self.email = mail.EmailMultiAlternatives(
            self.subject, self.html_content, self.from_namespace, [self.to]
        )

    def send(self, remove_instance: bool = True):
        self.email.attach_alternative(self.html_content, "text/html")
        self.email.send()

        if remove_instance:
            del self

    def start_thread(self):
        thread = threading.Thread(target=self.send)
        thread.start()
        thread.join()
