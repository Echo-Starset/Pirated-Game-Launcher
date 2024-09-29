import tkinter as tk
import subprocess
import sys
import threading

# Expanded list of common libraries
libraries = [
    'numpy', 'pandas', 'requests', 'matplotlib', 'scikit-learn',
    'tensorflow', 'keras', 'flask', 'django', 'beautifulsoup4',
    'scrapy', 'seaborn', 'plotly', 'opencv-python', 'pillow',
    'pytest', 'pytest-cov', 'jupyter', 'notebook', 'sympy',
    'nltk', 'spacy', 'scipy', 'pyyaml', 'sqlalchemy',
    'pydantic', 'fastapi', 'dash', 'bokeh', 'imageio',
    'pyqt5', 'tkinter', 'websocket-client', 'paramiko', 'paho-mqtt',
    'pyodbc', 'cx_Oracle', 'tensorflow-gpu', 'lxml',
    'cryptography', 'asyncio', 'twisted', 'Flask-SocketIO',
    'tqdm', 'rich', 'Cython', 'imageio[ffmpeg]',
    'requests-oauthlib', 'pytest-django', 'python-dotenv',
    'psycopg2', 'pygame', 'matplotlib', 'statsmodels',
    'plotnine', 'geopandas', 'shapely', 'fastapi', 'sqlalchemy',
    'scrapy', 'selenium', 'beautifulsoup4', 'moviepy',
    'pyinstaller', 'watchdog', 'pytest-bdd', 'Flask-RESTful',
    'gunicorn', 'Flask-Mail', 'Flask-Admin', 'Flask-WTF',
    'werkzeug', 'sqlalchemy-utils', 'flask-cors', 'requests-html',
    # Add more libraries as needed
]

def install_libraries():
    status_label.config(text="Starting installation...")
    for library in libraries:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])
            status_label.config(text=f"Installed: {library}")
        except subprocess.CalledProcessError:
            status_label.config(text=f"Failed to install: {library}")
            return
    status_label.config(text="All installations complete!")

def start_installation():
    threading.Thread(target=install_libraries, daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Library Installer")
root.configure(bg='grey')  # Set background color to grey
root.geometry("500x400")  # Set width and height (width x height)

# Create a start button with green background
start_button = tk.Button(root, text="Start", command=start_installation, padx=20, pady=10, bg='green')
start_button.pack(pady=20)

# Status label
status_label = tk.Label(root, text="", bg='grey')  # Set label background to grey
status_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
