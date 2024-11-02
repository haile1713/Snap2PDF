import tkinter as tk
from tkinter import filedialog
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        # Title Labels
        title_label1 = tk.Label(self.root, text="Snap2PDF", font=("helvetica", 16, "bold"))
        title_label2 = tk.Label(self.root, text="Image to PDF converter", font=("helvetica", 16, "bold"))
        title_label1.pack(pady=10)
        title_label2.pack(pady=10)

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("400x600")
    app = ImageToPDFConverter(root)  # Create an instance of ImageToPDFConverter
    root.mainloop()

if __name__ == "__main__":
    main()
