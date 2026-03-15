This is a visualizaition of some sorting algorithms.
The sorting steps of each algorithm are visualized through bars representing numbers in a list that are sorted step by step

## Python Scripts
* list_generator.py: generates a sample list to be used to visualize the algorithms
* gnome_sort.py: A class written to visualize gnome sorting algorithm and can be used in visualizer.py
* insertion_sort.py: A class written to visualize insertion sorting algorithm and can be used in visualizer.py
* merge_sort.py: an independent script that visualizes merge sort algorithm itself upon running.

## Working
* A sample list of a given size is generated through list_generator.py
* This list is used in visualizer.py and merge_sort.py
* visualizer.py runs visualizations of gnome_sort and insertion_sort.
* merge_sort.py independently runs its visualization upon running.
* The sample list is visualized in form of green bars of different heights being sorted from smallest to largest.

## Requirements
Requires Pygame supported python version to be run.