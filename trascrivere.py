import sys
import time
import threading
from pathlib import Path
import whisper

BASE_DIR = Path(__file__).parent
PASTA_INPUT = BASE_DIR / "Input"
PASTA_OUTPUT = BASE_DIR / "Output"


def animacao(texto, parar):
    sequencia = "|/-\\"
    i = 0
    inicio = time.time()
    while not parar.is_set():
        decorrido = int(time.time() - inicio)
        sys.stdout.write(f"\r{texto} {sequencia[i % len(sequencia)]} ({decorrido}s) ")
        sys.stdout.flush()
        i += 1
        time.sleep(0.15)


def transcrever(arquivo, parar):
    try:
        resultado = modelo.transcribe(str(arquivo), language="pt", fp16=False)
        saida = PASTA_OUTPUT / f"{arquivo.stem}.txt"
        saida.write_text(resultado["text"], encoding="utf-8")
        parar.set()
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"Salvo em {saida}")
    except Exception as e:
        parar.set()
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"Erro ao transcrever {arquivo.name}: {e}")


def escolher_modelo():
    print("Escolha o modelo Whisper:")
    print("1 - base (mais rapido)")
    print("2 - medium (maior precisao, mais lento)")
    while True:
        escolha = input("Modelo [1/2, Enter = base]: ").strip().lower()
        if escolha in ("", "1", "base"):
            return "base"
        if escolha in ("2", "medium"):
            return "medium"
        print("Opcao invalida. Escolha 1 (base) ou 2 (medium).")


nome_modelo = escolher_modelo()
print(f"Carregando modelo {nome_modelo}...")
modelo = whisper.load_model(nome_modelo)

arquivos = sorted(
    [p for p in PASTA_INPUT.iterdir() if p.suffix.lower() in (".mp3", ".m4a", ".mp4")]
)

if not arquivos:
    print(f"Nenhum arquivo .mp3, .m4a ou .mp4 encontrado em {PASTA_INPUT}")
    raise SystemExit(1)

PASTA_OUTPUT.mkdir(exist_ok=True)

for arquivo in arquivos:
    print(f"Transcrevendo {arquivo.name}...")
    parar = threading.Event()
    t = threading.Thread(target=transcrever, args=(arquivo, parar))
    t.start()
    animacao("Processando", parar)
    t.join()

print("Concluido.")