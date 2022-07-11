#!/usr/bin/python3
import unittest
import json
import io
import sys

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        y = Square(10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Square(10, 10, 10, 15)
        self.assertEqual(x.size, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)
        x = Square(56444, 500, 90000, 240000)
        self.assertEqual(x.size, 56444)
        self.assertEqual(x.x, 500)
        self.assertEqual(x.y, 90000)
        self.assertEqual(x.id, 240000)

    def test_attrs_type_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("20", 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.3, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2: 1}, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("20")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(["hello world", "?"])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, "x", 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(20, -42.3, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(20, 10, 5.2)
        self.assertRaises(TypeError, Square, float("NaN"))
        self.assertRaises(TypeError, Square, float("inf"))
        self.assertRaises(TypeError, Square, float("NaN"),
                          float("NaN"), float("NaN"))
        self.assertRaises(TypeError, Square, float("inf"),
                          float("inf"), float("inf"))
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, [10, 10],
                          [10, 10], [10, 10])
        self.assertRaises(TypeError, Square, "abebe",
                          "abebe", "abebe")
        self.assertRaises(TypeError, Square, 10,
                          [10, 10], {10, 10})

    def test_attrs_value_validation(self):
        Base._Base__nb_objects = 0
        w_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, w_err, Square, -20)
        self.assertRaisesRegex(ValueError, w_err, Square, 0)
        self.assertRaisesRegex(ValueError, w_err, Square, -20000000)

        h_err = "width must be > 0"
        self.assertRaisesRegex(ValueError, h_err, Square, -20)
        self.assertRaisesRegex(ValueError, h_err, Square, 0)
        self.assertRaisesRegex(ValueError, h_err, Square, -20000000)

        x_err = "x must be >= 0"
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -10)
        self.assertRaisesRegex(ValueError, x_err, Square, 10, -100000)

        y_err = "y must be >= 0"
        self.assertRaisesRegex(ValueError, y_err, Square, 10, 10, -10)
        self.assertRaisesRegex(ValueError, y_err, Square, 1, 1, -100000)

    def test_area(self):
        Base._Base__nb_objects = 0
        x = Square(10)
        self.assertEqual(x.area(), 100)

