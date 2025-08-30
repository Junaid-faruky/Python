import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from typing import Callable, List
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ImageProcessor:
    image: np.ndarray
    
    def __post_init__(self):
        if isinstance(self.image, (str, Path)):
            self.image = cv2.imread(str(self.image))
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
    
    def apply_filter(self, filter_func: Callable) -> 'ImageProcessor':
        self.image = filter_func(self.image)
        return self
    
    def resize(self, width: int, height: int) -> 'ImageProcessor':
        self.image = cv2.resize(self.image, (width, height))
        return self
    
    def grayscale(self) -> 'ImageProcessor':
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        return self
    
    def blur(self, kernel_size: int = 5) -> 'ImageProcessor':
        self.image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
        return self
    
    def edge_detect(self) -> 'ImageProcessor':
        gray = self.grayscale().image if len(self.image.shape) == 3 else self.image
        self.image = cv2.Canny(gray, 100, 200)
        return self
    
    def histogram_equalization(self) -> 'ImageProcessor':
        if len(self.image.shape) == 3:
            # Convert to YUV and equalize Y channel
            yuv = cv2.cvtColor(self.image, cv2.COLOR_RGB2YUV)
            yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
            self.image = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)
        else:
            self.image = cv2.equalizeHist(self.image)
        return self
    
    def adaptive_threshold(self, block_size: int = 11, c: int = 2) -> 'ImageProcessor':
        gray = self.grayscale().image if len(self.image.shape) == 3 else self.image
        self.image = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, block_size, c
        )
        return self
    
    def morphological_operations(self, operation: str = 'open', kernel_size: int = 3) -> 'ImageProcessor':
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        if operation == 'open':
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)
        elif operation == 'close':
            self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        elif operation == 'dilate':
            self.image = cv2.dilate(self.image, kernel, iterations=1)
        elif operation == 'erode':
            self.image = cv2.erode(self.image, kernel, iterations=1)
        return self
    
    def find_contours(self) -> List[np.ndarray]:
        if len(self.image.shape) == 3:
            gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        else:
            gray = self.image
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    
    def draw_contours(self, color: tuple = (255, 0, 0), thickness: int = 2) -> 'ImageProcessor':
        contours = self.find_contours()
        if len(self.image.shape) == 2:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2RGB)
        self.image = cv2.drawContours(self.image, contours, -1, color, thickness)
        return self
    
    def save(self, path: str):
        cv2.imwrite(path, cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR))
    
    def show(self):
        Image.fromarray(self.image).show()

# Example usage
processor = ImageProcessor("input.jpg")
processor.resize(800, 600)\
         .grayscale()\
         .histogram_equalization()\
         .adaptive_threshold()\
         .morphological_operations('open')\
         .draw_contours()\
         .save("output.jpg")
