from pytube import YouTube
import pyperclip, os, re, send2trash
import moviepy.editor as mp

link = pyperclip.paste()
YouTube(link).streams.filter(only_audio=True).first().download('C:\\Emil\\Muzica')

folder = 'C:\\Emil\\Muzica'
for file in os.listdir(folder):
    if re.search('mp4', file):
        mp4_path = os.path.join(folder, file)
        mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        send2trash.send2trash(mp4_path)