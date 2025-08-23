from PIL import Image, ImageFilter

# Open an image (replace 'example.jpg' with a real file path)
# image = Image.open('example.jpg')
# For demonstration, let's create a new image instead
image = Image.new('RGB', (200, 200), color='red')

# Apply a filter
blurred_image = image.filter(ImageFilter.BLUR)

# Save the new image
blurred_image.save('blurred_image.jpg')
print("Image processed and saved!")
