# Fourier Transform Image Reconstruction

## Overview

This repository contains code for performing Fourier Transform-based image reconstruction. The algorithm takes an input image, applies Fourier Transform to it, decomposes the image into its frequency components, and reconstructs the image using a subset of these components.

## Functions

### `browse_file()`

#### Description:
This function opens a file dialog window using Tkinter, allowing the user to browse and select an image file from their system.

---

### `calculate_2dft(input)`

#### Description:
This function calculates the 2D Fourier Transform of an input image using CuPy for GPU-accelerated computation.

---

### `calculate_2dift(input)`

#### Description:
This function calculates the inverse 2D Fourier Transform of an input frequency spectrum to reconstruct the image.

---

### `calculate_distance_from_centre(coords, centre)`

#### Description:
This function calculates the distance of a point from the center of an image.

---

### `find_symmetric_coordinates(coords, centre)`

#### Description:
This function finds the symmetric coordinates of a point with respect to the center of an image.

---

### `display_plots(individual_grating, reconstruction, idx, original_image, ft)`

#### Description:
This function displays the intermediate steps and results of the Fourier Transform-based image reconstruction.

---

### `perform_fourier_transform(image_filename, play_music=True)`

#### Description:
This function orchestrates the entire process of Fourier Transform-based image reconstruction, including file loading, Fourier Transform computation, reconstruction, and visualization.

## Usage

To use the code:

1. Clone the repository:

```bash
git clone https://github.com/your-username/fourier-transform-image-reconstruction.git
Certainly! Below is the compiled content for the `README.md` file:

```
2. Navigate to the repository directory:

```bash
cd fourier-transform-image-reconstruction
```

3. Ensure you have all the dependencies installed (see [Dependencies](#dependencies)).
4. Run the Python script:

```bash
python main.py
```

5. The script will prompt you to select an image file. Once selected, it will perform Fourier Transform-based reconstruction and display the results.

## Dependencies

The code requires the following dependencies:

- Python (>=3.6)
- NumPy
- Matplotlib
- Tkinter (for GUI file selection)
- Pygame (for playing music)
- CuPy (for GPU-accelerated computing, optional)

Install the dependencies using pip:

```bash
pip install numpy matplotlib pygame cupy
```


Feel free to customize the content further based on your specific use case, audience, or preferences.
