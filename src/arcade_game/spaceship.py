"""
Un module pour le vaisseau
                                   _     _
                                  | |   (_)
     ___ _ __   __ _  ___ ___  ___| |__  _ _ __
    / __| '_ \ / _` |/ __/ _ \/ __| '_ \| | '_ \
    \__ \ |_) | (_| | (_|  __/\__ \ | | | | |_) |
    |___/ .__/ \__,_|\___\___||___/_| |_|_| .__/
        | |                               | |
        |_|                               |_|
                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                                  `------'`
"""

import pyxel

class Spaceship :
    """
    Une classe pour notre vaisseau
    """
    def __init__(self, jeu, x, y):
        """Initialisation du vaisseau

        :param x: L'abscisse du coin supérieur gauche
        :type x: int
        :param y: L'ordonnée du coin supérieur gauche
        :type y: int
        """
        self.jeu = jeu
        # position initiale du vaisseau
        self.x = x
        self.y = y
        # largeur (width) et hauteur du vaisseau (height)
        self.w = 8
        self.h = 8

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour du vaisseau (30FPS)
        """
        print("titi")
        self._move()

    def _move(self):
        
        """déplacement avec les touches de directions"""
        print("toto")
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < self.jeu.w-self.w:
            self.x += 2
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0 :
             self.y -= 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
             self.x -= 2
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < self.jeu.h-self.h:
             self.y += 2 
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin du vaisseau
        """
        # vaisseau (carre 8x8)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)
