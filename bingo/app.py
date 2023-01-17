from bingo import Bingo
import tkinter as tk

b = Bingo(90)
root = tk.Tk()
root.title("Bingo 1.0")
root.geometry("400x200")
frame = tk.Frame(root)
frame.pack()
iniciar = tk.Button(frame, text="Iniciar", command=b.run)
iniciar.pack(side=tk.LEFT)
pausar = tk.Button(frame, text="Pausar/Continuar", command=b.play_pause)
pausar.pack(side=tk.LEFT)
finalizar = tk.Button(frame, text="Finalizar", command=b.finalizar)
finalizar.pack(side=tk.LEFT)

texto_numero = tk.StringVar()
texto_numero.set(".")
b.adicionar_observador(texto_numero)
numero = tk.Label(root, font=("Arial", 100), textvariable=texto_numero)
numero.pack()

root.mainloop()






