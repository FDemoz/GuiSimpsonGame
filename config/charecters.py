from utils.character import Character

characters = {
    "Homer": Character(name='Homer',
                  power=8,
                  health=9,
                  assault=4,
                  defence=6,
                  special_move="MOE's",
                  images={
                      "character_selection": {
                          "path": "charector_selection.png",
                          "width": 100,
                          "hight": 170,
                          "box_grid": [0, 0]
                      },
                      "action": {
                          "path": "action.png",
                          "width": 120,
                          "hight": 160,
                      },
                      "dead": {
                          "path": "dead.jpg",
                          "width": 200,
                          "hight": 100,
                      }
                  }),
    "Marge": Character(name='Marge',
                  power=5,
                  health=7,
                  assault=4,
                  defence=6,
                  special_move="Hair Attack",
                  images={
                      "character_selection": {
                          "path": "charector_selection.png",
                          "width": 100,
                          "hight": 150,
                          "box_grid": [1, 0]
                      },
                      "action": {
                          "path": "action.png",
                          "width": 100,
                          "hight": 200,
                      },
                      "dead": {
                          "path": "dead.jpg",
                          "width": 200,
                          "hight": 100,
                      }
                  }),
    "Bart": Character(name='Bart',
                  power=3,
                  health=9,
                  assault=4,
                  defence=9,
                  special_move="Fly Kick",
                  images={
                      "character_selection": {
                          "path": "charector_selection.png",
                          "width": 100,
                          "hight": 150,
                          "box_grid": [0, 1]
                      },
                      "action": {
                          "path": "action.png",
                          "width": 100,
                          "hight": 150,
                      },
                      "dead": {
                          "path": "dead.jpg",
                          "width": 200,
                          "hight": 100,
                      }
                  }),
    "Lisa": Character(name='Lisa',
                  power=2,
                  health=9,
                  assault=3,
                  defence=6,
                  special_move="Books",
                  images={
                      "character_selection": {
                          "path": "charector_selection.png",
                          "width": 100,
                          "hight": 150,
                          "box_grid": [1, 1]
                      },
                      "action": {
                          "path": "action.png",
                          "width": 100,
                          "hight": 150,
                      },
                      "dead": {
                          "path": "dead.jpg",
                          "width": 200,
                          "hight": 100,
                      }
                  }),
}
