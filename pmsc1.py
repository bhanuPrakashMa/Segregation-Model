import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class SchellingModel:
    def __init__(self, size=100, empty_ratio=0.1, H=4, move_type='random', update_order='sequential'):
        self.size = size
        self.empty_ratio = empty_ratio
        self.H = H
        self.move_type = move_type
        self.update_order = update_order
        self.grid = np.full((size, size), None)
        self.empty_cells = []
        self.init_grid()

    def init_grid(self):
        num_cells = self.size * self.size
        num_empty = int(num_cells * self.empty_ratio)
        num_agents = num_cells - num_empty
        num_red = num_agents // 2
        num_blue = num_agents - num_red
        
        cells = ['R'] * num_red + ['B'] * num_blue + [None] * num_empty
        random.shuffle(cells)
        self.grid = np.array(cells).reshape(self.size, self.size)
        self.empty_cells = list(zip(*np.where(self.grid == None)))
    
    def get_neighbors(self, x, y):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        neighbors = []
        for dx, dy in offsets:
            nx, ny = (x + dx) % self.size, (y + dy) % self.size
            if self.grid[nx, ny] is not None:
                neighbors.append(self.grid[nx, ny])
        return neighbors

    def is_happy(self, x, y):
        neighbors = self.get_neighbors(x, y)
        if not neighbors:
            return False
        same_type_count = neighbors.count(self.grid[x, y])
        return same_type_count >= self.H

    def find_empty_cell(self, x, y):
        if not self.empty_cells:
            return None
        if self.move_type == 'horizontal':
            self.empty_cells.sort(key=lambda pos: abs(pos[1] - y))
        return random.choice(self.empty_cells)

    def update(self):
        agents = [(x, y) for x, y in zip(*np.where(self.grid != None)) if not self.is_happy(x, y)]
        if not agents:
            return False
        
        if self.update_order == 'random':
            random.shuffle(agents)
        
        moved = False
        for x, y in agents:
            new_pos = self.find_empty_cell(x, y)
            if new_pos:
                self.grid[new_pos], self.grid[x, y] = self.grid[x, y], None
                self.empty_cells.remove(new_pos)
                self.empty_cells.append((x, y)) 
                moved = True
        return moved

    def run(self):
        iterations = 0
        max_iterations = 5000  # Loop restriction as the limiting value
        while iterations < max_iterations:
            moved = self.update()
            iterations += 1
            if not moved:
                break
        return iterations

    def plot(self):
        color_map = {'R': 1, 'B': 2, None: 0}  
        grid_numeric = np.vectorize(color_map.get)(self.grid) 

        cmap = mcolors.ListedColormap(['white', 'red', 'blue']) 
        plt.imshow(grid_numeric, cmap=cmap, interpolation='nearest')
        plt.colorbar(ticks=[0, 1, 2], label="0: Empty, 1: Red, 2: Blue")
        filename = f"plot_H{self.H}_Move__{self.move_type}_Order__{self.update_order}_H_value_{H}.png"
        plt.savefig(filename, dpi=300)
        plt.pause(0.3)
        plt.close()

H = 4  # Fixed H value for the question 1
num_runs = 3  # Number of runs per combination
move_types = ['random', 'horizontal']
update_orders = ['sequential', 'random']

for move_type in move_types:
    for update_order in update_orders:
        for i in range(num_runs):
            model = SchellingModel(H=H, move_type=move_type, update_order=update_order)
            iterations = model.run()
            print(f"Run {i+1} for H={H}, Move: {move_type}, Order: {update_order} -> Converged in {iterations} iterations.")
            model.plot()
            
# # Input for the question 2
# H = 8  # Range of H value
# num_runs = 3  # Number of runs per combination
# move_types = 'random'
# update_orders =  'random'

# for h in range(H):
#      model = SchellingModel(H=h, move_type=move_types, update_order=update_orders)
#      iterations = model.run()
#      print(f"Run {h+1} for H={h}, Move: {move_types}, Order: {update_orders} -> Converged in {iterations} iterations.")
#      model.plot()
