
import tkinter as tk

class Sprite():
    def __init__(self, pathForSprite):
        self.spritesheet = tk.PhotoImage(file=pathForSprite)
        self.num_sprintes = 3
        self.partWidth = 25 # int(self.spritesheet.width() / self.num_sprintes)
        self.images = [self.subimage(self.partWidth*i,
                       0,
                       self.partWidth*(i+1),
                       self.spritesheet.height()) for i in range(self.num_sprintes)]
        # self.updateimage(0)

    def subimage(self, l, t, r, b):
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    # def updateimage(self, sprite):
        # self.canvas.delete(self.last_img)
        # self.last_img = self.canvas.create_image(16, 24, image=self.images[sprite])
        # self.after(100, self.updateimage, (sprite+1) % self.num_sprintes)
