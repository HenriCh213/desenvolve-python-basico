from datetime import datetime

agora = datetime.now()

print(f"Data: {agora.day:02}/{agora.month:02}/{agora.year}")
print(f"Hora: {agora.hour:02}:{agora.minute:02}")