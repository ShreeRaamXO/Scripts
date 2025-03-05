import time
import random
import pyautogui
import subprocess

EDGE_PATH = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

def load_phrases(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def open_edge():
    subprocess.Popen([EDGE_PATH])
    time.sleep(5)  # Wait for Edge to open

def search_with_typing(phrases, min_delay=1, max_delay=10):
    for phrase in phrases:
        pyautogui.click(300, 60)  # Click on the address bar (Adjust based on screen resolution)
        time.sleep(1)
        pyautogui.write(phrase, interval=0.05)
        pyautogui.press("enter")
        time.sleep(random.randint(min_delay, max_delay))

if __name__ == "__main__":
    phrases = load_phrases(r"C:\Users\anuga\Documents\GitHub\Scripts\microsoft  search\topPhrases.txt")
    if phrases:
        open_edge()
        search_with_typing(phrases)
    else:
        print("No phrases found in the file.")
