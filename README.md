# trascrittore

Simples programa de transcrição de áudio usando Whisper (openai-whisper).

## Como usar

1. Instale o Python e o ffmpeg (no Windows: `winget install ffmpeg`).
2. Instale o Whisper: `pip install openai-whisper`.
3. Coloque os arquivos `.mp3` na pasta `Input`.
4. Execute `executar.bat` (ou `python trascrivere.py`).

O texto transcrito é salvo em `.txt` na pasta `output`, com o mesmo nome do áudio.

Para maior precisão, troque `"base"` por `"small"` ou `"medium"` em `trascrivere.py` (mais lento, porém mais preciso).