import speech_recognition as sr
import time

def listen_continuously():
    """
    الاستماع المستمر للصوت وتحويله إلى نص.
    """
    recognizer = sr.Recognizer()
    
    # ضبط إعدادات الميكروفون
    recognizer.energy_threshold = 3000  # حساسية اكتشاف الصوت
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8  # المدة بين الجمل
    
    print("🎤 جاري الاستماع... (اضغط Ctrl+C للإيقاف)")
    
    with sr.Microphone() as source:
        # ضبط مستوى الضوضاء المحيطة
        print("⚙️ ضبط مستوى الضوضاء المحيطة...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("✅ تم ضبط مستوى الضوضاء!")
        
        while True:
            try:
                print("\n👂 جاري الاستماع...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                print("🔍 جاري تحليل الصوت...")
                
                # محاولة التعرف على الكلام باللغة العربية
                text = recognizer.recognize_google(audio, language='ar-SA')
                print(f"🗣️ تم التعرف على: {text}")
                
                # هنا يمكنك إضافة المزيد من المعالجة للنص
                process_text(text)
                
            except sr.UnknownValueError:
                print("❌ لم يتم التعرف على الكلام")
            except sr.RequestError as e:
                print(f"❌ خطأ في الاتصال بخدمة Google Speech Recognition: {e}")
            except KeyboardInterrupt:
                print("\n⚡ تم إيقاف الاستماع")
                break
            except Exception as e:
                print(f"❌ حدث خطأ: {str(e)}")
                time.sleep(1)  # انتظار قليلاً قبل المحاولة مرة أخرى

def process_text(text):
    """
    معالجة النص المستخرج من الصوت
    """
    # هنا يمكنك إضافة المنطق الخاص بمعالجة النص
    # مثل: تحليل الطلب، الرد على العميل، إلخ
    pass

if __name__ == "__main__":
    listen_continuously()
