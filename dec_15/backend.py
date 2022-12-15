import os
import subprocess
import sys
import traceback
from tkinter import *
from tkinter import filedialog

class Context():
    _current_dir = os.getcwd()

    def get_current_dir(self):
        return self._current_dir

    def set_current_dir(self, new_directory):
        self._current_dir = new_directory


def set_text(text_area: Text, text: str):
    """
    Replaces the text on in the text area with the given text

    Args:
        text_area (Text): Text area widget
        text (str): New text
    """
    text_area.delete("1.0", END)
    text_area.insert(END, text)


def run(code_area: Text, output_area: Text, context: Context):
    code_str = code_area.get("1.0", END)
    py_file_path = os.path.join(context.get_current_dir(), 'tmp.py')

    with open(py_file_path, 'w') as file:
        file.write(code_str)

    try:
        result = subprocess.run(
                [sys.executable, py_file_path],
                cwd=context.get_current_dir(),
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                encoding='utf-8'
            )
        set_text(output_area, result.stdout)
    except Exception:
        tb = traceback.format_exc()
        set_text(output_area, str(tb))
    finally:
        if os.path.isfile(py_file_path):
            os.remove(py_file_path)


def select_file(list_box: Listbox, code_area: Text, context: Context):
    indices = list_box.curselection()

    if not indices:
        return
    
    selected_file_name = list_box.get(indices[0])
    selected_file_path = os.path.join(context.get_current_dir(), selected_file_name)

    with open(selected_file_path) as file:
        file_text = file.read()
        set_text(code_area, file_text)


def select_directory(list_box: Listbox, context: Context):
    new_directory = filedialog.askdirectory(title="Open directory", initialdir= context.get_current_dir())
    context.set_current_dir(new_directory)
    update_listbox(list_box, new_directory)

def update_listbox(list_box: Listbox, new_directory:str):
    list_box.delete(0, END)
    for file_name in os.listdir(new_directory):
        list_box.insert(END, file_name)
