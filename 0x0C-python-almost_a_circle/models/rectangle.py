#!/usr/bin/python3
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectCls(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        y = Rectangle(10, 10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10, 10, 10, 15)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)

    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("20", 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, "20")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(20, 20, "x", 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(20, 20, 10, "y")
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("inf"))
        self.assertRaises(TypeError, Rectangle, float("inf"), float("NaN"))
        self.assertRaises(TypeError, Rectangle, float("NaN"), float("NaN"),
                          float("NaN"), float("NaN"))
        self.assertRaises(TypeError, Rectangle, float("inf"), float("inf"),
                          float("inf"), float("inf"))
        self.assertRaises(TypeError, Rectangle, None, None)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, [10, 10], [10, 10],
                          [10, 10], [10, 10])
        self.assertRaises(TypeError, Rectangle, "abebe", "abebe",
                          "abebe", "abebe")
        self.assertRaises(TypeError, Rectangle, 10, (10, 10),
                          [10, 10], {10, 10})

    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Rectangle, -20, 20)
        self.assertRaisesRegex(ValueError, w_err, Rectangle, 0, 20)
        self.assertRaisesRegex(ValueError, w_err, Rectangle, -20000000, 20)

        h_err = "height must be > 0"
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, -20)
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, 0)
        self.assertRaisesRegex(ValueError, h_err, Rectangle, 20, -20000000)

        x_err = "x must be >= 0"

