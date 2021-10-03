import cv2  
from pathlib import Path 
from roi import RatioRoi

path = Path(__file__).parent

def circle(image, position, color=(255,0,0)):
    cv2.circle(image, position, 1, color, 5 )

def resize(image,window_height = 500):
    height, width = image.shape[:2]

    aspect_ratio = float(height/width)
    window_width = window_height/aspect_ratio
    image = cv2.resize(image, (int(window_height),int(window_width)))
    return image


img_path = path / 'image.webp'
img = cv2.imread(str(img_path))
resized = resize(image=img, window_height=200)

ratio = RatioRoi(img, resized)
pos = (40,130)
resized_pos = ratio.get_position(pos)
print(resized_pos)

circle(resized, resized_pos)
circle(img, pos)

cv2.imshow('original', img)
cv2.imshow('resized', resized)



cv2.waitKey(0)
# cv2.destroyAllwindows()