# Hand Gesture Keyboard Controller

Detect finger counts from your webcam feed and map them to keyboard events.

## Features

- Detects 1–5 fingers in real time
- Maps gestures to arrow keys and spacebar
- Cross-platform (Windows, macOS, Linux)

## Prerequisites

- Python 3.7+
- Webcam
- OS permissions for screen control (for PyAutoGUI)

## Installation

1. Clone the repo
   git clone https://github.com/<your-username>/hand-gesture-controller.git cd hand-gesture-controller

2. Create and activate a virtual environment
   python -m venv env source env/bin/activate     # macOS/Linux .\env\Scripts\activate      # Windows

3. Install dependencies
   pip install -r requirements.txt

## Usage

Run the main script:
```bash
python gesture_controller.py
```

Controls:
- 1 finger → Right arrow key
- 2 fingers → Left arrow key
- 3 fingers → Up arrow key
- 4 fingers → Down arrow key
- 5 fingers → Spacebar
Press Esc to exit.

File Overview
- gesture_controller.py – Main application code
- requirements.txt – Python dependencies
- .gitignore – Common ignored files
- LICENSE – Project license
Contributing
- Fork the repository
- Create a feature branch (git checkout -b feature/foo)
- - Commit your changes (git commit -am 'Add foo feature')
- Push to the branch (git push origin feature/foo)
- Open a Pull Request
License
This project is licensed under the MIT License.

