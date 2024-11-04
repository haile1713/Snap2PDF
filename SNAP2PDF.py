import tkinter as tk
from tkinter import filedialog, ttk
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()

        # Set window properties
        self.root.title("Snap2PDF - Image to PDF Converter")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f0f0")

        self.initialize_ui()

    def initialize_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#4CAF50", pady=10)
        header_frame.pack(fill="x")

        title_label1 = tk.Label(header_frame, text="Snap2PDF", font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white")
        title_label1.pack()

        subtitle_label = tk.Label(header_frame, text="Image to PDF Converter", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        subtitle_label.pack()

        # Main Frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        # Select Images Button
        select_images_button = tk.Button(main_frame, text="Select Images", command=self.select_images, bg="#2196F3", fg="white", font=("Helvetica", 12))
        select_images_button.pack(pady=10)

        # Listbox for selected images
        self.selected_images_listbox = tk.Listbox(main_frame, selectmode=tk.MULTIPLE, height=10, font=("Helvetica", 10))
        self.selected_images_listbox.pack(pady=10, fill="both", expand=True)

        # PDF Name Entry
        label = tk.Label(main_frame, text="Enter output PDF name (optional):", bg="#f0f0f0", font=("Helvetica", 10))
        label.pack()

        pdf_name_entry = tk.Entry(main_frame, textvariable=self.output_pdf_name, width=40, justify='center', font=("Helvetica", 10))
        pdf_name_entry.pack(pady=5)

        # Convert Button
        convert_button = tk.Button(main_frame, text="Convert to PDF", command=self.convert_images_to_pdf, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        convert_button.pack(pady=20)

        # Footer
        footer_label = tk.Label(self.root, text="Developed by [Haileleul Fiseha]", bg="#f0f0f0", font=("Helvetica", 8), fg="gray")
        footer_label.pack(pady=10)

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images", filetypes=[("Image files", "*.png *.jpg *.jpeg")]
        )
        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)
        for image_path in self.image_paths:
            _, image_name = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_name)

    def convert_images_to_pdf(self):
        if not self.image_paths:
            return

        # Ask the user where to save the PDF
        output_pdf_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF As"
        )
        if not output_pdf_path:
            return  # User canceled the save dialog

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))

        for image_path in self.image_paths:
            img = Image.open(image_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            pdf.setFillColorRGB(1, 1, 1)  # White background
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()

def main():
    root = tk.Tk()
    converter = ImageToPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
