from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator 
def validacion_numeros(value):
    if not value.indigit():
        raise ValidationError("El valor debe contener solo numeros")
def validacion_letras(value):
    if not value.isalpha():
        raise ValidationError("El valor debe contener solo letras")
#expresiones regulares
validacion_especial = RegexValidator(
    regex= r'^[a-zA-Z\s]+$',
    message= 'El valor debe contener letras y espacios'
)

