import os
import time
import threading
import subprocess
from blackboxai import BlackBoxAI  # Pastikan Anda telah menginstal blackboxai

class ShellBot:
    def execute_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"

class Jarvis:
    def __init__(self):
        self.ai = BlackBoxAI()  # Inisialisasi blackboxai
        self.shell_bot = ShellBot()
        self.running = True

    def display_status(self):
        while self.running:
            os.system('clear')  # Gunakan 'cls' untuk Windows
            time.sleep(5)

    def chat(self):
        print("Ketik 'exit' untuk keluar.")
        while self.running:
            user_input = input("Anda: ")
            if user_input.lower() == 'exit':
                self.running = False
                break
            
            # Menggunakan blackboxai untuk mendapatkan respons
            response = self.ai.get_response(user_input)  # Ganti dengan metode yang sesuai dari blackboxai
            print(f"Jarvis: {response}")

            # Eksekusi perintah shell jika respons mengandungnya
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
