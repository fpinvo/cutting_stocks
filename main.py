"""
2D Cutting Stock
"""
from typing import List
from random import randint
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Patch
import matplotlib.pyplot as plt
import greedypacker as g

# Assigning global variable for getting the cut pieces which are not fit in the sheet
list_extra = []

"""
Cutting Stock class for minimal wastage for the cutting sheet
"""


class CuttingStock:

    # getting the vertices
    def get_vertices(self, i: g.Item, margin: int = 0.0) -> List[int]:
        corners = [(i.x, i.y),
                   (i.x+i.width, i.y),
                   (i.x+i.width, i.y+i.height),
                   (i.x, i.y+i.height)]

        if margin:
            scalar = margin
            corners = [(i.x + scalar, i.y + scalar),
                       (i.x + i.width - scalar, i.y + scalar),
                       (i.x + i.width - scalar, i.y + i.height - scalar),
                       (i.x + scalar, i.y + i.height - scalar)]
        return corners
    
    # generating the  path and returing the vertices and the codes to map
    def generate_path(self, i: g.Item, margin: float = 0.0) -> Path:
        vertices = []
        codes = []
        codes += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
        vertices += self.get_vertices(i, margin) + [(0, 0)]

        vertices = np.array(vertices, float)
        return Path(vertices, codes)

    # Extra sheet left
    def draw_wastemap(self, binpack: g.BinManager) -> None:
        path = self.generate_path(binpack.bins[0].wastemap.freerects)
        return PathPatch(path, lw=2.0, fc='white', edgecolor='orange', hatch='/',  label='wastemap')

    # Extra pieces for cut but not fitted in the sheet
    def extra_cut(self, item):
        list_extra.append(item)

    # Calling the main function
    # getting the items from the user
    def render_bin(self, binpack: g.BinManager, save: bool = False) -> None:
        fig, ax = plt.subplots()
        zero = False
        non_zero = False
        
        # getting the cutting block and non-cutting block too
        # checking if the block having x =0 and y = 0 that means its first one.
        # if it has more then one that means it has extra block to cut whtich is not fitted in the sheet
        
        for item in binpack.items:
            if item.x != 0 and item.y != 0 or item.x == 0 and item.y != 0 or item.x != 0 and item.y == 0:
                path = self.generate_path(item)
                packed_item = PathPatch(
                    path, facecolor='blue', edgecolor='green', label='packed items')
                ax.add_patch(packed_item)
            elif item.x == 0 and item.y == 0 and zero == False:
                path = self.generate_path(item)
                packed_item = PathPatch(
                    path, facecolor='blue', edgecolor='green', label='packed items')
                ax.add_patch(packed_item)
                zero = True
            else:
                self.extra_cut(item)

        handles = [packed_item]

        # applying the algo
        if binpack.pack_algo == 'guillotine':
            
            for item in binpack.bins[0].freerects:
                path = self.generate_path(item, True)
                freerects = PathPatch(
                    path, fc='green', edgecolor='red', hatch='/', lw=1, label='freeRectangles')
                ax.add_patch(freerects)
                print(freerects)
            try:
                handles.append(freerects)
            except:
                pass

        # printing it
        ax.set_title('%s Algorithm ' % (M.pack_algo))
        ax.set_xlim(0, M.bin_width)
        ax.set_ylim(0, M.bin_height)

        plt.legend(handles=handles, bbox_to_anchor=(1.04, 1), loc="upper left")

        if save:
            plt.savefig('%s_Algorithm ' % (M.pack_algo),
                        bbox_inches="tight", dpi=150)
        else:
            plt.show()
        return

    # checking extra cut but we are not using it now
    def check_extra(self, max_x, max_y, list_of_cuts):
        max_size = max_x*max_y
        list_ = [list.width*list.height for list in list_of_cuts]
        list_to_cut = []
        for item in list_of_cuts:
            sum_ = 0
            for list in list_to_cut:
                if list:
                    sum_ += list.width*list.height

            total_ = sum_ + item.width*item.height
            if total_ > max_size:
                self.extra_cut(item)
            else:
                list_to_cut.append(item)

        return list_to_cut, list_extra


if __name__ == '__main__':

    CS = CuttingStock()
    Sheet_max_x = 500
    Sheet_max_y = 500

    # best_area
    # best_shortside
    # best_longside
    # worst_area
    # worst_shortside
    # worst_longside

    M = g.BinManager(Sheet_max_x, Sheet_max_y, pack_algo='guillotine',
                     heuristic='best_area', rectangle_merge=True, rotation=True)

    guillotine = [g.Item(50, 50),  g.Item(50, 50),  g.Item(100, 100), g.Item(100, 100), g.Item(100, 100), g.Item(100, 100), g.Item(100, 100), g.Item(200, 200), g.Item(200, 200), g.Item(200, 200), g.Item(200, 200), g.Item(
        200, 200), g.Item(200, 200), g.Item(200, 200), g.Item(150, 150), g.Item(101, 101), g.Item(50, 50), g.Item(50, 50), g.Item(100, 100), g.Item(100, 100), g.Item(100, 100), g.Item(100, 100), g.Item(100, 100)]

    M.add_items(*guillotine)
    M.execute()
    CS.render_bin(M, save=True)
    print("---- extra cuts ----")
    print(list_extra)
    print("---- ------- ----")
