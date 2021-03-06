#
# This file is where you will control your player.
# Make changes and add functions as you need.
#

import pygame
import math
import config
from client.base_control import *
from character import *


class Control(BaseControl):
    """
    This class is where you specify how your player
    behaves in the game.  You can use key presses,
    mouse clicks, and mouse motion to receive input
    from the user.

    You can also add calculations in this code to 
    control the behavior of your player based on the
    state of the game.

    The 4 methods below have specific purposes:
    __init__ is used to create an variables (data members) that
        you need to remember here and in the display class.
    pregame_control is used to get user input before you join 
        a game.  This is most important in deciding what kind 
        of game the user would like to join.
    game_input_control is used to get user input during a running
        game.  This is most important in allowing the user to
        tell your code what they would like to have happen.
    game_control is used to have your program make calculations
        and choose what actions to take, without user input.

    There are several parameters and data members that are
    of interest in some or all of these methods:
    engine is the game engine that contains all of the information
        about the current game.  It also has all of the control
        methods that allows you to send commands to the server
        to control your player.
    keys is the set of all keys that are currently pressed.  This
        allows your program to know what keys are held down, if you
        want to implement behavior that repeats when a key is held
        down.
    newkeys is the set of all keys that were newly pressed since.
        the last time these methods were called.  This allows your
        program to know what keys were just pressed, if you
        want to implement behavior that occurs once, when the key
        is first pressed.
    buttons is the set of all mouse buttons that are currently held
        down.  Much like keys is for the keyboard.
    newbuttons is the set of mouse buttons that were newly pressed
        since the last time these methods were called.  Much like
        newkeys is for the keyboard.
    mouse_position is the current location of the mouse.
    self.width is the width of the display screen in pixels.
    self.height is the height of the display screen in pixels.

    A note on keys and newkeys:
    pygame.K_UP is the symbol for the up arrow on your keyboard.
    If you want to know more keyboard symbols look at this
    site http://www.pygame.org/docs/ref/key.html.

    A note on buttons and newbuttons:
    The values in these sets are numbers 1, 2, 3, etc.,
    depending on the number of buttons you have on your
    mouse.  Usually, 1 is left, 2 is middle (holding down
    the scroll wheel), and 3 is right.

    A note on engine:
    You should look at engine_client/game_engine.py to learn
    more about the information and commands that are available
    from this object.
    """

    def __init__(self, width, height):
        """Create any control variables in this method"""
        
        BaseControl.__init__(self, width, height)
        # used to control display of individual item information
        self.show_info = False


        self.mario_sounds = ['mariothrow.wav', 'mariovictory.wav', 'mariodeath.wav']
        self.luigi_sounds = ['luigithrow.wav', 'luigivictory.wav', 'luigideath.wav']
        self.link_sounds = ['linkthrust.wav', 'linkvictory.wav', 'linkdeath.wav']
        self.kirby_sounds = ['Kirbythrow.wav', 'kirbyvictory.wav', 'kirbydeath.wav']

        self.link = Character('link', self.link_sounds, SPRITESHEETS[0], CHAR_STATE['link'])
        self.char = self.link
        

        self.yourcharacters = []
        Rect1 = pygame.Rect(50, 100, 100, 125)

        for i in range(config.CHARACTER_NUM):
            # color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            Rect1.left += 120
            self.yourcharacters.append([Rect1.copy(), False, False])
        
        self.enemycharacters =[]
        Rect2 = pygame.Rect(50, 255, 100, 125)
        for i in range(config.CHARACTER_NUM):
            Rect2.left += 120
            self.enemycharacters.append([Rect2.copy(), False, False])
            

        self.arenacharacters = []
        Rect3 = pygame.Rect(180, 420, 100, 125)
        for i in range(3):
            Rect3.left += 120
            self.arenacharacters.append([Rect3.copy(),False, False])

        self.charSelected = False
        self.foeSelected = False
        self.arenaSelected = False

        # self.chars= ['kirby','link','mario','luigi']
        # self.name = self.chars[(random.randint(0,3)]
        # 

        self.tourneyR = pygame.Rect(5,579,200,97)
        self.singleR = pygame.Rect(225,579,200,97)
        self.dualR = pygame.Rect(445,579,200,97)
        self.demoR = pygame.Rect(665,579,200,97)
        self. buttons  =[(pygame.Rect(5,579,200,97),'CONTROL_STATE_WANT_TOURNAMENT'),(pygame.Rect(225,579,200,97),'CONTROL_STATE_WANT_SINGLE'),(pygame.Rect(445,579,200,97),'CONTROL_STATE_WANT_TOURNAMENT'),(pygame.Rect(665,579,200,97),'CONTROL_STATE_WANT_VIEW')]

        return

    def pregame_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        """
        This method is called every frame while waiting for the
        user to decide they want to join a game, and what kind
        of game they want to join.

        Somewhere in this method you should make one of these calls:
        self.set_state(CONTROL_STATE_WANT_DUAL)
        self.set_state(CONTROL_STATE_WANT_SINGLE),
        self.set_state(CONTROL_STATE_WANT_TOURNAMENT),
        self.set_state(CONTROL_STATE_WANT_VIEW),
        based on the user input.  Defaults here are for the
        user to press 'd' for dual, 's' for single player game, 't' for tournament.
        """
        # print self.yourcharacters[0][1]
        for i in self.yourcharacters:
            # print mouse_position, i[0]
            if mouse_position[0] in range(i[0][0],i[0][0] + i[0][2]) and mouse_position[1] in range(i[0][1],i[0][1] + i[0][3]):
                if 1 in newbuttons:
                    #Some character was pressed
                    for reset in self.yourcharacters:
                        reset[1]=0
                    i[1] = [True]
                    self.charSelected = True
                i[2] = [True]
            else:
                i[2] = False


        for i in self.enemycharacters:
            if mouse_position[0] in range(i[0][0],i[0][0] + i[0][2]) and mouse_position[1] in range(i[0][1],i[0][1] + i[0][3]):
                if 1 in newbuttons:
                    for reset in self.enemycharacters:
                        reset[1] = 0
                    i[1] = [True]
                    self.foeSelected = True
                i[2] = [True]

            else:
                i[2] = False
             

        for i in self.arenacharacters:
            if mouse_position[0] in range(i[0][0],i[0][0] + i[0][2]) and mouse_position[1] in range(i[0][1],i[0][1] + i[0][3]):
                if 1 in newbuttons:
                    for reset in self.arenacharacters:
                        reset[1] = 0
                    i[1] = [True]
                    self.arenaSelected = True
                i[2] = [True]
            else:
                i[2] = False

            # print i[1], i[2]
        
            
            # if 1 in newbuttons:


        if 1 in newbuttons:
            for b in self.buttons:
                if b[0].collidepoint(mouse_position):
                    eval("self.set_state("+b[1]+')')

#             if mouse_position[0] in range(340, 556):
#                 if mouse_position[1] in range(39, 147):

#                     # self.set_state(CONTROL_STATE_WANT_DUAL)

#                     self.set_state(CONTROL_STATE_WANT_TOURNAMENT)
# ##        elif pygame.K_q in newkeys:

#                 elif mouse_position == (187, 295):
#                     self.set_state(CONTROL_STATE_WANT_SINGLE)
#                 elif mouse_position == (335, 443):

#                     # self.set_state(CONTROL_STATE_WANT_TOURNAMENT)

#                     self.set_state(CONTROL_STATE_WANT_DUAL)
# ##        elif pygame.K_v in newkeys:

#                 elif mouse_position == (483, 591):
#                     self.set_state(CONTROL_STATE_WANT_VIEW)
        # elif buttonUp:
            # characters[0][1] = COLORS[0]
##        if pygame.K_d in newkeys:
        # if pygame.K_1 in newbuttons:
            # if mouse_position == ( , ):
                # self.set_state(CONTROL_STATE_WANT_DUAL)
##        elif pygame.K_q in newkeys:
            # elif mouse_position == ( , ):
                # self.set_state(CONTROL_STATE_WANT_SINGLE)
##        elif pygame.K_t in newkeys:
            # elif mouse_position == ( , ):
                # self.set_state(CONTROL_STATE_WANT_TOURNAMENT)
##        elif pygame.K_v in newkeys:
            # elif mouse_position == ( , ):
                # self.set_state(CONTROL_STATE_WANT_VIEW)
                
        return
        
    def game_input_control(self, engine, keys, newkeys, buttons, newbuttons, mouse_position):
        """
        This method is called every frame while the game is
        running.  You should put controls in here
        to make changes to the game engine based on the
        user input.
        """
        # print CHAR_STATE['link']
        (mouse_x, mouse_y) = mouse_position
        degrees = 270


        degrees2 = 0
        oid = engine.get_player_oid()
        if oid > 0:
            player = engine.get_object(oid)
            if player != None:            
                (x1,y1) = player.get_center()

                newX = mouse_x - x1
                newY = mouse_y - y1
                
                radians = math.atan2(newY, newX)
                radians %= 2*math.pi
                degrees2 = math.degrees(radians)

        
        engine.set_missile_direction(degrees2)
        

        if pygame.K_w in keys: #forward
            rotation = (degrees + 0) % 360
            engine.set_player_direction(rotation)
            # engine.set_missile_direction(degrees2)
            engine.set_player_speed_slow()
        elif pygame.K_d in keys: #right
            rotation = (degrees + 90) % 360
            engine.set_player_direction(rotation)
            # engine.set_missile_direction(degrees2)
            engine.set_player_speed_slow()
        elif pygame.K_s in keys: #reverse
            rotation = (degrees + 180) % 360
            engine.set_player_direction(rotation)
            # engine.set_missile_direction(degrees2)
            engine.set_player_speed_slow()
        elif pygame.K_a in keys: #left
            rotation = (degrees + 270) % 360
            engine.set_player_direction(rotation)
            # engine.set_missile_direction(degree2)
            engine.set_player_speed_slow()
        else:
            engine.set_player_speed_stop()
        
        # if pygame.K_UP in newkeys:
        #     engine.set_player_direction(270)
        #     engine.set_missile_direction(270)
        # elif pygame.K_DOWN in newkeys:
        #     engine.set_player_direction(90)
        #     engine.set_missile_direction(90)
        # elif pygame.K_LEFT in newkeys:
        #     engine.set_player_direction(180)
        #     engine.set_missile_direction(180)
        # elif pygame.K_RIGHT in newkeys:
        #     engine.set_player_direction(0)
        #     engine.set_missile_direction(0)

        # if pygame.K_1 in newkeys:
        #     engine.set_player_speed_stop()
        # elif pygame.K_2 in newkeys:
        #     engine.set_player_speed_slow()
            
        if pygame.K_j in newkeys:
            engine.set_missile_range_none()
        elif pygame.K_k in newkeys:
            engine.set_missile_range_short()

        if pygame.K_l in newkeys:
            engine.set_missile_power_none()
        elif pygame.K_p in newkeys:
            engine.set_missile_power_low()
                
        if pygame.K_SPACE in newkeys:
            engine.fire_missile()

        if pygame.K_i in newkeys:
            self.show_info = not self.show_info

        return
        
    def game_control(self, engine):
        """
        This method is called every frame while the game is
        running.  You should put here any calls to the
        game engine you want to do based on your program's
        calculations.  This method is called immediately
        following the game_input_control() method.
        """

        return

    

    




