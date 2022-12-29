from tkinter import *
from tkinter import filedialog
import pyttsx3, PyPDF2


ventana = Tk()
ventana.title("PDF A MP3")
ventana.geometry("100x100+10+10")
ventana.resizable(width=False, height=False)
pdfFile = None
clean_text = ""

def seleccionar_pdf():
    global pdfFile
    pdfFile = filedialog.askopenfilename(title="abrir", filetypes=(("Archivos PDF", "*.pdf"), ("all files", "*.*")))
    print(pdfFile)
    ventana.quit()

ventana.mainloop()



pdfreader = PyPDF2.PdfReader((pdfFile), "rb")
speaker = pyttsx3.init()

for page_num in range (len(pdfreader.pages) ):
    text = pdfreader.pages[page_num].extract_text()
    clean_text += text.strip().replace("\n", " ")

print(clean_text)
speaker.save_to_file(clean_text, "audio.mp3")
speaker.runAndWait()
speaker.stop()