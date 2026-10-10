import speech_recognition as sr
import pyttsx3

def test_text_to_speech():
    print("\nTesting Text-to-Speech...")
    try:
        engine = pyttsx3.init()
        
        # تحسين جودة الصوت
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # استخدام صوت أنثوي
        engine.setProperty('rate', 150)  # سرعة الكلام
        engine.setProperty('volume', 1.0)  # مستوى الصوت
        
        engine.say("مرحباً، هذا اختبار لنظام تحويل النص إلى كلام")
        engine.runAndWait()
        print("Text-to-Speech test successful!")
    except Exception as e:
        print(f"Text-to-Speech error: {str(e)}")

def test_microphone():
    print("\nTesting Microphone...")
    try:
        r = sr.Recognizer()
        
        # عرض جميع الميكروفونات المتاحة
        print("\nAvailable microphones:")
        for i, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"{i}: {name}")
        
        # اختيار الميكروفون
        mic_index = int(input("\nEnter the number of the microphone you want to use: "))
        
        with sr.Microphone(device_index=mic_index) as source:
            print("\nAdjusting for ambient noise... Please remain silent.")
            r.adjust_for_ambient_noise(source, duration=2)
            print("Ambient noise adjustment complete!")
            
            print("\nPlease speak something in Arabic...")
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            print("Audio captured! Processing...")
            
            # محاولة التعرف على الكلام باللغة العربية
            text = r.recognize_google(audio, language='ar-SA')
            print(f"You said: {text}")
            
            # تحويل النص إلى كلام
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            
    except sr.WaitTimeoutError:
        print("لم يتم اكتشاف أي كلام خلال فترة الانتظار")
    except sr.UnknownValueError:
        print("لم نتمكن من فهم الكلام")
    except sr.RequestError as e:
        print(f"حدث خطأ في الاتصال: {e}")
    except Exception as e:
        print(f"خطأ في الميكروفون: {str(e)}")

if __name__ == "__main__":
    print("Starting tests...")
    test_text_to_speech()
    test_microphone()
    print("\nAll tests completed!") 