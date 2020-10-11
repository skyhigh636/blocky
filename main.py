def on_on_overlap(sprite, otherSprite):
    dart.destroy()
    bogey.destroy()
    dart.start_effect(effects.fire)
    bogey.start_effect(effects.fire)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 5 . . . . . . . . . . . . 
                    . . . . 5 . . . . . 5 . . . . . 
                    . . . . . 2 2 2 2 2 2 5 . . . . 
                    . . . . 5 . . . . . 5 . . . . . 
                    . . . 5 . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
dart: Sprite = None
spacePlane: Sprite = None
spacePlane = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 8 . . . . . . . . . . . . 
            . . 8 4 8 . . . . . . . . . . . 
            . . 8 4 4 8 . . . . . . 2 . . . 
            . . . 8 4 4 8 8 8 8 8 8 8 2 . . 
            . . . . 8 2 1 2 2 1 2 2 1 8 2 . 
            . . . . . 8 8 8 8 8 8 8 8 2 . . 
            . . . . . . . . . . . . 2 . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(spacePlane, 200, 200)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 2 2 2 . . . 
                    . . . . . 2 4 4 4 4 4 4 4 2 . . 
                    . . . . 2 4 f 5 5 5 5 5 f 4 2 . 
                    . . . . 2 4 5 8 8 8 8 8 5 4 2 . 
                    . . . . 2 4 5 8 a a a 8 5 4 2 . 
                    . . . . 2 4 5 8 a f a 8 5 4 2 . 
                    . . . . 2 4 5 8 a a a 8 5 4 2 . 
                    . . . . 2 4 5 8 8 8 8 8 5 4 2 . 
                    . . . . 2 4 f 5 5 5 5 5 f 4 2 . 
                    . . . . . 2 4 4 4 4 4 4 4 2 . . 
                    . . . . . . 2 2 2 2 2 2 2 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(180, randint(0, 120))
game.on_update_interval(500, on_update_interval)
