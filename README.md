# YOLO-Based Automated Mouse Control Bot

This project implements an automated bot using the YOLO object detection model to identify and interact with objects on the screen via simulated mouse movements. The bot captures screenshots, processes them with the YOLO model, identifies safe targets (fruits), and simulates mouse actions to interact with them while avoiding hazardous objects (bombs).

## Features

- Uses a YOLO model for object detection to distinguish between fruits and bombs.
- Simulates mouse movements and actions to "slice" detected fruits while avoiding bombs.
- Continuously takes screenshots of the screen to identify and interact with objects in real time.
- Utilizes threading for concurrent screenshot capture and processing.

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `ultralytics` (for YOLO model)
  - `keyboard` (for key event handling)
  - `threading` (for managing concurrent tasks)
  - `bettercam` (for capturing screenshots)
  - `pynput` (for mouse control)
  - `numpy` (for numerical operations)
  - `opencv-python` (for image display and manipulation)
  - `torch` (for running the YOLO model)

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:

   ```bash
   pip install ultralytics keyboard pynput numpy opencv-python torch
   ```

3. Ensure you have a compatible YOLO model (`bestv5.pt`) in the working directory.

## Usage

1. **Run the Bot**: Execute the script using Python:

   ```bash
   python main.py
   ```

2. **Start and Stop**: The bot starts automatically and continues to run until you press the `q` key.

## Script Overview

### Key Functions

- **initialize_bomb_bbox(x1, y1, x2, y2):** Initializes a numpy array representing a bomb's bounding box coordinates.
  
- **is_within_bomb(fruit_box, bomb_list):** Checks if any corner of a fruit's bounding box is within any bomb's bounding box.

- **determine_safe_fruits(fruits, bombs):** Determines which fruits are safe to slice by checking if they overlap with any bombs.

- **move_mouse(radius, num_steps):** Moves the mouse in a circular pattern around its current position.

- **run_bot(safe_fruits):** Simulates mouse actions to slice safe fruits by moving the mouse to fruit locations and performing slicing motions.

- **take_screenshot(stop_event, model, device):** Continuously captures screenshots and processes them using the YOLO object detection model to identify fruits and bombs.

- **load_model(device):** Loads the YOLO model for object detection and warms it up with dummy data.

### Main Flow

1. **Load Model:** Loads a pre-trained YOLO model for object detection.
2. **Start Screenshot Thread:** A separate thread is started to continuously capture screenshots and process them using the loaded model.
3. **Detect and Slice Fruits:** The bot identifies safe fruits and simulates mouse actions to slice them while avoiding bombs.
4. **Stop the Bot:** Press `q` to stop the bot and terminate the screenshot thread.

## Notes

- The bot requires a YOLO model trained to distinguish between "fruit" and "bomb" classes. Adjust the model paths and class names as needed.
- Ensure the screen resolution and region settings match your setup (`region=(0, 0, 1920, 1080)` for screenshots).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
