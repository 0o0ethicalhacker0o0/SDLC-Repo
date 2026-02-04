import subprocess
import sys

def run_cmd(user_input):
    # Intentionally insecure for demo purposes
    subprocess.call("echo " + user_input, shell=True)

if __name__ == "__main__":
    run_cmd(sys.argv[1])
