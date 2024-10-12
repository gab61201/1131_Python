import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "clipboard"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], check=True)
subprocess.check_call(["playwright", "install", "chromium"])

