import subprocess
from tkinter import messagebox


def convert_mp4_to_avi(input_file):
    output_file = input_file.replace(".mp4", ".avi")
    command = [
        'ffmpeg', '-i', input_file,
        '-c:v', 'libxvid',
        '-qscale:v', '3',  # Option pour contrôler la qualité
        '-c:a', 'libmp3lame',
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Succès", "Conversion en AVI réussie !")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", "La conversion en AVI a échoué.")
