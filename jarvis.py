# jarvis.py
import os
import time
import threading
from blackboxai import AIResponder
from main import ShellBot

class Jarvis:
    def __init__(self):
        self.ai_responder = AIResponder()
        self.shell_bot = ShellBot()
        self.running = True

    def display_status(self):
        while self.running:
            os.system('clear')  # Untuk Linux/Mac, gunakan 'cls' untuk Windows
            print("=== Jarvis Assistant ===")
            print("Status Daya: ON")
            print("Status Internet: UP")
            print("Suhu Perangkat: 25°C")
            print("=========================")
            time.sleep(5)

    def chat(self):
        print("Ketik 'exit' untuk keluar.")
        while self.running:
            user_input = input("Anda: ")
            if user_input.lower() == 'exit':
                self.running = False
                break
            
            response = self.ai_responder.get_response(user_input)
            print(f"Jarvis: {response}")

            # Jika respons mengandung perintah shell, eksekusi
            if response.startswith("execute:"):
                command = response.split("execute:")[1].strip()
                command_result = self.shell_bot.execute_command(command)
                print(f"Command Result: {command_result}")

    def run(self):
        status_thread = threading.Thread(target=self.display_status)
        status_thread.start()
        self.chat()
        status_thread.join()

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
