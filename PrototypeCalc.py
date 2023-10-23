import tkinter as tk

def calcular_ganhos():
    # Obter os valores dos campos de entrada
    ganhos_diarios = float(entry_diario.get())
    dias_semana = float(entry_dias_semana.get())
    despesa_alimentacao = float(entry_alimentacao.get())
    despesa_plano_saude = float(entry_plano_saude.get())
    despesa_compras = float(entry_compras.get())
    salario_fixo = float(entry_salario_fixo.get())
    
    # Calcular ganhos, despesas e ganhos líquidos
    ganhos_semanais = ganhos_diarios * dias_semana
    ganhos_mensais = ganhos_semanais * 4  # Considerando um mês de 4 semanas
    despesas_mensais = despesa_alimentacao + despesa_plano_saude + despesa_compras + salario_fixo
    ganhos_liquidos_mensais = ganhos_mensais - despesas_mensais

    # Atualizar os rótulos de saída
    label_ganhos_semanais.config(text=f'Ganhos Semanais: R$ {ganhos_semanais:.2f}')
    label_ganhos_mensais.config(text=f'Ganhos Mensais: R$ {ganhos_mensais:.2f}')
    label_despesas_mensais.config(text=f'Despesas Mensais: R$ {despesas_mensais:.2f}')
    label_ganhos_liquidos_mensais.config(text=f'Ganhos Líquidos Mensais: R$ {ganhos_liquidos_mensais:.2f}')

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Ganhos do Motorista de Aplicativo")

# Rótulos e campos de entrada
label_diario = tk.Label(janela, text="Ganhos Diários (R$):")
entry_diario = tk.Entry(janela)
label_dias_semana = tk.Label(janela, text="Dias por Semana:")
entry_dias_semana = tk.Entry(janela)
label_alimentacao = tk.Label(janela, text="Despesa com Alimentação (R$):")
entry_alimentacao = tk.Entry(janela)
label_plano_saude = tk.Label(janela, text="Despesa com Plano de Saúde (R$):")
entry_plano_saude = tk.Entry(janela)
label_compras = tk.Label(janela, text="Despesa com Compras (R$):")
entry_compras = tk.Entry(janela)
label_salario_fixo = tk.Label(janela, text="Salário Fixo (R$):")
entry_salario_fixo = tk.Entry(janela)

label_ganhos_semanais = tk.Label(janela, text="")
label_ganhos_mensais = tk.Label(janela, text="")
label_despesas_mensais = tk.Label(janela, text="")
label_ganhos_liquidos_mensais = tk.Label(janela, text="")

# Botão para calcular ganhos
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_ganhos)

# Layout dos elementos na janela
label_diario.pack()
entry_diario.pack()
label_dias_semana.pack()
entry_dias_semana.pack()
label_alimentacao.pack()
entry_alimentacao.pack()
label_plano_saude.pack()
entry_plano_saude.pack()
label_compras.pack()
entry_compras.pack()
label_salario_fixo.pack()
entry_salario_fixo.pack()
botao_calcular.pack()
label_ganhos_semanais.pack()
label_ganhos_mensais.pack()
label_despesas_mensais.pack()
label_ganhos_liquidos_mensais.pack()

# Iniciar a interface gráfica
janela.mainloop()
