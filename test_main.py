import unittest
import os
from main import read_text_files, search_engine, print_result


class TestReadText(unittest.TestCase):

    def setUp(self):
        # create directory and files for tests
        self.test_dir = "test_files"
        os.mkdir(self.test_dir)
        self.text_data = {
            "file1.txt": "This is file one",
            "file2.txt": "This is file two",
        }

        for filename, text in self.text_data.items():
            with open(os.path.join(self.test_dir, filename), "w") as f:
                f.write(text)

    def test_valid_path(self):
        # check the given path is valid
        self.assertIsInstance(read_text_files(self.test_dir), dict)

    def test_invalid_path(self):
        # check the given path is invalid
        directory = 'test'
        self.assertRaises(ValueError, read_text_files, directory)

    def test_empty_dir(self):
        # test the directory is empty
        directory = 'empty_dir'
        os.mkdir(directory)
        self.assertRaises(ValueError, read_text_files, directory)
        os.rmdir(directory)

    def test_read_text_files(self):
        # check the data store in the memory is right
        self.assertEqual(read_text_files(self.test_dir), self.text_data)

    def tearDown(self):
        # removing the dummy directory and files
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)


class TestSearchEngine(unittest.TestCase):

    def test_type(self):
        # Raise typeerror if not dictionary
        self.assertRaises(TypeError, search_engine, 3)
        self.assertRaises(TypeError, search_engine, 3+5j)
        self.assertRaises(TypeError, search_engine, True)
        self.assertRaises(TypeError, search_engine, "radius")


class TestPrintResult(unittest.TestCase):

    def test_type(self):
        # Raise typeerror if not dictionary
        self.assertRaises(TypeError, print_result, 3)
        self.assertRaises(TypeError, print_result, True)
        self.assertRaises(TypeError, print_result, "radius")


if __name__ == "__main__":
    unittest.main()
