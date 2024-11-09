import subprocess
from tkinter import messagebox


def convert_mp4_to_webm(input_file):
    output_file = input_file.replace(".mp4", ".webm")
    command = [
        'ffmpeg', '-i', input_file,
        '-c:v', 'libvpx-vp9',
        '-c:a', 'libopus',
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Succès", "Conversion en WebM réussie !")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", "La conversion en WebM a échoué.")
