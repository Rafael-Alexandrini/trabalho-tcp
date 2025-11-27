from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, title : str, frame_padding : tuple[int, int, int, int], menu_label : str = 'File'):
        self.__root = Tk()
        self.__root.title(title)
        style = ttk.Style()
        style.theme_use('clam')  
        
        self.__mainframe = ttk.Frame(self.__root, padding=frame_padding)
        self.__mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        self.__root.option_add('*tearoff', FALSE)
        self.__menubar = Menu(self.__root, tearoff=0)
        self.__root['menu'] = self.__menubar
        self.__menu = Menu(self.__menubar, tearoff=0)
        self.__menubar.add_cascade(menu=self.__menu, label=menu_label)

    def start_mainloop(self):
        self.__root.mainloop()

    def set_weights(self, columns : int, rows : int, weight : int = 1):
        for col in range(columns):
            self.__mainframe.columnconfigure(col, weight=weight)
        for row in range(rows):
            self.__mainframe.rowconfigure(row, weight=weight)

    def set_paddings(self, padx : int, pady : int):
        for child in self.__mainframe.winfo_children(): 
            child.grid_configure(padx=padx, pady=pady)

    def add_menu_command(self, label: str, command):
        self.__menu.add_command(label=label, command=command)

    def init_int_var(self):
        return IntVar()
    
    def init_string_var(self):
        return StringVar()

    def create_text_widget(self, width: int, height: int, initial_text: str, column: int, row: int, sticky: str, colspan: int = 1):
        text = Text(self.__mainframe, width=width, height=height)
        text.grid(column=column, row=row, sticky=sticky, columnspan=colspan)
        text.insert("1.0", initial_text)
        return text
    
    def create_button(self, text: str, command, column: int, row: int, sticky: str):
        button = ttk.Button(self.__mainframe, text=text, command=command)
        button.grid(column=column, row=row, sticky=sticky)
        return button
    
    def set_button_commmand(self, button: ttk.Button, command):
        button['command'] = command

    def set_button_text(self, button: ttk.Button, text: str):
        button['text'] = text
    
    def create_text_label(self, text: str, column: int, row: int, sticky: str, font: str = "TkDefaultFont", colspan: int = 1):
        label = ttk.Label(self.__mainframe, text=text, font=font)
        label.grid(column=column, row=row, sticky=sticky, columnspan=colspan)
        return label
    
    def create_combobox(self, values: tuple, textvariable: StringVar, column: int, row: int, sticky: str, initial_index: int = 0):
        combobox = ttk.Combobox(self.__mainframe, textvariable=textvariable)
        combobox.grid(column=column, row=row, sticky=sticky)
        combobox['values'] = values
        combobox.state(["readonly"])
        combobox.current(initial_index)
        return combobox
    
    def __update_scale_label(self, label: ttk.Label, var: IntVar):
        label['text'] = str(var.get())

    def create_horizontal_scale_with_label(self, label_text: str, from_: int, to: int, initial: int, variable: IntVar, length: int, column: int, row: int, sticky: str):
        self.create_text_label(label_text, column, row-1, 'sw')
        label = ttk.Label(self.__mainframe)
        label.grid(column=column, row=row-1, sticky='se')
        scale = ttk.Scale(self.__mainframe, orient='horizontal', length=length, from_=from_, to=to, variable=variable, command=lambda e:self.__update_scale_label(label, variable))
        scale.grid(column=column, row=row, sticky=sticky)
        scale.set(initial)
        return scale
    
    def bind_combobox_event(self, box: ttk.Combobox, command):
        box.bind('<<ComboboxSelected>>', command)

    def disable_text(self, text_widget: Text):
        text_widget['state'] = 'disabled'

    def enable_text(self, text_widget: Text):
        text_widget['state'] = 'normal'

    def is_text_enabled(self, text_widget: Text) -> bool:
        return text_widget['state'] == 'normal'

    def disable_widget(self, widget: Widget):
        widget.state(['disabled'])

    def enable_widget(self, widget: Widget):
        widget.state(['!disabled'])

    def is_widget_enabled(self, widget: Widget) -> bool:
        return widget.instate(['!disabled'])

    def get_text(self, text_widget: Text) -> str:
        return text_widget.get("1.0", END).strip()
    
    def get_intvar_value(self, var: IntVar) -> int:
        return var.get()
 
    def get_strvar_string(self, var: StringVar) -> str:
        return var.get()

    def get_combobox_current_index(self, combobox: ttk.Combobox) -> int:
        return combobox.current()
      
    def set_text(self, text_widget: Text, text: str):
        text_widget.delete("1.0", END)
        text_widget.insert("1.0", text)

    def set_intvar_value(self, var: IntVar, value: int):
        var.set(value)

    def set_combobox_current_index(self, combobox: ttk.Combobox, index: int):
        combobox.current(index)