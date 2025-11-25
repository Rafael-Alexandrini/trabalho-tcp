from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, title : str, frame_padding : tuple[int, int, int, int]):
        self._root = Tk()
        self._root.title(title)

        self._mainframe = ttk.Frame(self._root, padding=frame_padding)
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

        self._text = Text()
        self._volume = IntVar()
        self._bpm = IntVar()
        self._instrument = StringVar()
        self._octave = IntVar()

    def start_mainloop(self):
        self._root.mainloop()

    def set_weights(self, columns : int, rows : int, weight : int = 1):
        for col in range(columns):
            self._mainframe.columnconfigure(col, weight=weight)
        for row in range(rows):
            self._mainframe.rowconfigure(row, weight=weight)

    def set_paddings(self, padx : int, pady : int):
        for child in self._mainframe.winfo_children(): 
            child.grid_configure(padx=padx, pady=pady)

    def create_text_widget(self, width: int, height: int, initial_text: str, column: int, row: int, sticky: str):
        self._text = Text(self._mainframe, width=width, height=height)
        self._text.grid(column=column, row=row, sticky=sticky)
        self._text.insert("1.0", initial_text)
        return self._text
    
    def create_button(self, text: str, command, column: int, row: int, sticky: str):
        button = ttk.Button(self._mainframe, text=text, command=command)
        button.grid(column=column, row=row, sticky=sticky)
        return button
    
    def create_text_label(self, text: str, column: int, row: int, sticky: str):
        label = ttk.Label(self._mainframe, text=text)
        label.grid(column=column, row=row, sticky=sticky)
        return label
    
    def create_combobox(self, values: tuple, textvariable: StringVar, column: int, row: int, sticky: str):
        combobox = ttk.Combobox(self._mainframe, textvariable=textvariable)
        combobox.grid(column=column, row=row, sticky=sticky)
        combobox['values'] = values
        combobox.state(["readonly"])
        combobox.current(0)
        return combobox
    
    def create_horizontal_scale_with_label(self, label_text: str, from_: int, to: int, initial: int, variable: IntVar, length: int, column: int, row: int, sticky: str):
        self.create_text_label(label_text, column, row-1, 'sw')
        ttk.Label(self._mainframe, textvariable=variable).grid(column=column, row=row-1, sticky='se')
        scale = ttk.Scale(self._mainframe, orient='horizontal', length=length, from_=from_, to=to, variable=variable)
        scale.grid(column=column, row=row, sticky=sticky)
        scale.set(initial)
        return scale
    
    def get_text(self) -> str:
        return self._text.get("1.0", END).strip()
    
    def get_volume(self) -> int:
        return self._volume.get()
    
    def get_bpm(self) -> int:
        return self._bpm.get()

    def get_combobox_current_index(self, combobox: ttk.Combobox) -> int:
        return combobox.current()
      
    def set_text(self, text: str):
        self._text.delete("1.0", END)
        self._text.insert("1.0", text)

    def set_volume(self, volume: int):
        self._volume.set(volume)
    
    def set_bpm(self, bpm: int):
        self._bpm.set(bpm)

    def set_combobox_current_index(self, combobox: ttk.Combobox, index: int):
        combobox.current(index)