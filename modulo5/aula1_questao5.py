import emoji

print("""Emojis disponíveis:\n
❤️ - :red_heart:
👍 - :thumbs_up:
🤔 - :thinking_face:
🥳 - :partying_face:
""")

frase = input("Digite uma frase e ela será emojizada:\n")


print(f"Frase emojizada:\n{emoji.emojize(frase)}")

