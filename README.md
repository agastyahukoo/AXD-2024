## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/agastyahukoo/OpenCV-Drone.git
   cd OpenCV-Drone
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script and select a task:

```bash
python main.py
```

When prompted:

```
Select a task to execute:
1. Task 1
2. Task 2
3. Task 3
4. Task 4
Q. Quit
Enter your choice (1-4) or 'Q' to quit:
```

### Task 1: Shape Detection and Tracking

Detects and tracks red shapes (circles, squares, rectangles, triangles) in real-time.

## Project Structure

```
OpenCV-Drone/
├── main.py
├── requirements.txt
├── README.md
├── tasks/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
└── utils/
    ├── centroid_tracker.py
    └── image_processing.py
```

## Calibration

Adjust HSV color thresholds in `utils/image_processing.py` to match your environment:

```python
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])
```

## Troubleshooting

- **Camera Issues**: Ensure the webcam is connected and not in use by other applications.
- **Detection Issues**: Adjust HSV thresholds, ensure consistent lighting, and use a plain background.
- **Dependencies**: Verify all required Python packages are installed.
