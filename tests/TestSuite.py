import unittest
import sys
import os
import tkinter
sys.path.append(os.path.abspath(os.path.dirname(__file__)[:-6]))
import TextEditor
import GUI


class TestTextEditor(unittest.TestCase):
    def cleanup(self):
        TextEditor.FILE_NAME = tkinter.NONE
        TextEditor.BYTE_NUMBERS_ARRAY = [0]
        TextEditor.POINTER = -1
        TextEditor.INP = None
        TextEditor.CONTENT = ""

    def test_creation(self):
        self.cleanup()
        TextEditor.new_file()
        self.assertEqual(len(GUI.text.get('1.0', tkinter.END)), 1)
        self.assertEqual(TextEditor.FILE_NAME, "Untitled")

    def test_save(self):
        self.cleanup()
        TextEditor.new_file()
        GUI.text.delete('1.0', 'end')
        GUI.text.insert('1.0', "123456789")
        TextEditor.save_file(data=GUI.text.get('1.0', 'end'))
        file = open("Untitled")
        self.assertIsNotNone(file)
        self.assertEqual(file.read(), "123456789\n")
        file.close()

    def test_open(self):
        self.cleanup()
        GUI.open_file(file="Untitled")
        self.assertGreater(len(GUI.text.get('1.0', tkinter.END)), 0)
        TextEditor.INP.close()

    def test_portioning(self):
        self.cleanup()
        GUI.open_file(file="test.txt")
        number_of_char = len(GUI.text.get('1.0', tkinter.END))
        GUI.next_portion()
        self.assertNotEqual(len(GUI.text.get('1.0', tkinter.END)), number_of_char)
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 3)
        self.assertEqual(TextEditor.POINTER, 1)
        self.assertEqual(GUI.text.get('1.0', tkinter.END).count('\n'), 6)
        GUI.prev_portion()
        self.assertEqual(len(GUI.text.get('1.0', tkinter.END)), number_of_char)
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 3)
        self.assertEqual(TextEditor.POINTER, 0)
        self.assertEqual(GUI.text.get('1.0', tkinter.END).count('\n'), 6)
        TextEditor.INP.close()

    def test_save_portion(self):
        self.cleanup()
        GUI.open_file(file="test.txt")
        TextEditor.save_portion(GUI.text.get('1.0', 'end-1c'))
        self.assertEqual(len(TextEditor.BYTE_NUMBERS_ARRAY), 2)
        self.assertEqual(TextEditor.POINTER, 0)
        self.assertEqual(GUI.text.get('1.0', tkinter.END).count('\n'), 6)
        TextEditor.INP.close()


if __name__ == '__main__':
    unittest.main()
