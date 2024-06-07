import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["tkinter"]

# Check and install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

# Run the main application
subprocess.run([sys.executable, "flashcard_app.py"])
