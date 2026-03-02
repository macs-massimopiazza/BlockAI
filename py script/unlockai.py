import os
import subprocess
import ctypes

# Percorso del file hosts su Windows
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Lista di domini da rimuovere (tutti quelli aggiunti nello script precedente)
domains_to_remove = [
    "chat.openai.com",
    "auth.openai.com",
    "platform.openai.com",
    "api.openai.com",
    "openai.com",
    "www.openai.com",
    "www.chatgpt.com",
    "chat.chatgpt.com",
    "chatgpt.com",
    "claude.ai",
    "www.claude.ai",
    "api.anthropic.com",
    "anthropic.com",
    "gemini.google.com",
    "bard.google.com",
    "generativelanguage.googleapis.com",
    "ai.google.dev",
    "copilot.microsoft.com",
    "bing.com",
    "www.bing.com",
    "edgeservices.bing.com",
    "sydney.bing.com",
    "perplexity.ai",
    "www.perplexity.ai",
    "chat.perplexity.ai",
    "api.perplexity.ai",
    "cdn.perplexity.ai",
    "www2.perplexity.ai",
    "poe.com",
    "www.poe.com",
    "x.ai",
    "grok.x.ai",
    "api.x.ai",
    "grok.com",
    "huggingface.co",
    "www.huggingface.co",
    "api-inference.huggingface.co",
    "stability.ai",
    "api.stability.ai",
    "midjourney.com",
    "www.midjourney.com",
    "character.ai",
    "www.character.ai",
    "janitorai.com",
    "you.com",
    "phind.com",
    "deepai.org",
    "deepseek.com",
    "chat.deepseek.com",
    "playgroundai.com",
    "civitai.com",
    "replicate.com",
    "runpod.io",
    "vercel.app",
    "together.ai",
    "cohere.ai",
    "pizzagpt.it",
    "www.pizzagpt.it"
]

def main():
    # Controllo dei privilegi di amministratore
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Esegui questo script come amministratore!")
        return

    # Leggi il file hosts e filtra le righe
    try:
        with open(hosts_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        new_lines = [
            line for line in lines
            if not any(domain in line for domain in domains_to_remove)
        ]

        # Riscrivi il file hosts senza le righe da rimuovere
        with open(hosts_path, "w", encoding="utf-8") as file:
            file.writelines(new_lines)

        print("Hosts aggiornato: record AI rimossi con successo!")
    except PermissionError:
        print("Errore di permessi: esegui come amministratore.")
        return

    # Flush DNS
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("Cache DNS svuotata.")
    except subprocess.CalledProcessError:
        print("Errore durante il flush della cache DNS.")

if __name__ == "__main__":
    main()