import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize NLTK data
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    try:
        pdf = PyPDF2.PdfFileReader(open(file_path, 'rb'))
        text = ''
        for page in range(pdf.numPages):
            text += pdf.getPage(page).extractText()
        return text
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file path.")
        return None

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]  # Remove non-alphabetic tokens
    tokens = [t.lower() for t in tokens]  # Convert to lowercase
    tokens = [t for t in tokens if t not in stop_words]  # Remove stop words
    tokens = [stemmer.stem(t) for t in tokens]  # Stem words
    return tokens

# Function to answer questions
def answer_question(question, text):
    question_tokens = preprocess_text(question)
    text_tokens = preprocess_text(text)
    for token in question_tokens:
        if token in text_tokens:
            return 'Yes'
    return 'No'

# Tkinter GUI
def main():
    root = tk.Tk()
    root.title("PDF Reader and Question Answering System")

    # PDF file upload
    def upload_pdf_file():
        file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
        entry_pdf_file.delete(0, tk.END)
        entry_pdf_file.insert(0, file_path)

    # Answer question
    def answer():
        file_path = entry_pdf_file.get()
        text = extract_text_from_pdf(file_path)
        if text:
            question = entry_question.get()
            answer = answer_question(question, text)
            label_answer.config(text=answer)

    # GUI layout
    label_pdf_file = tk.Label(root, text="Upload PDF File:")
    label_pdf_file.grid(row=0, column=0, padx=5, pady=5)

    entry_pdf_file = tk.Entry(root, width=50)
    entry_pdf_file.grid(row=0, column=1, padx=5, pady=5)

    button_upload_pdf = tk.Button(root, text="Upload", command=upload_pdf_file)
    button_upload_pdf.grid(row=0, column=2, padx=5, pady=5)

    label_question = tk.Label(root, text="Enter Question:")
    label_question.grid(row=1, column=0, padx=5, pady=5)

    entry_question = tk.Entry(root, width=50)
    entry_question.grid(row=1, column=1, padx=5, pady=5)

    button_answer = tk.Button(root, text="Answer", command=answer)
    button_answer.grid(row=1, column=2, padx=5, pady=5)

    label_answer = tk.Label(root, text="")
    label_answer.grid(row=2, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()