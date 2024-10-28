import subprocess

class ShellBot:
    def execute_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"
