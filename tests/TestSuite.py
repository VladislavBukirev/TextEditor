import unittest
import sys
import os
import tkinter
sys.path.append(os.path.abspath(os.path.dirname(__file__)[:-6]))
import TextEditor


class TestTextEditor(unittest.TestCase):
    def test_creation(self):
        TextEditor.new_file()
        self.assertEqual(len(TextEditor.text.get('1.0', tkinter.END)), 1)
        self.assertEqual(TextEditor.FILE_NAME, "Untitled")

    def test_save(self):
        TextEditor.new_file()
        TextEditor.text.insert('1.0', "123456789")
        TextEditor.save_file()
        file = open("Untitled")
        self.assertIsNotNone(file)
        self.assertEqual(file.read(), "123456789\n")
        file.close()

    def test_open(self):
        TextEditor.open_file(None, file="Untitled")
        self.assertGreater(len(TextEditor.text.get('1.0', tkinter.END)), 1)

    def test_portioning(self):
        TextEditor.FILE_NAME = tkinter.NONE
        TextEditor.BYTE_NUMBERS_ARRAY = [0]
        TextEditor.POINTER = -1
        TextEditor.INP = "test.txt"
        TextEditor.open_file(None, file="test.txt")
        number_of_char = len(TextEditor.text.get('1.0', tkinter.END))
        TextEditor.next_portion()
        self.assertNotEqual(len(TextEditor.text.get('1.0', tkinter.END)), number_of_char)
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 3)
        self.assertEqual(TextEditor.POINTER, 1)
        self.assertEqual(TextEditor.text.get('1.0', tkinter.END).count('\n'), 6)
        TextEditor.prev_portion()
        self.assertEqual(len(TextEditor.text.get('1.0', tkinter.END)), number_of_char)
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 3)
        self.assertEqual(TextEditor.POINTER, 0)
        self.assertEqual(TextEditor.text.get('1.0', tkinter.END).count('\n'), 6)

    def test_save_portion(self):
        TextEditor.FILE_NAME = tkinter.NONE
        TextEditor.BYTE_NUMBERS_ARRAY = [0]
        TextEditor.POINTER = -1
        TextEditor.INP = "test.txt"
        TextEditor.open_file(None, file="test.txt")
        TextEditor.save_portion()
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 2)
        self.assertEqual(TextEditor.POINTER, 0)
        self.assertEqual(TextEditor.text.get('1.0', tkinter.END).count('\n'), 6)


if __name__ == '__main__':
    unittest.main()
