#!/usr/bin/python3
"""
module for test_console
"""
from unittest import TestCase
import sys
import io
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(TestCase):
    """
    implementation of test for Console class
    """
    def test_quit(self):
        """
        testing the quit command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
        self.assertTrue(result)

    def test_EOF(self):
        """
        testing the EOF command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("EOF")
        self.assertTrue(result)

    def test_help(self):
        """
        testing the help command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("help")
        self.assertNotEqual(result, "")

    def test_emptyline(self):
        """
        testing the emptyline command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue().strip(), "")

    def test_create_BaseModel(self):
        """
        testing create BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(f.getvalue().strip())

    def tes_show_BaseModel(self):
        """
        testing show BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_destroy_BaseModel(self):
        """
        testing destroy BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("destroy BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_all_BaseModel(self):
        """
        testing all BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("all BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_update_BaseModel(self):
        """
        testing update BaseModel command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            result = HBNBCommand().onecmd("update BaseModel")
        self.assertTrue(f.getvalue().strip())

    def test_all(self):
        """
        testing all() command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            BaseModel = HBNBCommand().onecmd("BaseModel.all()")
            Review = HBNBCommand().onecmd("Review.all()")
            User = HBNBCommand().onecmd("User.all()")
            State = HBNBCommand().onecmd("State.all()")
            City = HBNBCommand().onecmd("City.all()")
            Amenity = HBNBCommand().onecmd("Amenity.all()")
            Place = HBNBCommand().onecmd("Place.all()")
            self.assertNotEqual(BaseModel, [])
            self.assertNotEqual(Review, [])
            self.assertNotEqual(User, [])
            self.assertNotEqual(State, [])
            self.assertNotEqual(City, [])
            self.assertNotEqual(Amenity, [])
            self.assertNotEqual(Place, [])
        self.assertTrue(f.getvalue().strip())

    def test_count(self):
        """
        testing count() command
        """
        #with patch('sys.stdout', new=io.StringIO()) as f:
        BaseModel = HBNBCommand().onecmd("BaseModel.count()")
        Review = HBNBCommand().onecmd("Review.count()")
        User = HBNBCommand().onecmd("User.count()")
        State = HBNBCommand().onecmd("State.count()")
        City = HBNBCommand().onecmd("City.count()")
        Amenity = HBNBCommand().onecmd("Amenity.count()")
        Place = HBNBCommand().onecmd("Place.count()")
        print(BaseModel)
        self.assertNotEqual(int(BaseModel), 0)
        self.assertNotEqual(Review, 0)
        self.assertNotEqual(User, 0)
        self.assertNotEqual(State, 0)
        self.assertNotEqual(City, 0)
        self.assertNotEqual(Amenity, 0)
        self.assertNotEqual(Place, 0)
        #self.assertTrue(f.getvalue().strip())

    def test_show(self):
        """
        testing show("id") command
        """

    def test_destroy(Self):
        """
        testing destroy("id") command
        """


    def test_update_attrs_value(Self):
        """
        testing update("id", "attribute_name",
                        "string_value")
                        command
        """

    def test_update_with_dict(Self):
        """
        testing update() command with dictonary
        """


if __name__ == '__main__':
    unittest.main()
