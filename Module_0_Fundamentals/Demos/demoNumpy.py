from PIL import Image
import numpy as np

# Load the image
image = Image.open('Module_0_Fundamentals/Demos/Selfie.jpg')

# Convert the image to grayscale if necessary
grayscale_image = image.convert('L')

# Resize the grayscale image to 500x500 pixels
grayscale_image = grayscale_image.resize((500, 500))

# Convert the image to a NumPy array
image_array = np.array(grayscale_image)

# Display the shape of the array
print("Shape of the image array:", image_array.shape)

# Display the image array
print("Image array:")
print(image_array)

# TODO: Review the error code: TypeError: color must be int or single-element tuple on line 29 
# img = Image.new('1', (500, 500))
# pixels = img.load()

# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         pixels[i, j] = image_array[i][j]

# for i in range(image_array.shape[0]):
#     for j in range(image_array.shape[1]):
#         pixels[i, j] = image_array[i][j]


# Save the grayscale image
grayscale_image.show()
grayscale_image.save('Module_0_Fundamentals/Demos/Selfie_Grayscale.jpg')

# img.show()
# img.save('Module_0_Fundamentals/Demos/Selfie_New.jpg')