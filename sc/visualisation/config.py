from __future__ import absolute_import
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns


# SEA-BORN Modification
def set_style(size=(12, 8), font=1.8):
    """Initialisation the fig and font size with seaborn for unification graphs"""
    plt.style.use(['seaborn-white', 'seaborn-paper'])
    matplotlib.rc("font", family="Times New Roman")
    sns.set(rc={'figure.figsize': size})
    sns.set(font_scale=font)
    sns.set_style("whitegrid")
