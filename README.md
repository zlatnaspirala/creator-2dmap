# creator-2dmap #
## 2d Map Generator for platformer (visual-ts game engine) ##

 - This is tool for creating map objects for platformer game template
   in <b>visual-typescript game engine</b> project.

   Download engine source from :
     https://github.com/zlatnaspirala/visual-ts-game-engine

   For visual-ts-game-engine follow :
   https://github.com/zlatnaspirala/visual-ts-game-engine/blob/master/readme.md
   for help. In best way you need to install npm modules and run :
   ```
     npm run dev
     npm run rtc
   ```
   
   Tako a look youtube videos who it works: 
   
   [![YouTube link](https://i9.ytimg.com/vi/f2Ha_0lGj9o/mq3.jpg?sqp=CLjeqfcF&rs=AOn4CLClg6u40dP8qgdwsAWyDBJLABoCLw)](https://www.youtube.com/watch?v=Sm0LLR-iF8s&t=504s)
   [![YouTube link](https://i9.ytimg.com/vi/Sm0LLR-iF8s/mq3.jpg?sqp=CLjeqfcF&rs=AOn4CLD6hxEi0quFM8xMhfNSzkxFsGiMxQ)](https://www.youtube.com/watch?v=f2Ha_0lGj9o&t=4s)



![visualTSTools](https://github.com/zlatnaspirala/creator-2dmap/blob/master/creator-2d-map.image.png)

### Help : ###

 Much more easyest is creator-2dmap python script.
 After installation of all needed modules vie pip3 for python3, you need to run:

```bash
  # Windows
  python.exe tool.py
  # Macos - linux
  python3 ./tool.py
```

``` Possible bug on oldies linux os mint. Bug related with tkinter lib. ```

 #### You need to change `self.absolutePacksPath` from defaults.py config file. ####
 Put example platformer pack folder path :
  `src\examples\platformer\scripts\packs`
  but path must be absolute, my personal path is (For windows users : use double \ for escape ) :

  This is example for windows users:

  `E:\\web_server\\xampp\htdocs\\PRIVATE_SERVER\\visual-ts\\project\\visual-ts\\src\\examples\\platformer\\scripts\\packs\\"`

Realtive paths no need to change - Only if you use your own project modification.

```python
    self.relativeMapPath = "\\src\\examples\\platformer\\scripts\\packs\\"
    self.relativeTexturesPath = "\\src\\examples\\platformer\\imgs\\"
    self.relativeTexGroundsPath = "grounds\\"
    self.relativeTexCollectItemsPath = "collect-items\\"
```

Project based on Python3 and Tk library.


Last version:

<pre>

  <b>Version: 0.4.4</b>

  Games template based on version: 0.4.4
  https://apps.facebook.com/nidzica/ single player platformer solution.

#################################################################################
#  creator2dmap is python3 application for creating visuat-ts game engine 2d maps
#  LICENCE: GNU LESSER GENERAL PUBLIC LICENSE Version 3
#  https://github.com/zlatnaspirala/creator-2dmap
#  Code style ~camel
#  Version: 0.4.4
#  - Types of game object: [ground, collectItem, enemies, labels]
#  - Show/Hide grids
#  - Sticklers enable disable
#  - defaults.py - general config
#  - Save/Load direct (template map) it is : map2d.creator file in the root of
#     project. If you have already manualy added and than load default map it will
#     be append together in current map.
#    Save/Load dialog for custom maps. Default folder `saved-maps/`
#   Clear map - Force clear without warning
#   Reset input - for reset left box input values to the minimum.
#  - Relocate last added game object
#  - Remove last added element
#   Scroll vertical & horizontal canvas, help to create large maps.
#   Adding basic Text component (args: text , color)
#   Change canvas background
#   nextLevel item collection model. Item will teleport player to the next level/map
#   Export As - Feature Export and give a map name (without `.ts`)
#
#   Fix : load map
#################################################################################

</pre>

### Licence : ###
<b>
  GNU LESSER GENERAL PUBLIC LICENSE Version 3
  maximumroulette.com 2020
</b>

### About licence: ###

```
  If you use this code you need to provide your modification like open source
   with same licence GPL v3.
   In short way explanation: You can use it in commercial or noncommercial projects
   -if you provide origin licence with software, refer your modification source code with public link.
    If you make some improvements then let other people to use source just like you did.
```

### Export structure : ###

```javascript
let generatedMap = [
  {"x": 1300.0,
   "y": 375.0,
   "w": 50.0,
   "h": 50.0,
   "tex": require('../../imgs/grounds/boxAlt.png'),
   "tiles": {"tilesX": 1.0,
   "tilesY": 1.0}
  },
  {"x": 1300.0,
   "y": 275.0,
   "w": 50.0,
   "h": 50.0,
   "tex": require('../../imgs/collect-items/hudKey_green_empty.png'),
   "tiles": {"tilesX": 1.0,
   "tilesY": 1.0},
   "colectionLabel": "Level2",
   "points": 10
  },
  {"x": 600.0,
   "y": 130.0,
   "w": 50.0,
   "h": 50.0,
   "tex": require('../../imgs/collect-items/bitcoin-out.png'),
   "tiles": {"tilesX": 1.0,
   "tilesY": 1.0},
   "colectionLabel": "collectItemPoint",
   "points": 10
  }
]
```

I use best inside logic.Use undefined to make determination of type object.
Textures `tex` param and `tiles` indicate TextureComponent
If I catch colectionLabel then i check value for this key and if i find
"Level" sub string then teleport is my current model.
enemies refer to the enemy object.

