import os
import subprocess

# Percorso del file hosts su Windows
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Testo da aggiungere
hosts_entries = """

# BLOCCO SERVIZI AI
0.0.0.0 chat.openai.com
0.0.0.0 auth.openai.com
0.0.0.0 platform.openai.com
0.0.0.0 api.openai.com
0.0.0.0 openai.com
0.0.0.0 www.openai.com
0.0.0.0 www.chatgpt.com
0.0.0.0 chat.chatgpt.com
0.0.0.0 chatgpt.com
127.0.0.1 chat.openai.com
127.0.0.1 auth.openai.com
127.0.0.1 platform.openai.com

0.0.0.0 claude.ai
0.0.0.0 www.claude.ai
0.0.0.0 api.anthropic.com
0.0.0.0 anthropic.com
127.0.0.1 claude.ai

0.0.0.0 gemini.google.com
0.0.0.0 bard.google.com
0.0.0.0 generativelanguage.googleapis.com
0.0.0.0 ai.google.dev
127.0.0.1 gemini.google.com

0.0.0.0 copilot.microsoft.com
0.0.0.0 bing.com
0.0.0.0 www.bing.com
0.0.0.0 edgeservices.bing.com
0.0.0.0 sydney.bing.com
127.0.0.1 copilot.microsoft.com

0.0.0.0 perplexity.ai
0.0.0.0 www.perplexity.ai
0.0.0.0 chat.perplexity.ai
0.0.0.0 api.perplexity.ai
0.0.0.0 cdn.perplexity.ai
0.0.0.0 www2.perplexity.ai

127.0.0.1 perplexity.ai
127.0.0.1 www.perplexity.ai

0.0.0.0 poe.com
0.0.0.0 www.poe.com
127.0.0.1 poe.com

0.0.0.0 x.ai
0.0.0.0 grok.x.ai
0.0.0.0 api.x.ai
0.0.0.0 grok.com
127.0.0.1 x.ai

0.0.0.0 huggingface.co
0.0.0.0 www.huggingface.co
0.0.0.0 api-inference.huggingface.co
127.0.0.1 huggingface.co

0.0.0.0 stability.ai
0.0.0.0 api.stability.ai
127.0.0.1 stability.ai

0.0.0.0 midjourney.com
0.0.0.0 www.midjourney.com
127.0.0.1 midjourney.com

0.0.0.0 character.ai
0.0.0.0 www.character.ai
127.0.0.1 character.ai

0.0.0.0 janitorai.com
127.0.0.1 janitorai.com

0.0.0.0 you.com
127.0.0.1 you.com

0.0.0.0 phind.com
127.0.0.1 phind.com

0.0.0.0 deepai.org
127.0.0.1 deepai.org

0.0.0.0 deepseek.com
127.0.0.1 deepseek.com

0.0.0.0 chat.deepseek.com
127.0.0.1 chat.deepseek.com
0.0.0.0 playgroundai.com
127.0.0.1 playgroundai.com

0.0.0.0 civitai.com
127.0.0.1 civitai.com

0.0.0.0 replicate.com
127.0.0.1 replicate.com

0.0.0.0 runpod.io
127.0.0.1 runpod.io

0.0.0.0 vercel.app
127.0.0.1 vercel.app

0.0.0.0 together.ai
127.0.0.1 together.ai

0.0.0.0 cohere.ai
127.0.0.1 cohere.ai

0.0.0.0 pizzagpt.it
0.0.0.0 www.pizzagpt.it
0.0.0.0 www.google.com
0.0.0.0 google.com
0.0.0.0 www.use.ai
0.0.0.0 use.ai
"""

def main():
    # Verifica dei privilegi di amministratore
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Esegui questo script come amministratore!")
        return

    # Apre il file hosts in modalità append
    try:
        with open(hosts_path, "a", encoding="utf-8") as file:
            file.write(hosts_entries)
        print("Hosts aggiornato con successo!")
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
    import ctypes
    main()