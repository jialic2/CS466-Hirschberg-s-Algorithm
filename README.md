# Hirschberg's algorithm (CS466 FA20 Final Project)
This project is an implementation of the linear space global sequence alignment algorithm (i.e. [Hirschberg's algorithm](https://en.wikipedia.org/wiki/Hirschberg%27s_algorithm)), along with visualizations of alignments, and validation of correctness and memory usage. Our team members are 
Jiali Chen (jialic2), Guangya Wan (guangya2), and Eunice Zhou (xz33).

## Installing
Our code resides in a Jupyter Notebook `.ipynb` file, so you can either open the file locally with Jupyter Notebook or open the file using [Google Colab](https://colab.research.google.com/). You will need to clone this repository and have the `.ipynb` Notebook file locally.

- For instructions for running Jupyter Notebook file locally with JupyterLab, refer to the [JupyterLab installation guide](https://jupyter.org/install).

- For instructions for running Jupyter Notebook file with Google Colab, visit [Google Colab](https://colab.research.google.com/) and open the `.ipynb` file as prompted.

## Notebook

The notebook is broken down into the following sections: 

- Global sequence alignment
- Linear space algorithm
- Path reconstruction
- Visualization
- Correctness validation
- Alignment reconstruction
- Space complexity analysis

## Documentation

`global_score(sequence_1, sequence_2)`

Find the alignment score between sequence_1 and sequence_2 using global sequence alignment

`global_alignment(sequence_1, sequence_2)`

Find the actual alignment between sequence_1 and sequence_2 using global sequence alignment

`linear_space_score(sequence_1, sequence_2)`

Find the alignment score between sequence_1 and sequence_2 using Hirschberg's algorithm

`hirschberg(sequence_1, sequence_2)`

Run Hirscheberg's algorithm recursively to find the alignment between sequence_1 and sequence_2, return the list of cells that are reported by the algorithm

`reconstruct_path(sequence_1, sequence_2, reported_cells)`

Reconstruct the alignment between sequence_1 and sequence_2 using the reported cells returned by `hirschberg(sequence_1, sequence_2)`

`get_html_string(sequence_1, sequence_2, cells=None, title="")`

Return an HTML string to be used for visualizing the resulting sequence alignment. Call `HTML()` with the string passed in as argument to display the alignment in a table