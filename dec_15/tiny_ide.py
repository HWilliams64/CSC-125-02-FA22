import os
from tkinter import *
import backend

window = Tk()
context = backend.Context()
window.title("TIDE")

window.minsize(width=200, height=200)

# CODE
code_label = Label(window, text="Code:", font=("Arial", 10))
code_area = Text(window, height=15, width=80, font=("Courier", 10))
code_scroll = Scrollbar(window, command=code_area.yview)
code_area['yscrollcommand'] = code_scroll.set

# OUTPUT
output_label = Label(window, text="Output:", font=("Arial", 10))
output_area = Text(window, height=5, width=80, font=("Courier", 10))
output_scroll = Scrollbar(window, command=output_area.yview)
output_area['yscrollcommand'] = output_scroll.set


# BUTTONS
save_btn = Button(window, text="Save")
run_btn = Button(window, text="Run", command=lambda :backend.run(code_area, output_area, context))
exit_btn = Button(window, text="Exit", command=window.destroy)
dir_btn = Button(window, text="Directory", command=lambda :backend.select_directory(file_list_box, context))

# LIST BOX
files = StringVar(value=os.listdir(context.get_current_dir()))
file_list_box = Listbox(window, listvariable=files, height=5, selectmode="single")
file_scroll = Scrollbar(window, orient='vertical', command=file_list_box.yview)
file_list_box['yscrollcommand'] = file_scroll.set
file_list_box.bind(
    '<<ListboxSelect>>', 
    lambda e: backend.select_file(file_list_box, code_area, context)
    )


dir_btn.grid(column=0, row=0)
file_list_box.grid(column=0, row=1, rowspan=9, sticky="nsew")
file_scroll.grid(column=1, row=1, rowspan=9, sticky="nsew")

run_btn.grid(column=4, row=0, sticky="e")
save_btn.grid(column=5, row=0, sticky="e")
exit_btn.grid(column=6, row=0, sticky="e")

code_label.grid(column=2, row=0, sticky="w")
code_area.grid(column=2, row=1, columnspan=5, rowspan=4)
code_scroll.grid(column=7, row=1, rowspan=4, sticky="nsew")

output_label.grid(column=2, row=5, sticky="w")
output_area.grid(column=2, row=6, columnspan=5, rowspan=4,)
output_scroll.grid(column=7, row=6, rowspan=4, sticky="nsew")

window.mainloop()
