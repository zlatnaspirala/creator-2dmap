import Tkinter as tk

class Sprite(pathForSprite, tx, ty):
    def __init__(self):
        self.spritesheet = tk.PhotoImage(file=pathForSprite)
        self.num_sprintes = 7
        self.images = [self.subimage(32*i, 0, 32*(i+1), 48) for i in range(self.num_sprintes)]
        self.updateimage(0)

    def subimage(self, l, t, r, b):
        print(l,t,r,b)
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    # def updateimage(self, sprite):
        # self.canvas.delete(self.last_img)
        # self.last_img = self.canvas.create_image(16, 24, image=self.images[sprite])
        # self.after(100, self.updateimage, (sprite+1) % self.num_sprintes)
