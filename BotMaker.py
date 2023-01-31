import PySimpleGUI as sg
import os
import pathlib
import shutil
from tkinter import messagebox
import subprocess
import sys

sg.theme('TanBlue')

layout = [
    [sg.Text('DiscordBotMaker (For Button ver)')],
    [sg.Text('BotName', size=(13, 1)), sg.InputText('', size=(20, 1), key='bot')],
    [sg.Text('YourName', size=(13, 1)), sg.InputText('', size=(20, 1), key='name')],
    [sg.Text('Command(x!)', size=(13, 1)), sg.InputText('', size=(20, 1), key='com')],
    [sg.Text('Button-Command', size=(13, 1)), sg.InputText('', size=(20, 1), key='com1')],
    [sg.Text('Button1', size=(13, 1)), sg.InputText('', size=(20, 1), key='b1'), sg.InputText('', size=(20, 1), key='mes1')],
    [sg.Text('Button2', size=(13, 1)), sg.InputText('', size=(20, 1), key='b2'), sg.InputText('', size=(20, 1), key='mes2')],
    [sg.Text('Button3', size=(13, 1)), sg.InputText('', size=(20, 1), key='b3'), sg.InputText('', size=(20, 1), key='mes3')],
    [sg.Text('BotToken', size=(13, 1)), sg.InputText('', size=(20, 1), key='token')],
    [sg.Button('Start', key='go'), sg.Button('Cancel', key='no')]
]
     
window = sg.Window('BotMaker(button ver)', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'no':
        break

    if event == 'go': 

        shutil.copyfile("./files/bot.sorakana", "./build/bot.txt")

        file_name = "./build/bot.txt"
        with open(file_name, encoding="cp932") as f:
           data_lines = f.read()

        data_lines = data_lines.replace("YourCommand", values['com'])
        data_lines = data_lines.replace("BotName", values['bot'])
        data_lines = data_lines.replace("YourName", values['name'])
        data_lines = data_lines.replace("BotToken", values['token'])
        data_lines = data_lines.replace("Command1", values['com1'])
        data_lines = data_lines.replace("l1", values['b1'])
        data_lines = data_lines.replace("l2", values['b2'])
        data_lines = data_lines.replace("l3", values['b3'])
        data_lines = data_lines.replace("YourMessage1", values['mes1'])
        data_lines = data_lines.replace("YourMessage2", values['mes2'])
        data_lines = data_lines.replace("YourMessage3", values['mes3'])

        with open(file_name, mode="w", encoding="cp932") as f:
           f.write(data_lines)

        os.rename("./build/bot.txt", "./build/DiscordBot.py")

        messagebox.showinfo('BotMaker', 'Done! (In "build")                       ')
        ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
    if ret == True:
        sys.exit()
