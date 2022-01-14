import webbrowser
import cv2
from tkinter import Tk, filedialog, Button, Label,Entry

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("image color converter")
        self.window.geometry("600x500")
    
    def open_image(self):
        file_path = filedialog.askopenfilename(title="open image file")
        img_path_txt = Label(self.window, text=file_path)
        img_path_txt.pack()
        self.img = cv2.imread(file_path, 0)
        label2 = Label(self.window, text="write file name with codec example: my_image_name.jpg, my_image_name.png")
        label2.pack()
        self.entry1 = Entry(self.window, width = 20)
        self.entry1.pack()
        button1 = Button(self.window, text="convert", command=self.convert)
        button1.pack()
    
    def convert(self):
        file_name = self.entry1.get()
        try:
            cv2.imwrite(file_name, self.img)
            Label(self.window, text='converted').pack()
        except:
            print("retry")
        
    def colorize(self):
        webbrowser.open_new_tab("https://imagecolorizer.com/colorize.html")
        label3 = Label(self.window, text="use this website to colorize your image")
        label3.pack()

    def ui(self):
        button = Button(self.window, text="open image", command=self.open_image)
        button.pack()
        button1 = Button(self.window, text="colorize a image", command=self.colorize)
        button1.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.ui()
    app.run()
