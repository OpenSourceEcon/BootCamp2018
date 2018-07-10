# OSM Lab: Computational Methods Section Materials

This directory in the repository contains all the materials for the computational methods section of the OSM Lab Boot Camp.


## Prerequisite and tutorial resources

We expect students in the Boot Camp to be jumping into Python at a level beyond an absolute beginner. Some Great resources for getting to that point include the following Jupyter Notebooks in the [Tutorials](https://github.com/OpenSourceMacro/BootCamp2018/tree/master/Tutorials) folder of this repository.

1. [PythonReadIn.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonReadIn.ipynb). This Jupyter notebook provides instruction on basic Python I/O, reading data into Python, and saving data to disk.
2. [PythonNumpyPandas.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonNumpyPandas.ipynb). This Jupyter notebook provides instruction on working with data using `NumPy` as well as Python's powerful data library `pandas`.
3. [PythonDescribe.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonDescribe.ipynb). This Jupyter notebook provides instruction on describing, slicing, and manipulating data in Python.
4. [PythonFuncs.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonFuncs.ipynb). This Jupyter notebook provides instruction on working with and writing Python functions.
5. [PythonVisualize.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonVisualize.ipynb). This Jupyter notebook provides instruction on creating visualizations in Python.
6. [PythonRootMin.ipynb](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonRootMin.ipynb). This Jupyter notebook provides instruction on implementing univariate and multivariate root finders and unconstrained and constrained minimizers using functions in the [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) sub-library.

We also recommend the ["Intro to Python" lab](http://www.acme.byu.edu/wp-content/uploads/2017/08/PythonIntro.pdf) from Brigham Young University's Math Department's Applied and Computational Math Emphasis (ACME) as well as the ["An Introductory Example"](https://lectures.quantecon.org/py/python_by_example.html) and ["Python Essentials"](https://lectures.quantecon.org/py/python_essentials.html) lectures from [QuantEcon](https://lectures.quantecon.org/py/).


## Schedule

The computational methods lab sessions for the OSM Lab will be held from 8:00-11:50am, Tuesday and Thursday in Saieh Hall, Room 247. The lab files in the schedule under the "Materials column" that start with "ACME" come from the Brigham Young University Math Department's [Applied and Computational Math Emphasis (ACME program)](http://www.acme.byu.edu/). These computational labs are open source. We cover only a subset of these excellent applied math Python labs, which are available in their entirety at [http://www.acme.byu.edu/2017-2018-materials/](http://www.acme.byu.edu/2017-2018-materials/). We highly recommend that you take time after the Boot Camp to work through some of the other labs that are available to you.

### Week 1

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
6-18  | M   |     |     |     |     |
6-19  | T   |     | Jan Ertl | [ACME: Intro to NumPy](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/NumpyIntro.pdf) | [Comp Prob Set 1](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/PyIntro_probset.pdf) |
|     |     |     |                 | [ACME: Standard Library](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/StandardLibrary.pdf) | due T, 6-26, 6pm |
|     |     |     |                 | [ACME: Unit Testing](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/UnitTesting.pdf) |   |
6-20  | W   |     |         |          |    |
6-21  | Th  |     | Jan Ertl | [ACME: Object Oriented Programming](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/ObjectOriented.pdf) |   |
|     |     |     |                 | [ACME: Exceptions and File I/O](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk1_PyIntro/Exceptions_FileIO.pdf) |   |
6-22  | F   |     |     |     |     |

### Week 2

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
6-25  | M   |     |     |     |     |
6-26  | T   | Visualizations | Jan Ertl | [Visualizations Notebook](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonVisualize.ipynb) | [Comp. Prob Set 2](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/DataVis_probset.pdf) |
|     |     | and Pandas  |    | [ACME: Intro to Matplotlib](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/MatplotlibIntro.pdf) | due T, 7-3, 6pm |
|     |     |     |    | [ACME: Data Visualization](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/DataVisualization.pdf) |   |
|     |     |     |    | [ACME: Pandas 1](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/Pandas1.pdf) |   |
|     |     |     |    | [ACME: Pandas 2](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/Pandas2.pdf) |   |
6-27  | W   |     |         |          |     |
6-28  | Th  | Visualizations | Jan Ertl | [Pandas Notebook](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Tutorials/PythonNumpyPandas.ipynb) |   |
|     |     | and Bokeh      |          | [ACME: Pandas 3](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/Pandas3.pdf) |    |
|     |     |      |          | [ACME: Pandas 4](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk2_DataVis/Pandas4.pdf) |    |
6-29  | F   |     |     |     |     |

### Week 3

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-2  | M  |  |  |  |  |
7-3  | T  |  Matrix Decomposition | Jan Ertl | [ACME: QR Decomp](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/QR_Decomposition.pdf) | [Comp Prob Set 3](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/Decomp_probset.pdf) |
|     |     |  |          | [ACME: Lsq, eigenvalues](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/LeastSquares_Eigenvalues.pdf) | due T, 7-10, 6pm |
|     |     |      |          | [ACME: SVD Image Compress](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/SVD_ImageCompression.pdf) |  |
7-4  | W    | NO CLASSES: HOLIDAY | NO CLASSES: HOLIDAY | NO CLASSES: HOLIDAY  |  |
7-5  | Th   | Matrix conditions | Jan Ertl | [ACME: Drazin Inverse](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/BlazinDrazin.pdf) |   |
7-6  | F    |     |     | [ACME: PageRank Algorithm](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/PageRank.pdf) |  |
|     |     |      |          | [ACME: Conditioning and Stability](https://github.com/OpenSourceMacro/BootCamp2018/blob/master/Computation/Wk3_Decomp/Conditioning_Stability.pdf) |  |

### Week 4

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-9  | M  |     |     |     |     |
7-10 | T  | Sparse Grids | [Simon Scheidegger](https://sites.google.com/site/simonscheidegger/) | [Simon's HPC repo](https://github.com/sischei/OSM2018) | Comp Prob Set 4  |
|     |     |   |     |  | due T, 7-17, 11pm |
7-11  | W  |     |     |     |    |
7-12  | Th | High Performance Computing | [Simon Scheidegger](https://sites.google.com/site/simonscheidegger/) | [Simon's HPC repo](https://github.com/sischei/OSM2018) |  |
7-13  | F  |     |     |     |     |

### Week 5

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-16  | M  |     |     |     |     |
7-17 | T  | High Performance Computing | [Simon Scheidegger](https://sites.google.com/site/simonscheidegger/) | [Simon's HPC repo](https://github.com/sischei/OSM2018) | Comp Prob Set 5  |
|     |     |   |     |  | due T, 7-24, 11pm |
7-18  | W  |     |     |     |    |
7-19  | Th | High Performance Computing | [Simon Scheidegger](https://sites.google.com/site/simonscheidegger/) | [Simon's HPC repo](https://github.com/sischei/OSM2018) |  |
7-20  | F  |     |     |     |     |


### Week 6

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-23  | M   |     |     |     |     |
7-24  | T   | Matrix conditions | Jan Ertl |  | Comp Prob Set 6 |
|     |     | Numerical Diff. and Int. |           |  | due T, 7-31, 6pm |
|     |     |     |      | [ACME: Numerical Differentiation](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_NumDiff.pdf) |  |
|     |     |     |      | [Evans: Numerical Integration](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/NumIntegr_Evans.pdf) |  |
7-25  | W   |     |     |     |    |
7-26  | Th  | Root finding | Jan Ertl | [ACME: Simplex Method](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_Simplex.pdf) |  |
|     |     |     |      | [ACME: Line Search Methods](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_LineSrch.pdf) |  |
|     |     |     |      | [ACME: Newton's Method](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_Newtons.pdf) |  |
|     |     |     |      | [ACME: Iterative Solvers](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_IterSolvers.pdf) |  |
7-27  | F   |     |     |     |     |

### Week 7

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-30 | M  |     |          |     |                   |
7-31 | T  |     | Jan Ertl |     | Comp. Prob. Set 7 |
8-1  | W  |     |          |     | due F, 8-3, 11pm  |
8-2  | Th |     | Jan Ertl |     |                   |
8-3  | F  | Conclusion: Hwk due |          |     |                   |

<!-- ### Week 5

| Date | Day | Topic | Instructor | Materials | Problem Set |
|:---:|:---:|:--- |:--- |:--- | --- |
7-17  | M   |     |     |     |     |
7-18  | T   | Minimization | Jan Ertl | [ACME: Interior Point, Linear Programs](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_IntPtLin.pdf) |  |
|     |     |     |      | [ACME: Interior Point, Quadratic Programs](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_IntPtQuad.pdf) |  |
|     |     |     |      | [ACME: Newton and Quasi Newton Methods](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_QuasNewt.pdf) |  |
|     |     |     |      | [ACME: Scipy.optimize](https://github.com/OpenSourceMacro/BootCamp2017/blob/master/Computation/Wk4_DifIntOpt/ACME_ScipyOpt.pdf) |  | -->


## References

* Humpherys, Jeffrey, "[Computational Labs for *Foundations of Applied Mathematics*](http://www.acme.byu.edu/2016-2017-materials/)" (2017).

