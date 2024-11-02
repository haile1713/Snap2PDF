import tkinter as tk
from tkinter import filedialog
import os 

class ImageToPDFConverter :
    def __init__(self,root):
        self.root = root
        self.image_paths=[]
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)

        