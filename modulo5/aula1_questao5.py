import emoji
print("Emojis disponíveis:")
print(f"{emoji.emojize(':red_heart:')}  - :red_heart:")
print(f"{emoji.emojize(':thumbs_up:')} - :thumbs_up:")
print(f"{emoji.emojize(':thinking_face:')} - :thinking_face:")
print(f"{emoji.emojize(':partying_face:')} - :partying_face:")
frase = input("Digite uma frase e ela será emojizada:\n")
retorno = emoji.emojize(frase)
print("\nFrase emojizada: ")
print(retorno)