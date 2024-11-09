import unittest


class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right_complex: "Complex"):
        return Complex(self.real + right_complex.real, self.imaginary + right_complex.imaginary)

    def __sub__(self, right_complex: "Complex"):
        return Complex(self.real - right_complex.real, self.imaginary - right_complex.imaginary)

    def __mul__(self, right_complex: "Complex"):
        return Complex(self.real * right_complex.real - self.imaginary * right_complex.imaginary,
                       self.real * right_complex.imaginary + self.imaginary * right_complex.real)

    def __truediv__(self, right_complex: "Complex"):
        real_numerator = self.real * right_complex.real + self.imaginary * right_complex.imaginary
        imaginary_numerator = right_complex.real * self.imaginary - self.real * right_complex.imaginary
        denominator = self.real ** 2 + right_complex.real ** 2

        return Complex(real_numerator / denominator, imaginary_numerator / denominator)

    def __eq__(self, right_complex: "Complex"):
        return self.real == right_complex.real and self.imaginary == right_complex.imaginary

class TestComplex(unittest.TestCase):

    def setUp(self):
        self.left_complex = Complex(1, 2)
        self.right_complex = Complex(3, 4)

    def test_add(self):
        expected = Complex(4, 6)
        actual = self.left_complex + self.right_complex
        self.assertEqual(expected, actual)

    def test_sub(self):
        expected = Complex(-2, -2)
        actual = self.left_complex - self.right_complex
        self.assertEqual(expected, actual)

    def test_mul(self):
        expected = Complex(-5, 10)
        actual = self.left_complex * self.right_complex
        self.assertEqual(expected, actual)