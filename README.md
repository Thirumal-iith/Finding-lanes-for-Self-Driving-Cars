# Finding Lanes for Self-Driving Cars

## Overview

This project implements a lane detection system for self-driving cars using computer vision techniques. It processes video footage to detect and highlight lane lines, helping autonomous vehicles stay on the road.

## Features

- Edge detection using the Canny method
- Region of interest selection
- Line detection using the Hough Transform
- Averaged slope and intercept calculation for smooth lane lines
- Real-time lane detection on video footage

## Project Structure

- **main.py**: The core Python script containing all the functions for lane detection.
- **test\_image.jpg**: Example image for testing lane detection.
- **test2.mp4**: Example video for testing real-time lane detection.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.7 or higher
- OpenCV
- NumPy
- Matplotlib

Install dependencies using the command:

```bash
pip install opencv-python numpy matplotlib
```

## How It Works

1. **Canny Edge Detection**: Identifies edges in the input image or video by detecting strong gradients.
2. **Region of Interest**: Masks the irrelevant parts of the image to focus on the road area.
3. **Hough Transform**: Detects straight lines in the masked image and transforms them into lane lines.
4. **Averaging**: Computes an averaged slope and intercept for smoother lane lines.
5. **Overlay**: Draws the detected lane lines on the original image or video.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Thirumal-iith/finding-lanes-self-driving-cars.git
cd finding-lanes-self-driving-cars
```

2. Replace `test_image.jpg` or `test2.mp4` with your own test images or videos if desired.

3. Run the Python script:

```bash
python main.py
```

4. For real-time lane detection from a video file, press `q` to quit the display window.

## Code Walkthrough

### Key Functions

1. **`canny(image)`**:

   - Converts the image to grayscale.
   - Applies Gaussian blur to reduce noise.
   - Performs Canny edge detection.

2. **`region_of_interest(image)`**:

   - Defines a triangular region covering the road.
   - Masks irrelevant areas outside the region of interest.

3. **`display_lines(image, lines)`**:

   - Draws detected lines on a black image.

4. **`averaged_slope_intercept(image, lines)`**:

   - Calculates the averaged slope and intercept for left and right lane lines.
   - Returns smoothed lane lines.

5. **`make_coordinates(image, line_parameters)`**:

   - Converts slope and intercept into start and end coordinates for drawing lines.

### Hough Transform

The script uses the probabilistic Hough Transform to detect lines. It divides the image into bins and identifies the best-fit line based on the maximum number of votes.

### Video Processing

The script processes each frame of the video in real time:

- Detects edges
- Masks the region of interest
- Finds lane lines
- Overlays lane lines on the original frame

## Example

Run the script and observe the detected lane lines overlayed on the video:



## Future Enhancements

- Implement curve detection for non-linear roads.
- Add functionality for detecting lane changes.
- Optimize for better performance on higher resolution videos.


## Author

Thirumalesh ([GitHub Profile](https://github.com/Thirumal-iith))

