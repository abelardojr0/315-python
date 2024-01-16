from tkinter import * 

caixa = Tk()
caixa.title("Hora trabalhada")
caixa.geometry("300x300")


def calcular_hora():
    salario = float(salario_input.get())
    horas = int(horas_input.get())
    hora_trabalhada = salario / horas
    if hora_trabalhada >= 0 and hora_trabalhada <= 10:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="red")
    elif hora_trabalhada >= 11 and hora_trabalhada <= 25:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="orange")
    elif hora_trabalhada >= 26 and hora_trabalhada <= 50:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="blue")
    else:
        resultado.configure(text=f"Você recebe por hora: R$ {hora_trabalhada:.2f}", fg="pink")





salario_label = Label(text="Digite o seu salário", font=("Arial", 16)).pack()
salario_input = Entry()
salario_input.pack()


horas_label = Label(text="Digite a quantidade de horas trabalhadas").pack()
horas_input = Entry()
horas_input.pack()


botao = Button(caixa, text="Calcular hora trabalhada", command=calcular_hora)
botao.pack()


resultado = Label(text="")
resultado.pack()





caixa.mainloop()