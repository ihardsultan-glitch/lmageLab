


import tkinter as tk
from pathlib import Path
import shutil

def extract_file():
    source = Path(__file__).parent / "game.exe"
    destination = Path.home() / "Desktop" / "game.exe"
    shutil.copy2(source, destination)
    status.config(text="تم استخراج الملف إلى سطح المكتب")

app = tk.Tk()
app.title("My Application")
app.geometry("400x200")

tk.Label(app, text="ملفي المضمّن داخل التطبيق").pack(pady=30)

tk.Button(app, text="استخراج الملف", command=extract_file).pack()

status = tk.Label(app, text="")
status.pack(pady=20)

app.mainloop()
