import pymupdf # Importa la libreria pymupdf per l'elaborazione dei file PDF.
import ollama # Importa la libreria ollama per interagire con i modelli LLM locali.
import gradio as gr # Importa la libreria gradio per creare l'interfaccia utente.

def extract_text_from_pdf(pdf_path):
    """
    Estrae il testo da un file PDF utilizzando pymupdf.

    Args:
        pdf_path (str): Il percorso del file PDF.

    Returns:
        str: Il testo estratto dal PDF, o una stringa vuota in caso di errore.
    """
    text = "" # Inizializza una stringa vuota per accumulare il testo estratto.
    try:
        pdf_document = pymupdf.open(pdf_path) # Apre il file PDF utilizzando pymupdf.
        for page_num in range(pdf_document.page_count): # Itera attraverso ogni pagina del PDF.
            page = pdf_document[page_num] # Ottiene l'oggetto pagina corrente.
            text += page.get_text() # Estrae il testo dalla pagina e lo aggiunge alla stringa 'text'.
        pdf_document.close() # Chiude il file PDF.
    except Exception as e:
        print(f"Errore durante l'estrazione del testo dal PDF: {e}") # Stampa un messaggio di errore se si verifica un'eccezione.
    return text # Restituisce il testo estratto.

def chat_with_llm(prompt, context):
    """
    Invia un prompt all'LLM e restituisce la risposta.

    Args:
        prompt (str): La domanda o l'input dell'utente.
        context (str): Il contesto fornito all'LLM (il testo estratto dal PDF).

    Returns:
        str: La risposta dell'LLM, o un messaggio di errore in caso di problemi.
    """
    try:
        response = ollama.chat(model='llama2', messages=[ # Invia un messaggio all'LLM 'llama2'.
            {'role': 'system', 'content': context}, # Fornisce il contesto all'LLM come messaggio di sistema.
            {'role': 'user', 'content': prompt} # Invia la domanda dell'utente all'LLM.
        ])
        return response['message']['content'] # Restituisce il contenuto della risposta dell'LLM.
    except Exception as e:
        return f"Errore durante la comunicazione con l'LLM: {e}" # Restituisce un messaggio di errore se la comunicazione fallisce.

def chat_interface(user_input):
    """
    Interfaccia di chat di Gradio.

    Args:
        user_input (str): L'input dell'utente dalla chat.

    Returns:
        str: La risposta dell'LLM.
    """
    context = extract_text_from_pdf("il_tuo_file.pdf") # Estrae il testo dal PDF e lo utilizza come contesto.
    response = chat_with_llm(user_input, context) # Ottiene la risposta dall'LLM.
    return response # Restituisce la risposta per visualizzarla nell'interfaccia.

iface = gr.Interface(fn=chat_interface, inputs="text", outputs="text") # Crea un'interfaccia Gradio con una casella di input di testo e una casella di output di testo.
iface.launch() # Avvia l'interfaccia Gradio.