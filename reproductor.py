import tkinter as tk
from tkinter import filedialogimport tkinter as tk
from tkinter import filedialog
 import pygame

 class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor Multimedia")
        self.root.geometry("400x200")

        # Inicializar pygame.mixer
        pygame.mixer.init()

        # Variables
        self.is_playing = False
        self.audio_file = None

        # Interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Botón para cargar archivo
        self.load_button = tk.Button(self.root, text="Cargar Archivo", command=self.load_file)
        self.load_button.pack(pady=10)

        # Botones de control
        self.play_button = tk.Button(self.root, text="Reproducir", command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pausar", command=self.pause_audio, state=tk.DISABLED)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_audio, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Etiqueta de información
        self.info_label = tk.Label(self.root, text="Carga un archivo para comenzar.")
        self.info_label.pack(pady=10)

    def load_file(self):
        # Abrir un cuadro de diálogo para seleccionar archivo de audio
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.wav")])
        if file_path:
            self.audio_file = file_path
            self.info_label.config(text=f"Archivo cargado: {file_path.split('/')[-1]}")
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.is_playing = False

    def play_audio(self):
        if self.audio_file:
            if not self.is_playing:
                pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
                self.is_playing = True
                self.info_label.config(text="Reproduciendo...")
                self.pause_button.config(state=tk.NORMAL)
            elif pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
                self.info_label.config(text="Reproduciendo...")

    def pause_audio(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.info_label.config(text="Pausado...")

    def stop_audio(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.info_label.config(text="Reproducción detenida.")
            self.pause_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = MediaPlayer(root)
    root.mainloop()
