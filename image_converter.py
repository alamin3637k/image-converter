import cv2

img_path = input("Enter image path: ")
file_name = input("Enter file name(with converting extension example: my_file_name.png or my_file_name.jpg): ")
try:
    img = cv2.imread(img_path, -1)
except Exception as error:
    print(error)
    print("image path is wrong")
    input()

print("converting...")
cv2.imwrite(filename=file_name, img=img)
print("converted")



