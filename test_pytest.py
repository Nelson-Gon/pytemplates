import pytest 
from our_project import hello_world

def test_init():
    assert isinstance(hello_world.HelloWorld(hello_text="Hello World"), hello_world.HelloWorld)

def test_hello_text_print():
    my_obj = hello_world.HelloWorld(hello_text="Hello World")
    assert my_obj.print_text() == "Hello World"
    with pytest.raises(AssertionError) as err:
        hello_world.HelloWorld(hello_text=420.42)
        assert str(err.exception) == "hello_text must be a string not float"

#TODO Use fixtures 