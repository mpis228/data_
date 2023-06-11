import tkinter
import customtkinter
import tools


class FatherW(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main = None
        self.geometry("600x460")
        self.InputGet = customtkinter.CTkEntry(self)
        self.InputGet.pack()
        self.button_cod = customtkinter.CTkButton(self, text="закодувати", command=self.cod)
        self.button_decod = customtkinter.CTkButton(self, text="розкодувати", command=self.decod)
        self.button_cod.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)
        self.button_decod.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)
        self.answer = None

    def chek_leb_and_del(self):
        if self.answer is None:
            pass
        else:
            self.answer.destroy()

    def cod(self):
        self.chek_leb_and_del()
        text = self.InputGet.get()
        self.answer = customtkinter.CTkLabel(self, text=self.main.cod(text))
        self.answer.pack()

    def decod(self):
        self.chek_leb_and_del()
        text = self.InputGet.get()
        self.answer = customtkinter.CTkLabel(self, text=self.main.decod(text))
        self.answer.pack()


class WindowAtbash(FatherW):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Шифр Атбаш")
        self.main = tools.Adbash()

    def decod(self):
        self.chek_leb_and_del()
        text = self.InputGet.get()
        self.answer = customtkinter.CTkLabel(self, text=self.main.cod(text))
        self.answer.pack()


class WindowCezar(FatherW):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Шифр Цезарь")
        self.main = tools.Cezar()


class WindowPolibia(FatherW):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Шифр Полибия")
        self.main = tools.Polibia()


class WindowTrisimys(FatherW):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Шифр Трисемуса")
        self.main = tools.Trisemus()
        self.key_word_labal = customtkinter.CTkLabel(self, text="ведите слово ключ")
        self.key_word_labal.pack()
        self.input_get_word_key = customtkinter.CTkEntry(self)
        self.input_get_word_key.pack()

    def cod(self):
        self.chek_leb_and_del()
        text = self.InputGet.get()
        key = self.input_get_word_key.get()
        self.answer = customtkinter.CTkLabel(self, text=self.main.cod(key, text))
        self.answer.pack()

    def decod(self):
        self.chek_leb_and_del()
        text = self.InputGet.get()
        key = self.input_get_word_key.get()
        self.answer = customtkinter.CTkLabel(self, text=self.main.decod(key, text))
        self.answer.pack()


class App(customtkinter.CTk):

    """главаний класс я би ще назвал його класс меню тому что що в нем прописана логика роботи с другими класами
    просанна работа 4 кнопок"""

    def __init__(self):
        super().__init__()
        self.geometry('600x520')
        self.title("app")
        self.label = customtkinter.CTkLabel(self, text="Вибери шифр", width=300, height=300)
        self.label.pack()
        self.button_1 = customtkinter.CTkButton(self, text="Атбаш", command=self.open_atbash)
        self.button_2 = customtkinter.CTkButton(self, text="Цезар", command=self.open_cezar)
        self.button_3 = customtkinter.CTkButton(self, text="Полібія", command=self.open_polibi)
        self.button_4 = customtkinter.CTkButton(self, text="Трісемус", command=self.open_trisimys)
        self.button_1.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
        self.button_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.button_3.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)
        self.button_4.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
        self.top_wind = None

    def open_atbash(self):  # октритие окно роботы с шифром атбаш
        if self.top_wind is None or not self.top_wind.winfo_exists():
            self.top_wind = WindowAtbash(self)
        else:
            self.top_wind.focus()

    def open_cezar(self):  # октритие окно роботы с шифром цезарь
        if self.top_wind is None or not self.top_wind.winfo_exists():
            self.top_wind = WindowCezar(self)
        else:
            self.top_wind.focus()

    def open_polibi(self):  # октритие окно роботы с шифром полибия
        if self.top_wind is None or not self.top_wind.winfo_exists():
            self.top_wind = WindowPolibia(self)
        else:
            self.top_wind.focus()

    def open_trisimys(self):  # октритие окно роботы с шифром Трисемус
        if self.top_wind is None or not self.top_wind.winfo_exists():
            self.top_wind = WindowTrisimys(self)
        else:
            self.top_wind.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
