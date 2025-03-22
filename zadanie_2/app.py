import re
import math
from datetime import datetime

def is_palindrome(text):
    """Sprawdza, czy tekst jest palindromem, ignorując wielkość liter i znaki interpunkcyjne."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def calculate_area(shape, dimensions):
    """Oblicza pole figury (prostokąt lub koło) na podstawie podanych wymiarów."""
    if shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires two dimensions: width and height")
        width, height = dimensions
        return width * height
    elif shape == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires one dimension: radius")
        radius = dimensions[0]
        return math.pi * radius ** 2
    else:
        raise ValueError("Unsupported shape")

def filter_even_numbers(numbers):
    """Zwraca listę parzystych liczb z podanej listy."""
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_str, from_format, to_format):
    """Konwertuje datę z jednego formatu na inny."""
    date_obj = datetime.strptime(date_str, from_format)
    return date_obj.strftime(to_format)

def validate_email(email):
    """Sprawdza poprawność adresu email."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))