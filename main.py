import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import torch
import os
from dotenv import load_dotenv

class RealEstateAssistant:
    def __init__(self):
        print("Initializing Real Estate Assistant...")
        
        print("Initializing Text-to-Speech engine...")
        # تهيئة محرك تحويل النص إلى كلام
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # اختيار الصوت الافتراضي
        self.engine.setProperty('rate', 150)  # سرعة الكلام
        self.engine.setProperty('volume', 0.9)  # مستوى الصوت
        print("Text-to-Speech engine initialized successfully!")
        
        print("Initializing Speech Recognition...")
        # تهيئة التعرف على الصوت
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 3000  # تخفيض حساسية الميكروفون
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        
        # Test microphone
        try:
            with sr.Microphone() as source:
                print("Microphone initialized successfully!")
                print("Available microphones:")
                for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
                    print(f"{i}: {microphone_name}")
                print("\nAdjusting for ambient noise... Please remain silent.")
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                print("Ambient noise adjustment complete!")
        except Exception as e:
            print(f"Error initializing microphone: {str(e)}")
            raise
        
        print("Initializing Language Model...")
        # تهيئة نموذج اللغة المحلي
        try:
            self.qa_model = pipeline(
                "question-answering",
                model="deepset/roberta-base-squad2",
                device=0 if torch.cuda.is_available() else -1
            )
            print("Language Model initialized successfully!")
        except Exception as e:
            print(f"Error initializing language model: {str(e)}")
            raise
        
        # سياق العقارات
        self.context = """
        We are a real estate company specializing in buying, selling, and renting properties.
        We offer our services in various residential and commercial areas.
        We have a diverse portfolio of properties available for sale and rent.
        We can help you find the right property for your needs.
        
        Starting prices:
        - Apartments: $500,000
        - Villas: $2,000,000
        - Commercial Shops: $1,000,000
        
        Coverage areas:
        - New Cairo
        - Sheikh Zayed
        - Fifth Settlement
        - Nasr City
        - Maadi
        
        You can visit our website: www.realestate.com
        Or contact us at: 01234567890
        """
        print("Real Estate Assistant initialized successfully!")
    
    def listen(self):
        """الاستماع إلى صوت المستخدم وتحويله إلى نص"""
        with sr.Microphone() as source:
            print("\nListening... Speak now!")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Audio captured! Processing...")
                text = self.recognizer.recognize_google(audio, language="en-US")
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected within timeout period")
                return None
            except sr.UnknownValueError:
                print("Could not understand the audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None
            except Exception as e:
                print(f"Error in speech recognition: {str(e)}")
                return None
    
    def speak(self, text):
        """تحويل النص إلى كلام"""
        print(f"\nAssistant: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech synthesis: {str(e)}")
    
    def process_question(self, question):
        """معالجة السؤال وتوليد الإجابة"""
        try:
            print(f"\nProcessing question: {question}")
            result = self.qa_model(question=question, context=self.context)
            print(f"Generated answer: {result['answer']}")
            return result['answer']
        except Exception as e:
            print(f"Error processing question: {str(e)}")
            return "I apologize, but I couldn't process your question. Could you please rephrase it?"
    
    def run(self):
        """تشغيل المساعد"""
        print("\nStarting the assistant...")
        welcome_message = "Hello! I'm your real estate assistant. How can I help you today?"
        print(welcome_message)
        self.speak(welcome_message)
        
        while True:
            question = self.listen()
            if question:
                if "goodbye" in question.lower() or "bye" in question.lower():
                    farewell = "Thank you for your time. Have a great day!"
                    self.speak(farewell)
                    break
                
                answer = self.process_question(question)
                self.speak(answer)

if __name__ == "__main__":
    try:
        print("Starting the Real Estate Assistant application...")
        assistant = RealEstateAssistant()
        assistant.run()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        print("Please make sure all requirements are installed and the microphone is properly connected.")