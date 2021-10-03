import numpy as np

class RatioRoi:
    def __init__(self, original, resized):
        original_shape = original.shape[:2]
        resized_shape = resized.shape[:2]
        self.scale = np.flipud(np.divide(resized_shape, original_shape)) # numerator remains
    
    def get_position(self, position):# use this on to get new top left corner and bottom right corner coordinates
        new_top_left_corner = np.multiply(position, self.scale)
        pos = new_top_left_corner.astype(int)
        return list(pos)
