import tkinter as tk

class InterfaceManager:
    def __init__(self, root):
        self.root = root
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<space>", self.select_item)
        self.root.bind("<Return>", self.save_and_next)

        self.objects = []
        self.current_selection = 0

    def move_up(self, event):
        if self.current_selection > 0:
            self.current_selection -= 1
            self.render_objects()

    def move_down(self, event):
        if self.current_selection < len(self.objects) - 1:
            self.current_selection += 1
            self.render_objects()

    def select_item(self, event):
        selected_object = self.objects[self.current_selection]
        if hasattr(selected_object, "selected") and not selected_object.selected:
            selected_object.selected = True
        else:
            selected_object.selected = False
        self.render_objects()

    def save_and_next(self, event):
        # Aqui você pode realizar ações com os objetos selecionados
        selected_objects = [obj for obj in self.objects if hasattr(obj, "selected") and obj.selected]
        print("Objetos selecionados:", selected_objects)
        # Implemente as ações que desejar para os objetos selecionados

    def render_objects(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        for i, obj in enumerate(self.objects):
            color = "green" if i == self.current_selection else "blue"
            label = tk.Label(self.root, text=obj.name, fg=color)
            label.pack(pady=5)

def screenList(root, objects, navigation_style="upOrDown"):
    interface_manager = InterfaceManager(root)
    interface_manager.objects = objects

    if navigation_style == "allArrows":
        root.bind("<Left>", interface_manager.move_up)
        root.bind("<Right>", interface_manager.move_down)

    interface_manager.render_objects()

if __name__ == "__main__":
    root = tk.Tk()
    objects = [
        {"name": "Objeto 1"},
        {"name": "Objeto 2"},
        {"name": "Objeto 3"},
        {"name": "Objeto 4"},
        {"name": "Objeto 5"}
    ]
    screenList(root, objects, navigation_style="upOrDown")
    root.mainloop()
