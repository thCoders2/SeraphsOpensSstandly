import tkinter as tk
from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title("Interface HTTP")
        self.root.geometry("800x600")
        self.root.bind("<Return>", self.save_and_next)

        self.items = []
        self.selected_items = []

        self.current_selection = 0

    @abstractmethod
    def render_items(self):
        pass

    @abstractmethod
    def move_up(self, event):
        pass

    @abstractmethod
    def move_down(self, event):
        pass

    @abstractmethod
    def select_item(self, event):
        pass

    def save_and_next(self, event):
        # Implementar a lógica para salvar os itens selecionados e avançar para a próxima tela
        pass

class ListScreen(Screen):
    def __init__(self, root, navigation_style="upOrDown"):
        super().__init__(root)
        if navigation_style == "upOrDown":
            self.root.bind("<Up>", self.move_up)
            self.root.bind("<Down>", self.move_down)
            self.root.bind("<space>", self.select_item)
        elif navigation_style == "allArrows":
            self.root.bind("<Left>", self.move_up)
            self.root.bind("<Right>", self.move_down)
            self.root.bind("<space>", self.select_item)
        elif navigation_style == "fullKeyboard":
            self.root.bind("<Key>", self.select_item)
        elif navigation_style == "keyboardWithArrows":
            self.root.bind("<Left>", self.move_up)
            self.root.bind("<Right>", self.move_down)
            self.root.bind("<Key>", self.select_item)

    def render_items(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        for i, item in enumerate(self.items):
            color = "green" if i == self.current_selection else "blue"
            label = tk.Label(self.root, text=item, fg=color)
            label.pack(pady=5)

    def move_up(self, event):
        if self.current_selection > 0:
            self.current_selection -= 1
            self.render_items()

    def move_down(self, event):
        if self.current_selection < len(self.items) - 1:
            self.current_selection += 1
            self.render_items()

    def select_item(self, event):
        if event.keysym == "space" or event.char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            item = self.items[self.current_selection]
            if item not in self.selected_items:
                self.selected_items.append(item)
                print(f"Selected {item}")
                # Você pode mudar a cor do item selecionado aqui se quiser
                # ou adicionar algum outro feedback visual
                #self.render_items()

# Você pode criar outras subclasses de Screen para outros tipos de tela,
# como TableScreen, FormScreen, etc. Cada subclasse deve implementar os métodos
# render_items, move_up, move_down e select_item de acordo com o tipo de tela.

def create_screen(root, screen_type, items, format_func=None, navigation_style=None):
    # Essa função cria uma instância da subclasse correspondente ao tipo de tela
    # e retorna o objeto. Você pode passar uma função opcional para formatar os itens
    # e um estilo opcional de navegação.
    screen = None
    if screen_type == "list":
        screen = ListScreen(root, navigation_style)
    # elif screen_type == "table":
    #     screen = TableScreen(root, navigation_style)
    # elif screen_type == "form":
    #     screen = FormScreen(root, navigation_style)
    # etc.

    if screen:
        screen.items = items
        if format_func:
            screen.items = [format_func(item) for item in items]
        screen.render_items()
        return screen
    else:
        print(f"Invalid screen type: {screen_type}")
        return None

# Exemplo de uso da função create_screen para criar uma tela de lista
root = tk.Tk()
screen = create_screen(root, "list", ["Pedido 50253", "Pedido 48965", "Pedido 54685"], navigation_style="upOrDown")
root.mainloop()
