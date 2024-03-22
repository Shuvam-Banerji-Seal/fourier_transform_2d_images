import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Button, Label, IntVar, Checkbutton
import pygame

# Initialize pygame mixer for playing music
pygame.mixer.init()

def browse_file():
    Tk().withdraw()
    filename = filedialog.askopenfilename()
    return filename

def calculate_2dft(input):
    ft = np.fft.ifftshift(input)
    ft = np.fft.fft2(ft)
    return np.fft.fftshift(ft)

def calculate_2dift(input):
    ift = np.fft.ifftshift(input)
    ift = np.fft.ifft2(ift)
    ift = np.fft.fftshift(ift)
    return ift.real

def calculate_distance_from_centre(coords, centre):
    return np.sqrt(np.sum((np.array(coords) - centre) ** 2))

def find_symmetric_coordinates(coords, centre):
    return (centre + (centre - coords[0]),
            centre + (centre - coords[1]))

def display_plots(individual_grating, reconstruction, idx, original_image, ft):
    plt.subplot(221)
    plt.imshow(original_image)
    plt.title("Original Image")
    plt.axis("off")
    plt.subplot(222)
    plt.imshow(individual_grating)
    plt.title("Individual Grating")
    plt.axis("off")
    plt.subplot(223)
    plt.imshow(reconstruction)
    plt.title("Reconstructed Image")
    plt.axis("off")
    plt.subplot(224)
    plt.imshow(np.log(abs(ft)))
    plt.title("Fourier Transform")
    plt.axis("off")
    plt.suptitle(f"Terms: {idx}")
    plt.pause(0.01)

def perform_fourier_transform(image_filename, play_music=True):
    # Read and process image
    image = plt.imread(image_filename)
    original_image = image
    image = image[:, :, :3].mean(axis=2)  # Convert to grayscale

    # Array dimensions (array is square) and centre pixel
    array_size = min(image.shape)
    if array_size % 2 == 0:
        array_size -= 1

    # Crop image so it's a square image
    image = image[:array_size, :array_size]
    centre = (array_size - 1) / 2

    # Get all coordinate pairs in the left half of the array,
    # including the column at the centre of the array (which
    # includes the centre pixel)
    coords_left_half = [(x, y) for x in range(array_size) for y in range(int(centre) + 1)]

    # Sort points based on distance from centre
    coords_left_half.sort(key=lambda x: calculate_distance_from_centre(x, centre))

    plt.set_cmap("gray")

    ft = calculate_2dft(image)

    # Show grayscale image and its Fourier transform
    plt.subplot(121)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(np.log(abs(ft)))
    plt.title("Fourier Transform")
    plt.axis("off")
    plt.pause(2)

    # Play music if enabled
    if play_music:
        music_file = "your_music_file.mp3"  # Replace with your music file path
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

    # Reconstruct image
    fig = plt.figure()
    # Step 1
    # Set up empty arrays for final image and
    # individual gratings
    rec_image = np.zeros(image.shape)
    individual_grating = np.zeros(
        image.shape, dtype="complex"
    )
    idx = 0

    # All steps are displayed until display_all_until value
    display_all_until = 10  # Decreased value for faster appearance
    # After this, skip which steps to display using the
    # display_step value
    display_step = 1  # Decreased value for faster appearance
    # Work out index of next step to display
    next_display = display_all_until + display_step

    # Step 2
    for coords in coords_left_half:
        # Central column: only include if points in top half of
        # the central column
        if not (coords[1] == centre and coords[0] > centre):
            idx += 1
            symm_coords = find_symmetric_coordinates(
                coords, centre
            )
            # Step 3
            # Copy values from Fourier transform into
            # individual_grating for the pair of points in
            # current iteration
            individual_grating[coords] = ft[coords]
            individual_grating[int(symm_coords[0]), int(symm_coords[1])] = ft[int(symm_coords[0]), int(symm_coords[1])]

            # Step 4
            # Calculate inverse Fourier transform to give the
            # reconstructed grating. Add this reconstructed
            # grating to the reconstructed image
            rec_grating = calculate_2dift(individual_grating)
            rec_image += rec_grating

            # Clear individual_grating array, ready for
            # next iteration
            individual_grating[coords] = 0
            individual_grating[int(symm_coords[0]), int(symm_coords[1])] = 0

            # Display intermediate steps
            display_plots(rec_grating, rec_image, idx, original_image, ft)

            # Check if 1 second has passed
            if idx >= 10:
                plt.pause(0.1)

    plt.show()

# GUI setup
root = Tk()
root.title("Image Fourier Transform")
root.geometry("300x200")

instruction_text = "Please click the button below to open the file manager and select an image."
instruction_label = Label(root, text=instruction_text, wraplength=280)
instruction_label.pack(pady=10)

music_check_var = IntVar()
music_check = Checkbutton(root, text="Play Music", variable=music_check_var)
music_check.pack()

def open_file_manager():
    file_path = browse_file()
    if file_path:
        play_music = music_check_var.get()
        perform_fourier_transform(file_path, play_music)

open_file_button = Button(root, text="Open File Manager", command=open_file_manager)
open_file_button.pack(pady=20)

root.mainloop()
