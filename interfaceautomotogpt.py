import tkinter as tk

def verificar():
    cadeia = entrada.get()
    estado = "q0"

    # Validação da cadeia
    for algarismo in cadeia:
        if algarismo not in ["0", "1"]:
            resultado.set("Cadeia inválida (use apenas 0 ou 1)")
            return

    # Processamento do autômato
    for algarismo in cadeia:
        if estado == "q0":
            if algarismo == "0":
                estado = "q0"
            elif algarismo == "1":
                estado = "q1"

        elif estado == "q1":
            if algarismo == "0":
                estado = "q0"
            elif algarismo == "1":
                estado = "q1"

    # Resultado final
    if estado == "q1":
        resultado.set(f"Estado final: {estado} → Cadeia válida")
    else:
        resultado.set(f"Estado final: {estado} → Cadeia inválida")


# Janela principal
janela = tk.Tk()
janela.title("Autômato Binário")
janela.geometry("350x200")

# Título
titulo = tk.Label(janela, text="Verificador de Cadeia Binária", font=("Arial", 12))
titulo.pack(pady=10)

# Entrada
entrada = tk.Entry(janela, width=25)
entrada.pack(pady=5)

# Botão
botao = tk.Button(janela, text="Verificar", command=verificar)
botao.pack(pady=10)

# Resultado
resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado, fg="blue")
label_resultado.pack(pady=10)

# Rodar
janela.mainloop()