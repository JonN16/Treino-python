import os          # mexer com arquivos e pastas
import shutil      # mover arquivos
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor(FileSystemEventHandler):
    def on_created(self, event):
        GuardarArquivo(event,"PDF")

def GuardarArquivo(event, tipo):

    pasta = tipo
    extensao = "." + tipo.lower()

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    nome = os.path.basename(event.src_path)

    for i in os.listdir(pasta):
        if nome == i:
            n = 1
            nome_base, ext = os.path.splitext(nome)

            while True:
                novo_nome = nome_base + str(n) + ext
                if novo_nome not in os.listdir(pasta):
                    break
                n += 1

            os.rename(nome, novo_nome)
            nome = novo_nome 

    shutil.move(nome, pasta)

def monitorar(pasta):
    observer = Observer()
    observer.schedule(Monitor(), path=pasta, recursive=False)
    observer.start()

    try:
        while True:      
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

arquivo = "c:\\Users\\joaoe\\OneDrive\\Área de Trabalho\\programação\\seila"
monitorar(arquivo)
