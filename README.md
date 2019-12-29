# creator-2dmap #

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

Licence :
  GNU LESSER GENERAL PUBLIC LICENSE Version 3
  maximumroulette.com 2020

  About licence:

```
  If you use this code you need to provide your modification in some way.
```

### Export structure : ###

`
let generatedMap = [{"x": 400.0,
  "y": 400.0,
  "w": 800.0,
  "h": 80.0,
  "tex": "imgs/texx.png",
  "tiles": {"tilesX": 10.0,
  "tilesY": 1.0}}]
`

 ```
  UNDERCONSTRUCT
 ```
