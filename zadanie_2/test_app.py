import unittest
from app import is_palindrome, calculate_area, filter_even_numbers, convert_date_format, validate_email

class TestApp(unittest.TestCase):
    def setUp(self):
        """Przygotowanie danych testowych przed każdym testem."""
        self.test_numbers = [1, 2, 3, 4, 5, 6]

    # Testy dla is_palindrome
    def test_is_palindrome_typical(self):
        """Testuje typowe palindromy."""
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_empty(self):
        """Testuje przypadek brzegowy: pusty ciąg."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_not_palindrome(self):
        """Testuje tekst, który nie jest palindromem."""
        self.assertFalse(is_palindrome("hello"))

    # Testy dla calculate_area
    def test_calculate_area_rectangle(self):
        """Testuje obliczenie pola prostokąta."""
        self.assertEqual(calculate_area("rectangle", [2, 3]), 6)

    def test_calculate_area_circle(self):
        """Testuje obliczenie pola koła."""
        self.assertAlmostEqual(calculate_area("circle", [2]), 12.566370614359172)

    def test_calculate_area_invalid_shape(self):
        """Testuje błędny kształt figury."""
        with self.assertRaises(ValueError):
            calculate_area("triangle", [2, 3])

    # Testy dla filter_even_numbers
    def test_filter_even_numbers_typical(self):
        """Testuje filtrowanie parzystych liczb z listy."""
        self.assertEqual(filter_even_numbers(self.test_numbers), [2, 4, 6])

    def test_filter_even_numbers_empty(self):
        """Testuje przypadek brzegowy: pusta lista."""
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_even_numbers_no_evens(self):
        """Testuje listę bez parzystych liczb."""
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    # Testy dla convert_date_format
    def test_convert_date_format_typical(self):
        """Testuje konwersję daty z YYYY-MM-DD na DD/MM/YYYY."""
        self.assertEqual(convert_date_format("2023-10-25", "%Y-%m-%d", "%d/%m/%Y"), "25/10/2023")

    def test_convert_date_format_invalid_date(self):
        """Testuje błędny format daty."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01", "%Y-%m-%d", "%d/%m/%Y")

    # Testy dla validate_email
    def test_validate_email_valid(self):
        """Testuje poprawny adres email."""
        self.assertTrue(validate_email("test@example.com"))

    def test_validate_email_invalid(self):
        """Testuje niepoprawny adres email."""
        self.assertFalse(validate_email("test@.com"))
        self.assertFalse(validate_email("test"))

    # Test parametryzowany
    def test_is_palindrome_parametrized(self):
        """Testuje palindromy za pomocą testów parametryzowanych."""
        test_cases = [
            ("kajak", True),
            ("hello", False),
            ("", True),
            ("A man a plan a canal Panama", True),
        ]
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)

if __name__ == "__main__":
    unittest.main()