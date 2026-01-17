import os          # mexer com arquivos e pastas
import shutil      # mover arquivos
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class Monitor(FileSystemEventHandler):
    def on_created(self, event):
        GuardarArquivo(event)

def GuardarArquivo(event):
    if not os.path.exists("PDFs"):
        os.makedirs("PDFs")
    if event.src_path.endswith(".pdf"):
        nome = os.path.basename(event.src_path)
        for i in os.listdir("PDFs"):
            if nome == i:
                nome_base, extensao = os.path.splitext(nome)
                novo_nome = nome_base + "_1" + extensao
                os.rename(nome,novo_nome)
                nome = novo_nome
        shutil.move(nome, "PDFs/")

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
