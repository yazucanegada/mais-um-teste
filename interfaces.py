import PySimpleGUI as sg
from funcaoB import *
from funcaoAV import *

def JanelaDeLogin():
    sg.theme('DarkAmber')

    layout = [[sg.Text('Username', key= '-user-')],
              [sg.InputText()],
              [sg.Text('Senha')],
              [sg.InputText()],
              [sg.Button('Logar'), sg.Button('Registrar', key='-regis-')]]
    
    janela = sg.Window('Banco14 Login/Registro', layout)

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED:
            break
        elif(event == '-regis-'):
            janela.close()
            TelaDeCadastro()

def TelaDeCadastro():
    sg.theme('DarkAmber')

    layout = [[sg.Text(('Nome Completo:'),size=(15,1)), sg.InputText()],
              [sg.Text(('CPF:'),size=(15,1)), sg.InputText()],
              [sg.Text(('Seu Sexo:'),size=(15,1)), sg.Combo(('Masculino', 'Feminino', 'Outro'), size=(10,1)), sg.Text('Idade:'),sg.InputText(size=(10,1))],
              [sg.Text(('Senha:'),size=(15,1)), sg.InputText()],
              [sg.Text(('Confimar Senha:'),size=(15,1)), sg.InputText()],
              [sg.Button('Concluir'),sg.Button('Cancelar')]]
    
    janela = sg.Window('Banco14 Registro', layout)

    while True:
        event, values = janela.read()
        if (event == sg.WIN_CLOSED) or (event == 'Cancelar'):
            janela.close()
            break
        elif event == 'Concluir':
            if OpreacaoDeCadastro(values):
                sg.popup("Conta Registrada com Sucesso!")
                janela.close()
                JanelaDeLogin()

            
JanelaDeLogin()
