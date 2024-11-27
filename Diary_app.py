import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import datetime

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("800x500")

        # Load background image
        self.background_image = Image.open("background.jpeg")
        self.background_image = self.background_image.resize((800, 500), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Set up background label with the image
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Transparent frame for entry container
        self.entry_frame = tk.Frame(self.root, bg="#ffffff", bd=5, relief="groove")
        self.entry_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=300)
        
        # Title label
        self.label = tk.Label(self.entry_frame, text="Write your diary entry:", font=("Helvetica", 16, "italic"),
                              bg="#ffffff", fg="#333333")
        self.label.pack(pady=10)

        # Text area with big, italic font
        self.text_area = tk.Text(self.entry_frame, wrap="word", font=("Helvetica", 14, "italic"), bg="#f0f0f0", fg="#333333")
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Customized Save button
        self.save_button = tk.Button(self.root, text="💾 Save Entry", command=self.save_entry,
                                     font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", 
                                     activebackground="#45a049", cursor="hand2")
        self.save_button.place(relx=0.5, rely=0.9, anchor="center")

    def save_entry(self):
        content = self.text_area.get("1.0", tk.END).strip()
        
        if not content:
            messagebox.showwarning("Warning", "Diary entry cannot be empty!")
            return
        
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        save_path = filedialog.asksaveasfilename(
            initialfile=f"Diary_{date}.txt",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if save_path:
            with open(save_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Saved", "Diary entry saved successfully!")
            self.text_area.delete("1.0", tk.END)

# Set up the main application window
def run_diary_app():
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    run_diary_app()
