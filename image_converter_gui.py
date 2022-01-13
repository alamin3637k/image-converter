import cv2
from tkinter import Button, Tk, filedialog, Label, Entry

class app:
    def __init__(self):
        self.window = Tk()
        self.window.title("img converter")   
        self.window.geometry("500x400")
    def open_img_command(self):
        file_path = filedialog.askopenfilename(title="open image file")
        img_path_txt = Label(self.window, text=file_path)
        img_path_txt.pack()
        self.img = cv2.imread(file_path, -1)
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

    def ui(self):
        open_img = Button(self.window, text="open image", command=self.open_img_command)
        open_img.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = app()
    app.ui()
    app.run()
