import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        # تحسين جودة الصوت
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # استخدام صوت أنثوي
        self.engine.setProperty('rate', 150)  # سرعة الكلام
        self.engine.setProperty('volume', 1.0)  # مستوى الصوت

    def speak(self, text):
        """تحويل النص إلى كلام"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return True
        except Exception as e:
            print(f"خطأ في تحويل النص إلى كلام: {str(e)}")
            return False

if __name__ == "__main__":
    sample_text = "مرحبًا! كيف يمكنني مساعدتك اليوم؟"
    tts = TextToSpeech()
    tts.speak(sample_text)
    print("🔊 تم حفظ الصوت في", "audio/output/response.wav")
