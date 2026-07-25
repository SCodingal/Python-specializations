import cv2
import numpy as np

def apply_color_filters(image,filter_type):
    """Apply the specified color filter to the image"""

    filtered_image = image.copy()
    if filter_type =="purple_tint":

        filtered_image[:,:,1] = 0

    elif filter_type == 'yellow_tint':
        filtered_image[:,:,0] = 0
    
    elif filter_type == 'magenta_tint':
        filtered_image[:,:,0] = 0
        filtered_image[:,:,2] = 0
    
    elif filter_type == 'increase_tint':
       filtered_image[:,:,1] = cv2.add(filtered_image[:,:,1],50)

    elif filter_type == 'decreasee_tint':
       filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,2],50)

    return filtered_image

image_path ='example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found, try to put one")

else:
    filter_type = "Original"

    print("Press the following keys to apply filters")
    print("p - Purple Tint")
    print("y - Yellow Tint")
    print("m - Magenta Tint")
    print("i - Increase Purple Intensity")
    print("d - Decrease Yellow Intensity")
    print("Exit") 

    while True:

        filtered_image = apply_color_filters(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('p'):
            filter_type = "purple_tint"
        elif key == ord('y'):
            filter_type = "yellow_tint"
        elif key == ord('m'):
            filter_type = "magenta_tint"
        elif key == ord('i'):
            filter_type = "increase_purple"
        elif key == ord('d'):
            filter_type = "decrease_yellow"
        elif key == ord('q'):
            print("Exiting...")
            break

        else:
            print("Invalid key! Please use 'p', 'y','m','i','d', or 'q' ")

cv2.destroyAllWindows()