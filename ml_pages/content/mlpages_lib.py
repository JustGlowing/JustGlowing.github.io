import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from myst_nb import glue

import matplotlib as mpl
from cycler import cycler
colors_cycle = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

#colors_cycle= ['#0080e8', '#70d0ff', '#98f098',
#               '#ffa000', '#009900', '#c00060'][::-1]

#colors_cycle = ['#c44129', '#ec9332', '#3e8410', '#0560bd'][::-1]

colors_cycle = ['#30a2da', '#fc4f30', '#e5ae38', '#6d904f', '#8b8b8b']

mpl.rcParams['figure.figsize'] = [1.0, 8.0]
mpl.rcParams['axes.edgecolor'] = '#999999'
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.color'] = '#999999'
mpl.rcParams['axes.labelsize'] = 18
mpl.rcParams['axes.labelweight'] = 2
mpl.rcParams['axes.titlesize'] = 18
mpl.rcParams['axes.titleweight'] = 3
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['xtick.bottom'] = False
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.left'] = False
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.prop_cycle'] = cycler('color', colors_cycle)
mpl.rcParams['boxplot.patchartist'] = True
mpl.rcParams['boxplot.boxprops.linewidth'] = 2.
mpl.rcParams['boxplot.medianprops.linewidth'] = 2.
mpl.rcParams['axes.axisbelow'] = True