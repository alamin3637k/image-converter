import webbrowser
import cv2

print("what you want?")
print("1/ Color to Black and White image")
print("2/ Black and White to Color")
ans = int(input("Ans(1 or 2): "))

if ans == 1:
    img_path = input("Enter image path: ")
    file_name = input("Enter new file name: ")
    try:
        print("converting...")
        img = cv2.imread(img_path, 0)
    except Exception as error:
        print(error)
        input()
    try:
        print("saving new image...")
        cv2.imwrite(filename=file_name, img=img)
        print("converted")
        input()
    except Exception as error:
        print(error)
        input()

elif ans == 2:
    webbrowser.open_new_tab("https://imagecolorizer.com/colorize.html")
    print("use this website to colorize your image")
    input()

else:
    print('error')
    input()
