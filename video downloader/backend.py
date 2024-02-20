from pytube import YouTube
from customtkinter import *
# from tkinter import *
from moviepy.editor import *
import os


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

msgVarGeral = StringVar()