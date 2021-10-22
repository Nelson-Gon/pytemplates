# inport testing framework here
# Currently using unittest but can import pytest instead
import unittest
from my_project import hello_world

class TestProject(unittest.TestCase):

    def test_init(self):
        self.assertIsInstance(hello_world.HelloWorld(hello_text="Hello World"), hello_world.HelloWorld)

    def test_hello_text_print(self):
        my_obj = hello_world.HelloWorld(hello_text="Hello World")
        self.assertEqual(my_obj.print_text(), "Hello World")

        with self.assertRaises(AssertionError) as err:
            hello_world.HelloWorld(hello_text=420.42)
        self.assertEqual(str(err.exception), "hello_text must be a string not float")
        




if __name__=="__main__":
    unittest.main()

    