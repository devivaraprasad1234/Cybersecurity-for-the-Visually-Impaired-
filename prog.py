import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3
import qrcode
from PIL import Image
import hashlib

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Generate Secure QR Code with SHA-256
def generate_secure_qr():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "URL cannot be empty.")
        return
    hashed_url = hashlib.sha256(url.encode()).hexdigest()
    qr_data = f"{url}|{hashed_url}"
    qr = qrcode.make(qr_data)
    path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if path:
        qr.save(path)
        speak("Secure QR code saved successfully.")
        messagebox.showinfo("Success", "QR code generated and saved!")

# Detect Phishing using AI-inspired logic (keyword scanning)
def detect_phishing():
    content = phishing_text.get("1.0", tk.END).lower()
    keywords = ["login", "verify", "update", "confirm", "account", "bank", "password","open","urgent","request","Turnin","finanace"]
    threats = [k for k in keywords if k in content]
    if threats:
        speak("Warning. Phishing risk detected.")
        messagebox.showwarning("Phishing Alert", f"Suspicious words: {', '.join(threats)}")
    else:
        speak("No phishing content detected.")
        messagebox.showinfo("Safe", "No phishing content found.")

# Provide Audio Guide
def audio_guide():
    guide = ("Welcome to Secure Assist. "
             "You can generate secure QR codes for safe website access. "
             "Or paste text content to detect phishing attempts.")
    speak(guide)

# Build GUI
root = tk.Tk()
root.title("Secure Assist: Cybersecurity for Visually Impaired")
root.geometry("750x600")
root.configure(bg="white")

tk.Label(root, text="Secure QR Code Generator", bg="white", font=("Arial", 14, "bold")).pack(pady=10)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)
tk.Button(root, text="Generate Secure QR Code", command=generate_secure_qr, bg="green", fg="black").pack(pady=5)

tk.Label(root, text="Phishing Detection (Paste Email/Web Content)", bg="white", font=("Arial", 14, "bold")).pack(pady=15)
phishing_text = tk.Text(root, width=80, height=10)
phishing_text.pack(pady=5)
tk.Button(root, text="Scan for Phishing", command=detect_phishing, bg="red", fg="black").pack(pady=5)

tk.Button(root, text="🔊 Audio Guide", command=audio_guide, bg="blue", fg="black").pack(pady=20)

root.mainloop()
