import tkinter as tk

class AsciCharacter:
    def __init__(self, arr_of_animation, hp, atk, name='main', is_bot=False):
        self.speed_ticks = 50
        self.steps_ticks = 64
        self.name = name
        self.hp = hp
        self.atk = atk
        self.direction = {'x': '50%', 'y': '-50%'}
        self.x = 0
        self.y = 0
        self.animation_arr = arr_of_animation
        self.index_animation = 0
        self.index_animation_limit = len(arr_of_animation)
        self.font_size = 32
        self.is_bot = is_bot

    def update_frame_animation(self):
        # Implement the logic to update the animation frame here
        self.index_animation = (self.index_animation + 1) % self.index_animation_limit
        return self.animation_arr[self.index_animation]

class AnimationsRoading:
    def __init__(self, root, loaded_maps):
        self.root = root
        self.main_character = AsciCharacter(arr_ascci, 15, 3, is_bot=False)
        self.data_base_enemies = [
            {'asci_arr': ['<o>', '<o>', '<->'], 'hp': 10, 'atk': 2, 'name': 'olhin', 'is_bot': True},
            # ... other enemy data
        ]
        self.enemies = self.generate_enemies(self.data_base_enemies)
        self.data_base_maps = loaded_maps

        self.canvas = tk.Canvas(self.root, width=200, height=100, bg='black')
        self.canvas.pack()

        self.character_text = self.canvas.create_text(100, 50, text='', font=('Courier', self.main_character.font_size), fill='white')
        self.root.after(0, self.update_animation)

    def generate_enemies(self, enemies_data):
        enemies_arr = []
        for enemy in enemies_data:
            enemies_arr.append(AsciCharacter(enemy['asci_arr'], enemy['hp'], enemy['atk'], enemy['name'], enemy['is_bot']))
        return enemies_arr

    def update_animation(self):
        animation_frame = self.main_character.update_frame_animation()
        self.canvas.itemconfig(self.character_text, text=animation_frame)
        self.root.after(1000, self.update_animation)  # Update every 1 second (1000 milliseconds)

if __name__ == "__main__":
    arr_ascci = ['(>o_o)>', '(>O_o)>', '(>-_-)>']

    root = tk.Tk()
    root.title("ASCI Animation")
    app = AnimationsRoading(root, loaded_maps=None)
    root.mainloop()
