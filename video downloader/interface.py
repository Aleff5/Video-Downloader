
from customtkinter import *
from tkinter import *


def themeMode():
    if switch.get() == 'on':
        set_appearance_mode('Light')
    else:
        set_appearance_mode('Dark')

# inicializando janela
app = CTk()
app.title('video downloader')
app.geometry('500x600')
set_appearance_mode('dark')


# selecao de pasta
download_folder = StringVar(value="Caminho/Padrao")
choose_folder_button = CTkButton(app, text='Escolher Pasta de Download',)
choose_folder_button.pack(padx=10, pady=10)
label2 = CTkLabel(master=app, textvariable=download_folder, width=120, height=25,fg_color=('black', 'gray'), corner_radius=8, text_color=('white'))
label2.pack(padx=9, pady=9)


# set theme
swicthVar1 = StringVar(value='on')
swicthVar2 = StringVar(value='off')
switch = CTkSwitch(master=app, text='Switch theme', command=themeMode,variable=swicthVar2, onvalue='on', offvalue='off')
switch.pack(padx=10, pady=10)


msgVarGeral = StringVar()

# tabs
tabview = CTkTabview(app)
tabview.pack(padx=30, pady=30)

# MP4 Tab
tabview.add('Baixar em MP4')
tabview.set('Baixar em MP4')  # default tab

userLinkMp4 = CTkEntry(tabview.tab('Baixar em MP4'), placeholder_text='Enter your link',width=150, height=30, border_width=2, corner_radius=10)
userLinkMp4.place(relx=0.5, rely=0.4, anchor='center')
# selecao de resolucao
deafultRel = StringVar(value='')
resolutionBox = CTkComboBox(tabview.tab('Baixar em MP4'), values=['high', 'low'], variable=deafultRel)
resolutionBox.place(relx=0.5, rely=0.63, anchor='center')
# botao download 1
bDownload1 = CTkButton(tabview.tab('Baixar em MP4'), text='download',corner_radius=32, hover_color='#399C31')
bDownload1.place(relx=0.5, rely=0.85, anchor='center')


# MP3
tabview.add('Baixar em MP3')
userLinkMp3 = CTkEntry(tabview.tab('Baixar em MP3'), placeholder_text='Enter your link',width=150, height=30, border_width=2, corner_radius=10)
userLinkMp3.place(relx=0.5, rely=0.4, anchor='center')
# Botao download 2
bDownload2 = CTkButton(tabview.tab('Baixar em MP3'), text='download', corner_radius=32, hover_color='#399C31')
bDownload2.place(relx=0.5, rely=0.85, anchor='center')

# CONVESAO tab
tabview.add('Converção')
# botao de selecao
selectionButton = CTkButton(tabview.tab('Converção'), text='select the archive',corner_radius=32, hover_color='#399C31')
selectionButton.place(relx=0.5, rely=0.65, anchor='center')
# botao de conversao
convertionButton = CTkButton(tabview.tab('Converção'), text='convert archive',corner_radius=32, hover_color='#399C31')
convertionButton.place(relx=0.5, rely=0.85, anchor='center')

fileName = StringVar(value='Arquivo não selecionado')
labelName = CTkLabel(tabview.tab('Converção'), textvariable=fileName, width=120,height=25, fg_color=('black', 'gray'), corner_radius=8, text_color=('white'))
labelName.place(relx=0.5, rely=0.45, anchor='center')


# main label
label = CTkLabel(master=app, textvariable=msgVarGeral, width=120, height=25, fg_color=('black', 'gray'), corner_radius=8, text_color=('white'))
label.place(relx=0.5, rely=0.85, anchor='center')


app.mainloop()
