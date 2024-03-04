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



class GridScreen(Screen):
    def __init__(self, root, functions=None):
        super().__init__(root)
        # O atributo current_selection agora é uma tupla com a linha e a coluna da seleção atual
        self.current_selection = (0, 0)
        # O atributo functions é um dicionário com os nomes e as funções das funções laterais
        self.functions = functions or {}
        # O atributo rows e cols define o número de linhas e colunas da matriz de itens
        self.rows = 5
        self.cols = 9
        # O atributo labels é uma matriz de labels que mostra os itens na interface
        self.labels = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        # O atributo function_frame é um frame que mostra os botões das funções na lateral
        self.function_frame = None
        # O atributo function_buttons é uma lista de botões que mostra os nomes e as funções das funções laterais
        self.function_buttons = []

        # Configurando os eventos do teclado para navegar pelos itens
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.select_item)

    def render_items(self):
        # Removendo os widgets antigos antes de criar os novos
        for i in range(self.rows):
            for j in range(self.cols):
                if self.labels[i][j]:
                    self.labels[i][j].grid_remove()

        if self.function_frame:
            self.function_frame.grid_remove()

        # Criando os labels com os itens e as cores de acordo com a seleção
        for i, item in enumerate(self.items):
            row = i // self.cols
            col = i % self.cols
            color = "green" if (row, col) == self.current_selection else "blue"
            label = tk.Label(self.root, text=item, fg=color)
            label.grid(row=row, column=col, padx=5, pady=5)
            self.labels[row][col] = label

        # Criando o frame com os botões das funções laterais
        self.function_frame = tk.Frame(self.root)
        self.function_frame.grid(row=0, column=self.cols, rowspan=self.rows, sticky="ns")

        # Criando os botões com os nomes e as funções das funções laterais
        for name, func in self.functions.items():
            button = tk.Button(self.function_frame, text=name, command=func)
            button.pack(padx=10, pady=10)
            self.function_buttons.append(button)

    def move_up(self, event):
        row, col = self.current_selection
        if row > 0:
            row -= 1
            self.current_selection = (row, col)
            self.render_items()

    def move_down(self, event):
        row, col = self.current_selection
        if row < self.rows - 1:
            row += 1
            self.current_selection = (row, col)
            self.render_items()

    def move_left(self, event):
        row, col = self.current_selection
        if col > 0:
            col -= 1
            self.current_selection = (row, col)
            self.render_items()

    def move_right(self, event):
        row, col = self.current_selection
        if col < min(len(self.items) - 1 - row * self.cols, self.cols - 1):
            col += 1
            self.current_selection = (row, col)
            self.render_items()

    def select_item(self, event):
        item = None
        try:
            item = self.items[self.current_selection[0] * self.cols + self.current_selection[1]]
        except IndexError:
            pass

        if item and item not in self.selected_items:
            print(f"Selected {item}")
            # Você pode mudar a cor do item selecionado aqui se quiser
            # ou adicionar algum outro feedback visual
            #self.render_items()


def create_screen(root, screen_type, items, format_func=None, navigation_style=None, functions=None):
    # Essa função cria uma instância da subclasse correspondente ao tipo de tela
    # e retorna o objeto. Você pode passar uma função opcional para formatar os itens,
    # um estilo opcional de navegação e um dicionário opcional com as funções laterais.
    screen = None
    if screen_type == "list":
        screen = ListScreen(root, navigation_style)
    elif screen_type == "grid":
        screen = GridScreen(root, functions)

    if screen:
        screen.items = items
        if format_func:
            screen.items = [format_func(item) for item in items]
        screen.render_items()
        return screen
    else:
        print(f"Invalid screen type: {screen_type}")
        return
    


if __name__ == "__main__":
    root = tk.Tk()

# Exemplo de lista de itens para a grade
grid_items = [f"Item {i}" for i in range(1, 31)]

# Exemplo de função para formatar os itens na grade (opcional)
def format_item(item):
    return f"ID: {item}"

# Exemplo de dicionário com as funções laterais (opcional)
function_dict = {
    "Function 1": lambda: print("Function 1 acionada"),
    "Function 2": lambda: print("Function 2 acionada"),
    # Adicione outras funções aqui, se necessário
}

# Criação da tela com gridNavigation
screen = create_screen(root, "grid", grid_items, format_func=format_item, navigation_style="keyboardWithArrows", functions=function_dict)

root.mainloop()
