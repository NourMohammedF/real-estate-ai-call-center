import tkinter as tk
from tkinter import messagebox
import call_handler
import os
import pygame
import threading
import queue

AUDIO_OUTPUT = "audio/output/response.wav"

class VoiceAssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("نظام المكالمات الذكي")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # متغيرات النص
        self.input_text = tk.StringVar()
        self.output_text = tk.StringVar()
        
        # حالة التسجيل
        self.is_recording = False
        self.recording_thread = None
        
        self.setup_gui()
        
    def setup_gui(self):
        """
        إعداد عناصر واجهة المستخدم
        """
        # العناوين
        tk.Label(self.root, text="🎙️ النص المستخرج:", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(self.root, textvariable=self.input_text, wraplength=450, justify="center", fg="blue").pack(pady=5)
        
        tk.Label(self.root, text="🤖 رد الذكاء الصناعي:", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(self.root, textvariable=self.output_text, wraplength=450, justify="center", fg="green").pack(pady=5)
        
        # زر التسجيل
        self.record_button = tk.Button(
            self.root,
            text="🎤 بدء الاستماع",
            command=self.toggle_recording,
            bg="lightblue",
            width=20
        )
        self.record_button.pack(pady=10)
        
        # حالة التسجيل
        self.status_label = tk.Label(self.root, text="", fg="gray")
        self.status_label.pack(pady=5)
        
    def toggle_recording(self):
        """
        تبديل حالة التسجيل
        """
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()
    
    def start_recording(self):
        """
        بدء التسجيل في خيط منفصل
        """
        self.is_recording = True
        self.record_button.config(text="⏹️ إيقاف الاستماع", bg="pink")
        self.status_label.config(text="جاري الاستماع...", fg="green")
        
        # بدء التسجيل في خيط منفصل
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.daemon = True
        self.recording_thread.start()
    
    def stop_recording(self):
        """
        إيقاف التسجيل
        """
        self.is_recording = False
        self.record_button.config(text="🎤 بدء الاستماع", bg="lightblue")
        self.status_label.config(text="تم إيقاف الاستماع", fg="gray")
    
    def record_audio(self):
        """
        تسجيل الصوت في خيط منفصل
        """
        try:
            call_handler.run_call()
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التسجيل: {str(e)}")
            self.stop_recording()
    
    def run(self):
        """
        تشغيل الواجهة
        """
        self.root.mainloop()

if __name__ == "__main__":
    app = VoiceAssistantGUI()
    app.run()
