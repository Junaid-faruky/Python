from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

url = input("Enter image URL: ")
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)
print("Caption:", processor.decode(out[0], skip_special_tokens=True))
