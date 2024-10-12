import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "clipboard"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
subprocess.check_call([sys.executable, '-m', 'playwright', 'install', 'chromium'])
input("\n\n安裝完成")
