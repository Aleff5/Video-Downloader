# from tkinter import filedialog
from pytube import YouTube
from customtkinter import *
from tkinter import *
from moviepy.editor import *
import os


def themeMode():
    if switch.get() == 'on':
        set_appearance_mode('Light')
    else:
        set_appearance_mode('Dark')


def chooseDownloadFolder():
    chosen_folder = filedialog.askdirectory()
    if chosen_folder:
        download_folder.set(chosen_folder)


def botaoDownload1():
    link = userLinkMp4.get()
    yt = YouTube(link)
    if resolutionBox.get() == 'high':
        video = yt.streams.get_highest_resolution()
        msgVarGeral.set('downloading the highest resolution of your video...')
    else:
        video = yt.streams.get_lowest_resolution()
        msgVarGeral.set('downloading the lowest resolution of your video...')
    video.download(output_path=download_folder.get())


def botaoDownload2():
    link = userLinkMp3.get()
    yt = YouTube(link)
    arqMp3 = yt.streams.get_audio_only()
    # arqMp3 = yt.streams.filter(only_audio=True).first()

    output_file = arqMp3.download(output_path=download_folder.get())
    new_file_name = os.path.splitext(output_file)[0] + ".mp3"
    os.rename(output_file, new_file_name)
    msgVarGeral.set('Downloading your video as MP3...')


def fileSearcher():
    file_Path = filedialog.askopenfilename(
        filetypes=[('Video Files', '*.mp4')])
    if file_Path:
        nomeArquivo = os.path.basename(file_Path)
        fileName.set(nomeArquivo)


def convertFile():
    file_Path = fileName.get().replace('Arquivo selecionado: ', '')
    if file_Path.lower().endswith('.mp4'):
        op_path = file_Path[:-4] + '.mp3'
        videoClip = VideoFileClip(file_Path)
        audioClip = videoClip.audio
        audioClip.write_audiofile(op_path)
        audioClip.close()
        videoClip.close()
        msgVarGeral.set('Conversão de MP4 para MP3 concluída!')
    else:
        msgVarGeral.set('Formato não suportado')




app = CTk()
app.title('video downloader')
app.geometry('500x600')
set_appearance_mode('dark')



download_folder = StringVar(value="Caminho/Padrao")
choose_folder_button = CTkButton(
    app, text='Escolher Pasta de Download', command=chooseDownloadFolder)
choose_folder_button.pack(padx=10, pady=10)

label2 = CTkLabel(master=app, textvariable=download_folder, width=120, height=25,
                  fg_color=('black', 'gray'), corner_radius=8, text_color=('white'))
label2.pack(padx=9, pady=9)

swicthVar1 = StringVar(value='on')
swicthVar2 = StringVar(value='off')
switch = CTkSwitch(master=app, text='Switch theme', command=themeMode,
                   variable=swicthVar2, onvalue='on', offvalue='off')
switch.pack(padx=10, pady=10)


msgVarGeral = StringVar()


tabview = CTkTabview(app)
tabview.pack(padx=30, pady=30)


tabview.add('Baixar em MP4')
tabview.set('Baixar em MP4')  

userLinkMp4 = CTkEntry(tabview.tab('Baixar em MP4'), placeholder_text='Enter your link',
                       width=150, height=30, border_width=2, corner_radius=10)
userLinkMp4.place(relx=0.5, rely=0.4, anchor='center')


deafultRel = StringVar(value='')

resolutionBox = CTkComboBox(tabview.tab('Baixar em MP4'), values=[
                            'high', 'low'], variable=deafultRel)
resolutionBox.place(relx=0.5, rely=0.63, anchor='center')


bDownload1 = CTkButton(tabview.tab('Baixar em MP4'), text='download',
                       corner_radius=32, hover_color='#399C31', command=botaoDownload1)
bDownload1.place(relx=0.5, rely=0.85, anchor='center')



tabview.add('Baixar em MP3')

userLinkMp3 = CTkEntry(tabview.tab('Baixar em MP3'), placeholder_text='Enter your link',
                       width=150, height=30, border_width=2, corner_radius=10)
userLinkMp3.place(relx=0.5, rely=0.4, anchor='center')



bDownload2 = CTkButton(tabview.tab('Baixar em MP3'), text='download',
                       corner_radius=32, hover_color='#399C31', command=botaoDownload2)
bDownload2.place(relx=0.5, rely=0.85, anchor='center')


tabview.add('Converção')

selectionButton = CTkButton(tabview.tab('Converção'), text='select the archive',
                            corner_radius=32, hover_color='#399C31', command=fileSearcher)
selectionButton.place(relx=0.5, rely=0.65, anchor='center')

convertionButton = CTkButton(tabview.tab('Converção'), text='convert archive',
                             corner_radius=32, hover_color='#399C31', command=convertFile)
convertionButton.place(relx=0.5, rely=0.85, anchor='center')

fileName = StringVar(value='Arquivo não selecionado')
labelName = CTkLabel(tabview.tab('Converção'), textvariable=fileName, width=120,
                     height=25, fg_color=('black', 'gray'), corner_radius=8, text_color=('white'))
labelName.place(relx=0.5, rely=0.45, anchor='center')



label = CTkLabel(master=app, textvariable=msgVarGeral, width=120, height=25, fg_color=(
    'black', 'gray'), corner_radius=8, text_color=('white'))
label.place(relx=0.5, rely=0.85, anchor='center')


app.mainloop()
