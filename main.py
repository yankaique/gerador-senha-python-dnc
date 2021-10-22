import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Senha', size=(20, 1))],
            [sg.Input(key='password', size=(34,4))],
            [sg.Text('Tipo', size=(20, 1))],
            [sg.Combo(['Caracteres Especiais', 'Numeros'], enable_events=True, key='combo', size=(32,4))],
            [sg.Text('Senha Criptografada')],
            [sg.Output(key='crypt_password', size=(32,5))],
            [sg.Button('Gerar Senha')]
        ]
        self.janela = sg.Window('Gerador de Senha', layout)
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break 
            if evento == 'Gerar Senha':
                self.limpar_input(valores)
                senha_criptografada = self.gerar_senha(valores)

    def gerar_senha(self, valores):
        password = valores['password']
        newPassword = ''
        newValue = ''
        for value in password:
            newValue = value
            if value == 'A' or value == 'a':
                newValue = '!' if valores['combo'] == 'Caracteres Especiais' else '1'
            elif value == 'E' or value == 'e':
                newValue = '@' if valores['combo'] == 'Caracteres Especiais' else '2'
            elif value == 'I' or value == 'i':
                newValue = '#' if valores['combo'] == 'Caracteres Especiais' else '3'
            elif value == 'O' or value == 'o':
                newValue = '$' if valores['combo'] == 'Caracteres Especiais' else '4'
            elif value == 'U' or value == 'u':
                newValue = '%' if valores['combo'] == 'Caracteres Especiais' else '5'
            newPassword += newValue
        print(newPassword)
    def limpar_input(self, valor):
        self.janela.FindElement('crypt_password').Update('')

gen = PassGen()
gen.Iniciar()
