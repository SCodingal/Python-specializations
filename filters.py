import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image."""""
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')

    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
        plt.show()

def intercarive_edge_deterction(image_path):
    """Interactive acticity for edge detection and filtering."""
    image= cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    
    grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", grey_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gussian Smoothing")
    print("5. Medium Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice(1-6):")

        if choice =="1":

            sobel_x = cv2.Sobel(grey_image, cv2.CV_64F, 1,0, ksize=3)
            sobel_y = cv2.Sobel(grey_image, cv2.CV_64F, 0,1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), 
sobel_y. astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            print("Adjust thresholds for Canny(defult: 100 and 200)")
            lower_thresh =int(input("Enter Lower threshold: "))
            upper_thresh =int(input("Enter Upper threshold: "))
            edges= cv2.Canny(grey_image, lower_thresh, upper_thresh)
            display_image("Canny Edges Detection", edges)

        elif choice == "3":
            laplacian = cv2.Laplacian(grey_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", 
np.abs(laplacian).astype(np.uint8))
            
        elif choice == "4":                                              

            print("Adjust Kernel size for Gussian blur (must be odd, defult:" 
            "5")

            kernel_size =int(input("Enter karnel size(odd number):"))
            blurred = cv2.GuassianBlur(image,(kernel_size, kernel_size),0)
            display_image("Guassian Smothed Image", blurred)

        elif choice == "5":

            print("Adjust Kernel size for Median filtering(must be odd, defult:" 
            "5")

            karnel_size =int(input("Enter karnel size(odd number):"))
            median_filtered = cv2.medianBlur(image,(kernel_size))
            display_image("Median Filtered Image", median_filtered)

        elif choice =="6":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please select a number between 1 and 6")

intercarive_edge_deterction('example.jpg')


