# Two Dimensional Bin Packing


A 2D bin packing library based on on Jukka Jylänki's article "A Thousand
Ways to Pack the Bin - A Practical Approach to Two-Dimensional Rectangle Bin
Packing."

This library is intended for offline packing. All algorithms
heuristics and optimizations from Jukka's article are included.

A web demo made with Flask and ReactJS is available ["here"](https//:google.com)
Packing performance varies drastically with different combinations of optimizations and
datasets, so its important to under the settings and test a variety of them.


#### Algorithms


##### ["Guillotine"](https://github.com/ssbothwell/greedypacker/blob/master/docs/guillotine.md)


#### General Optional Parameters:

All optimizations are passed in as keyword arguments when the GreedyPacker
instance is created:

##### Item Rotation
Item rotation can be disabled with the keyword argument `rotation=False`

##### Item Pre-Sort
Items can be pre-sorted according to a number of settings for 
the 'sorting_heuristic' keyword argument:

* ASCA: Sort By Area Ascending
* DESCA: Sort By Area Descending (This is the default setting)
* ASCSS: Sort By Shorter Side Ascending
* DESCSS: Sort By Shorter Side Descending
* ASCLS: Sort By Longer Side Ascending
* DESCLS: Sort By Longer Side Descending
* ASCPERIM: Sort By Perimeter Ascending
* DESCPERIM: Sort By Perimeter Descending
* ASCDIFF: Sort by The ABS Difference Between Sides Ascending
* DESCDIFF: Sort By The ABS Difference Between Sides Descending
* ASCRATIO: Sort By The Ratio of The Sides Ascending
* DESCRATIO: Sort By The Ratio of The Sides Descending


### install notes

Requires Python`>=3.0`.  


```
pip install -r requirements.txt

python main.py

