import tkinter as tk
from tkinter import filedialog
from desafio_de_projeto_2 import escala_de_cinza, preto_e_branco

def escolher_pasta():
   pasta = filedialog.askopenfile()
   if pasta:
      #print(f'Pasta selecionada: {pasta}')
      escala_de_cinza(pasta)
      preto_e_branco(pasta)
      
janela = tk.Tk()
janela.title('Selecionar Pasta')

botao = tk.Button(janela, text='Escolher Pasta', command=escolher_pasta)
botao.pack(pady=10)

label_resultado = tk.Label(janela, text='Nenhuma pasta selecionada.')
label_resultado.pack()


janela.mainloop()