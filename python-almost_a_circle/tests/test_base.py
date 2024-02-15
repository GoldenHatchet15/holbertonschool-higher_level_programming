#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBaseInstantiation - Tests instantiation of the Base class.
    TestBaseToJSONString - Tests the JSON string conversion method of Base.
    TestBaseSaveToFile - Tests the JSON file saving method of Base.
    TestBaseFromJSONString - Tests the JSON string to dictionary conversion method of Base.
    TestBaseCreate - Tests the create method of Base, creating instances from dictionaries.
    TestBaseLoadFromFile - Tests the JSON file to instances loading method of Base.
    TestBaseSaveToFileCSV - Tests the CSV file saving method of Base (if applicable).
    TestBaseLoadFromFileCSV - Tests the CSV file to instances loading method of Base (if applicable).
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0  # Resetting for consistent id assignment

    def test_no_arg(self):
        """Test id auto-assignment."""
        b1 = Base()
        b2 = Base()
        self.assertTrue(b1.id + 1, b2.id)

    def test_id_assigned(self):
        """Test manual id assignment."""
        b3 = Base(42)
        self.assertEqual(b3.id, 42)

    def test_id_as_none(self):
        """Test None as id."""
        b4 = Base(None)
        self.assertIsNotNone(b4.id)

    def test_string_id(self):
        """Test string as id."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_float_id(self):
        """Test float as id."""
        b = Base(5.5)
        self.assertEqual(b.id, 5.5)

    def test_complex_id(self):
        """Test complex number as id."""
        b = Base(complex(5, 1))
        self.assertEqual(b.id, complex(5, 1))

    def test_list_id(self):
        """Test list as id."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_tuple_id(self):
        """Test tuple as id."""
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

    def test_dict_id(self):
        """Test dictionary as id."""
        b = Base({"a": 1, "b": 2})
        self.assertEqual(b.id, {"a": 1, "b": 2})

    def test_bool_id(self):
        """Test Boolean True as id."""
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_bool_false_id(self):
        """Test Boolean False as id, ensuring it's not confused with None/default."""
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_set_id(self):
        """Test set as id."""
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})

    def test_frozenset_id(self):
        """Test frozenset as id."""
        b = Base(frozenset([1, 2, 3]))
        self.assertEqual(b.id, frozenset([1, 2, 3]))

    def test_range_id(self):
        """Test range as id."""
        b = Base(range(5))
        self.assertEqual(b.id, range(5))

    def test_bytes_id(self):
        """Test bytes as id."""
        b = Base(b'Python')
        self.assertEqual(b.id, b'Python')

    def test_bytearray_id(self):
        """Test bytearray as id."""
        b = Base(bytearray(b'example'))
        self.assertEqual(b.id, bytearray(b'example'))

    def test_memoryview_id(self):
        """Test memoryview as id."""
        b = Base(memoryview(b'example'))
        self.assertTrue(isinstance(b.id, memoryview))

    def test_nan_id(self):
        """Test NaN as id. Note: NaN is unique in that it is not equal to itself."""
        b = Base(float('nan'))
        self.assertTrue(isinstance(b.id, float) and b.id != b.id)  # NaN is not equal to itself

    def test_inf_id(self):
        """Test infinity as id."""
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

class TestBaseToJSONString(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_list_dict_to_json_string(self):
        """Test converting list of dictionaries to JSON string."""
        dict_list = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(dict_list)
        self.assertIsInstance(json_str, str)
        self.assertCountEqual(json_str, '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_with_none(self):
        """Test converting None to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        """Test converting an empty list to JSON string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_empty_dict(self):
        """Test converting a list containing an empty dictionary to JSON string."""
        self.assertEqual(Base.to_json_string([{}]), "[{}]")

    def test_to_json_string_with_multiple_empty_dicts(self):
        """Test converting a list containing multiple empty dictionaries to JSON string."""
        self.assertEqual(Base.to_json_string([{}, {}]), "[{}, {}]")

    def test_to_json_string_with_mixed_empty_and_non_empty_dicts(self):
        """Test converting a list with mixed empty and non-empty dictionaries to JSON string."""
        dict_list = [{}, {"id": 1}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{}, {"id": 1}]')

    def test_to_json_string_with_non_dict(self):
        """Test handling of non-dictionary items in the list. Expected to raise an error."""
        non_dict_list = ["Not a dict"]
        with self.assertRaises(TypeError):
            Base.to_json_string(non_dict_list)

    def test_to_json_string_with_partially_valid_input(self):
        """Test converting a list with both dictionaries and invalid types."""
        mixed_list = [{"id": 1}, "Not a dict"]
        with self.assertRaises(TypeError):
            Base.to_json_string(mixed_list)

    def test_to_json_string_with_nested_dicts(self):
        """Test converting a list containing nested dictionaries to JSON string."""
        dict_list = [{"id": 1, "dimensions": {"width": 10, "height": 20}}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 1, "dimensions": {"width": 10, "height": 20}}]')

class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""
    
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0  # Resetting for consistent id assignment

    @classmethod
    def tearDownClass(cls):
        """Clean up files."""
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_save_rectangle_to_file(self):
        """Test saving list of Rectangle instances to a file."""
        r1 = Rectangle(1, 1, 0, 0, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_with_none(self):
        """Test saving None to a file, which should result in an empty list in the file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        """Test saving an empty list to a file, which should result in an empty list in the file."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_multiple_rectangles_to_file(self):
        """Test saving multiple Rectangle instances to a file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"id": 2', content)

    def test_save_multiple_squares_to_file(self):
        """Test saving multiple Square instances to a file."""
        s1 = Square(5, 0, 0, 3)
        s2 = Square(7, 1, 1, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 3', content)
            self.assertIn('"id": 4', content)

    def test_save_to_file_overwrite(self):
        """Test overwriting an existing file with new content."""
        r1 = Rectangle(1, 1, 0, 0, 1)
        Rectangle.save_to_file([r1])  # Initial save
        r2 = Rectangle(2, 2, 1, 1, 2)
        Rectangle.save_to_file([r2])  # Overwrite with new content
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 2', content)
            self.assertNotIn('"id": 1', content)

class TestBaseFromJSONString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""
    
    def test_json_string_to_list(self):
        """Test converting JSON string to list of dictionaries."""
        json_str = '[{"id": 1}, {"id": 2}]'
        dict_list = Base.from_json_string(json_str)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 2)
        self.assertDictEqual(dict_list[0], {"id": 1})
        self.assertDictEqual(dict_list[1], {"id": 2})

    def test_json_string_empty_list(self):
        """Test converting JSON string of an empty list."""
        json_str = '[]'
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_json_string_none(self):
        """Test converting a None JSON string to a list."""
        json_str = None
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_json_string_empty(self):
        """Test converting an empty JSON string."""
        json_str = ''
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_json_string_malformed(self):
        """Test handling of malformed JSON string."""
        json_str = '[{id: 1}, {id: 2}]'  # Missing quotes around field names
        with self.assertRaises(ValueError):
            Base.from_json_string(json_str)

    def test_json_string_with_complex_data(self):
        """Test converting JSON string with more complex data."""
        json_str = '[{"id": 1, "list": [1, 2, 3], "dict": {"key": "value"}}]'
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertDictEqual(result[0], {"id": 1, "list": [1, 2, 3], "dict": {"key": "value"}})

    def test_json_string_with_nested_objects(self):
        """Test converting JSON string with nested objects."""
        json_str = '[{"id": 1, "nested": {"id": 2}}]'
        result = Base.from_json_string(json_str)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertDictEqual(result[0], {"id": 1, "nested": {"id": 2}})

    def test_json_string_with_invalid_type(self):
        """Test handling of invalid type input instead of string."""
        with self.assertRaises(TypeError):
            Base.from_json_string(123)  # Input is not a string


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""
    
    def test_create_rectangle(self):
        """Test creating Rectangle instance from dictionary."""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

    def test_create_square(self):
        """Test creating Square instance from dictionary."""
        s1 = Square(4, 2, 3, 5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsInstance(s2, Square)
        self.assertNotEqual(s1, s2)
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

    def test_create_with_missing_fields(self):
        """Test creating instances with missing fields in the dictionary."""
        rectangle_dict = {"id": 101, "width": 5, "height": 10}
        # Missing 'x' and 'y', should default to 0
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 101)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)  # Check if default is applied
        self.assertEqual(rectangle.y, 0)  # Check if default is applied

    def test_create_with_extra_fields(self):
        """Test creating instances with extra fields in the dictionary that are ignored."""
        square_dict = {"id": 202, "size": 7, "x": 2, "y": 3, "extra": "ignored"}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 202)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        with self.assertRaises(AttributeError):
            _ = square.extra  # Attribute 'extra' should not exist

    def test_create_rectangle_defaults(self):
        """Test creating Rectangle with default values for 'x', 'y', and 'id'."""
        rectangle_dict = {"width": 4, "height": 2}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_create_square_defaults(self):
        """Test creating Square with default values for 'x', 'y', and 'id'."""
        square_dict = {"size": 5}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for testing load_from_file method of Base class."""
    
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0  # Resetting for consistent id assignment
    
    @classmethod
    def tearDownClass(cls):
        """Clean up files."""
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_load_rectangles_from_file(self):
        """Test loading list of Rectangle instances from a file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_of_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(list_of_rectangles, list)
        self.assertTrue(all(isinstance(r, Rectangle) for r in list_of_rectangles))
        self.assertEqual(len(list_of_rectangles), 2)
        self.assertEqual(list_of_rectangles[0].width, 10)
        self.assertEqual(list_of_rectangles[1].width, 2)

    def test_load_squares_from_file(self):
        """Test loading list of Square instances from a file."""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(7, 0, 0, 4)
        Square.save_to_file([s1, s2])
        list_of_squares = Square.load_from_file()
        self.assertIsInstance(list_of_squares, list)
        self.assertTrue(all(isinstance(s, Square) for s in list_of_squares))
        self.assertEqual(len(list_of_squares), 2)
        self.assertEqual(list_of_squares[0].size, 5)
        self.assertEqual(list_of_squares[1].size, 7)

    def test_load_from_empty_file(self):
        """Test loading from an empty file."""
        Rectangle.save_to_file([])
        list_of_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(list_of_rectangles, list)
        self.assertEqual(len(list_of_rectangles), 0)

    def test_load_from_nonexistent_file(self):
        """Test loading from a nonexistent file."""
        if os.path.exists("Nonexistent.json"):
            os.remove("Nonexistent.json")  # Ensure file does not exist before test
        list_of_objects = Base.load_from_file("Nonexistent.json")
        self.assertIsInstance(list_of_objects, list)
        self.assertEqual(len(list_of_objects), 0)

    def test_load_rectangles_with_custom_attributes(self):
        """Test loading Rectangle instances with custom attributes from a file."""
        r1 = Rectangle(10, 5, 1, 2, 3)
        r2 = Rectangle(20, 10, 3, 4, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertTrue(len(rectangles) == 2)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[1].height, 10)

    def test_file_after_modification(self):
        """Test integrity of loaded objects after modifying the source file."""
        s1 = Square(4, 1, 2, 3)
        Square.save_to_file([s1])
        # Modify the file to add another Square
        s2 = Square(8, 3, 4, 5)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[1].size, 8)

if __name__ == "__main__":
    unittest.main()
