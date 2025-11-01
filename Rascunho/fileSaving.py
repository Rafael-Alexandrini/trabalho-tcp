from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the main Tk window
Tk().withdraw()

filename = askopenfilename(
    title="Select a MIDI file",
    filetypes=[("MIDI files", "*.mid *.midi"), ("All files", "*.*")]
)

if filename:
    print("Selected file:", filename)
else:
    print("No file selected")

#######################################
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

Tk().withdraw()

save_path = asksaveasfilename(
    title="Save MIDI file as...",
    defaultextension=".mid",
    filetypes=[("MIDI files", "*.mid *.midi")]
)

if save_path:
    print("File will be saved to:", save_path)
    # Example of writing binary data:
    with open(save_path, "wb") as f:
        f.write(b"your midi data here")
else:
    print("Save cancelled")