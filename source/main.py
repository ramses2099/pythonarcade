import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

PLAYER_IMG = "../assets/Player/player_01.png"
COIN_IMG = "../assets/Environment/environment_11.png"
COIN_COUNT = 20


class Coin(arcade.Sprite):
    def __init__(self, filename):
        super().__init__(filename)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Game(arcade.Window):
    def __init__(self, title):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(PLAYER_IMG)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # create coins
        for i in range(COIN_COUNT):
            coin = Coin(COIN_IMG)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()

        # score draw
        ouput = f"Score: {self.score}"
        arcade.draw_text(ouput, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time: float):
        self.coin_list.update()
        # Generate a list of all sprites that collided wiht the player
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    window = Game("Test Arcade Framework")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
