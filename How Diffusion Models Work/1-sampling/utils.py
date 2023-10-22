import torch
import torchvision
import matplotlib.pyplot as plt

def display_grid_images(tensor, nrow=8):
    # Convert the tensor to a grid of images
    grid_image = torchvision.utils.make_grid(tensor, nrow=nrow)

    # Convert the grid image to numpy array
    grid_image_np = grid_image.numpy().transpose((1, 2, 0))

    # Display the grid image using matplotlib
    plt.imshow(grid_image_np)
    plt.axis('off')
    plt.show()