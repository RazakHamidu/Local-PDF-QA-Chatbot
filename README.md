# Local PDF QA Chatbot

Questo progetto permette di interagire con un documento PDF locale ponendo domande in linguaggio naturale e ricevendo risposte generate da un modello linguistico di grandi dimensioni (LLM) eseguito localmente.

## Problema

Quando si utilizzano servizi LLM basati su cloud (come OpenAI GPT, Google Gemini, Anthropic Claude, ecc.) per analizzare o interrogare documenti, spesso è necessario inviare il contenuto di tali documenti ai server esterni. Questo solleva **preoccupazioni significative riguardo alla privacy e alla confidenzialità dei dati**, specialmente se i documenti contengono informazioni sensibili o proprietarie. Non si vuole che i propri dati vengano utilizzati da terze parti o che escano dal proprio controllo locale.

## Soluzione

Per risolvere il problema della privacy e garantire che i tuoi dati non lascino mai il tuo computer, questo progetto implementa un flusso di lavoro completamente locale:

1.  **Estrazione del Testo Locale**: Il testo viene letto direttamente dal file PDF presente sul tuo computer (`il_tuo_file.pdf` nel file `main.py` - **ricorda di modificarlo!**) utilizzando la libreria PyMuPDF. Nessun dato viene inviato all'esterno durante questa fase.
2.  **Elaborazione Locale con LLM**: La tua domanda e il testo estratto dal PDF vengono forniti come contesto a un modello linguistico (LLM, come `llama2`) che viene eseguito **interamente sulla tua macchina** grazie a Ollama. L'analisi e la generazione della risposta avvengono localmente, senza alcuna comunicazione con server cloud.
3.  **Interfaccia Utente Locale**: L'interfaccia per porre domande e visualizzare le risposte (creata con Gradio) viene eseguita anch'essa localmente nel tuo browser.

Questo approccio garantisce che l'intero processo, dall'analisi del PDF alla generazione della risposta, avvenga all'interno del tuo ambiente, **risolvendo così il problema della privacy** poiché nessun dato sensibile viene condiviso con servizi esterni.

## Tech Stack

Le tecnologie principali utilizzate in questo progetto sono:

*   **Python**: Linguaggio di programmazione principale.
*   **PyMuPDF**: Libreria per l'estrazione efficiente del testo dai file PDF.
*   **Ollama**: Piattaforma per eseguire modelli linguistici di grandi dimensioni (come Llama 2) **localmente**.
*   **Gradio**: Libreria per creare rapidamente interfacce utente web per modelli di machine learning.
*   **Llama 2**: Il modello linguistico specifico utilizzato (tramite Ollama) per generare le risposte.

---

### Installazione

1.  Clona il repository:
    ```bash
    git clone https://github.com/RazakHamidu/Local-PDF-QA-Chatbot.git
    cd Local-PDF-QA-Chatbot
    ```
2.  (Consigliato) Crea un ambiente virtuale:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
    ```
3.  Installa le dipendenze (crea prima un file `requirements.txt`):
    ```bash
    pip install pymupdf ollama gradio
    ```
    *(Se hai un file `requirements.txt`, usa: `pip install -r requirements.txt`)*
4.  Assicurati di avere Ollama installato e in esecuzione. Link a Ollama
5.  Scarica il modello Llama 2 per Ollama (o un altro modello supportato):
    ```bash
    ollama pull llama2
    ```

### Utilizzo

1.  **Modifica il percorso del PDF**: Apri il file `main.py` e cambia `"il_tuo_file.pdf"` nella funzione `chat_interface` con il percorso corretto del tuo file PDF.
2.  Esegui lo script principale:
    ```bash
    python main.py
    ```
3.  Apri il browser all'indirizzo fornito da Gradio (solitamente `http://127.0.0.1:7860`).
4.  Inserisci la tua domanda nella casella di testo e premi Invio o clicca sul pulsante di invio.

