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

![visualTSTools](https://github.com/zlatnaspirala/creator-2dmap/blob/master/creator-2d-map.image.png)

### Help : ###

 Much more easyest is creator-2dmap python script.
 After installation of all needed modules vie pip3 for python3 you need to run :

```bash
  # Windows
  python.exe toll.py
  # Macos - linux
  python3 ./toll.py
```

 #### You need to change `self.absolutePacksPath` from defaults.py config file. ####
 Put example platformer pack folder path :
  `src\examples\platformer\scripts\packs`
  but path must be absolute, my personal path is (For windows users : use double \ for escape ) :

  This is example for windows users:

  `E:\\web_server\\xampp\htdocs\\PRIVATE_SERVER\\visual-ts\\project\\visual-ts\\src\\examples\\platformer\\scripts\\packs\\"`

Realtive paths no need to change - Only if you use your own project modification .

```python
    self.relativeMapPath = "\\src\\examples\\platformer\\scripts\\packs\\"
    self.relativeTexturesPath = "\\src\\examples\\platformer\\imgs\\"
    self.relativeTexGroundsPath = "grounds\\"
    self.relativeTexCollectItemsPath = "collect-items\\"
```

Project based on Python3 and Tk library.


Last version :

<pre>

  <b>Version: 0.4</b>
  - Types of game object : [ground, collectItem]
  - Show/Hide grids
  - Sticklers enable disable
  - defaults.py - general config
  - Save Load direct (template map) it is : map2d.creator file in the root of
     project. If you have already manualy added and than load default map it will
     be append together in current map.
    Save/Load dialog for custom maps. Default folder `saved-maps/`
   Clear map - Force clear without warning
   Reset input - for reset left box input values to the minimum.
  - Relocate last added game object
  - Canvas scroolbar ver & hor added. defaults.py props:
   `self.canvasScreenCoeficientW & self.canvasScreenCoeficientH`
    for controling map size.


</pre>

Licence :
  GNU LESSER GENERAL PUBLIC LICENSE Version 3
  maximumroulette.com 2020

  About licence:

```
  If you use this code you need to provide your modification like open source
   with same licence GPL v3.
   You can use it in commercial or noncommercial projects
   if you provide origin licence.
```

### Export structure : ###

```javascript
let generatedMap = [
  {
    "x": 400.0,
    "y": 400.0,
    "w": 800.0,
    "h": 80.0,
    "tex": "imgs/texx.png",
    "tiles": {
      "tilesX": 10.0,
      "tilesY": 1.0
    }
  }
]
```

