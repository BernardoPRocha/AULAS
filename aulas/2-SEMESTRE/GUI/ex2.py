from tkinter import *
window = Tk()
window.title("Título da Janela")
window.geometry("350x200+400+200")
window.configure(background="moccasin")
rotulo = Label(window, font="Impact 20 bold", background="moccasin")
rotulo["text"] = "Hello World"
rotulo.pack()
botao= Button(window, text="Click ME", pady=10, padx=10)
botao["font"] = ("Courier New", "16", "bold")
botao["fg"] = "white"
botao["bg"] = "black"
botao["command"] = window.quit
botao.pack()
window.mainloop()