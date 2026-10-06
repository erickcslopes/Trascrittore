# trascrittore

Simples programa de transcrição de áudio em português usando Whisper (openai-whisper).

## Como usar

1. Instale o Python e o ffmpeg (no Windows: `winget install ffmpeg`).
2. Instale o Whisper: `pip install openai-whisper`.
3. Coloque os arquivos `.mp3`, `.m4a` ou `.mp4` na pasta `Input`.
4. Execute `executar.bat` (ou `python trascrivere.py`).
5. Escolha o modelo no menu:
   - `1` ou `base`: mais rápido e leve; é o padrão ao pressionar Enter.
   - `2` ou `medium`: geralmente mais preciso, mas mais lento e exige mais memória.

O modelo escolhido é usado para todos os arquivos daquela execução. Também é possível digitar o nome do modelo (`base` ou `medium`). Opções inválidas solicitam uma nova escolha.

Na primeira utilização de cada modelo, o Whisper baixa seus arquivos, o que exige conexão com a internet e pode demorar.

O texto transcrito é salvo em `.txt` na pasta `Output`, com o mesmo nome do áudio.
