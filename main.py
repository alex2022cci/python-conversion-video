# import de la librairie pour le graphisme
from tkinter import *
from tkinter import filedialog, messagebox

# Import des fonctions de conversion depuis les fichiers spécifiques
from converters.mp4_to_webm import convert_mp4_to_webm
from converters.mp4_to_avi import convert_mp4_to_avi

# créer une première fenêtre
window = Tk()

# personalisation de la fenêtre
window.title("Convertisseur Vidéo")
window.geometry("800x600")
window.minsize(480,360)
window.config(background='#91Da91')

# Créer la frame
frame = Frame(window, bg='#91Da91', bd=2 , relief=SUNKEN)

# ajouter du texte
label_title = Label(frame, text="Bienvenue sur l'application \n de conversion de vidéo",
                                    font=("Helvetica", 40), bg='#91DA91', fg='white')
label_title.pack()

# ajouter du texte 2
label_subtitle = Label(frame, text="Cliquer sur Fichier", font=("Helvetica", 25), bg='#91DA91', fg='white')
label_subtitle.pack()

# ajouter la frame
frame.pack(expand=YES)


# Fonction pour sélectionner le fichier et lancer la conversion en WebM
def select_and_convert_to_webm():
    input_file = filedialog.askopenfilename(title="Sélectionner un fichier MP4", filetypes=[("MP4 files", "*.mp4")])
    if input_file:
        convert_mp4_to_webm(input_file)


# Fonction pour sélectionner le fichier et lancer la conversion en AVI
def select_and_convert_to_avi():
    input_file = filedialog.askopenfilename(title="Sélectionner un fichier MP4", filetypes=[("MP4 files", "*.mp4")])
    if input_file:
        convert_mp4_to_avi(input_file)


# Création d'une barre de menu
menu_bar = Menu(window)

# Créer un 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Convertir en WebM", command=select_and_convert_to_webm)
file_menu.add_command(label="Convertir en AVI", command=select_and_convert_to_avi)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# ajout de la menu_bar
window.config(menu=menu_bar)

# afficher la fenêtre
window.mainloop()