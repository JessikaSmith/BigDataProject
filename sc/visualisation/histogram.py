from .config import *


def plot_Hist(data, save=False, bins=None, x_lim=(0, 320), color='firebrick', title='Lenght of Twitts',
              _xlabel='Lenght', yscale='linear'):
    ax = sns.distplot(data, bins=bins, color=color, norm_hist=False, kde=False, hist_kws={"alpha": 0.8},
                      label='Sample')
    ax.set_yscale(yscale)
    ax.set(xlabel=_xlabel, ylabel='Num. of tweets, ' + yscale + ' scale')
    plt.plot([140, 140], [0, 350000], ls='--', linewidth=2, color='#0084b4')
    plt.xlim(x_lim)
    plt.legend(loc=1)
    plt.tight_layout()
    if save:
        if not os.path.exists('Images/Histograms/'):
            os.makedirs('Images/Histograms/')
        plt.savefig('Images/Histograms/' + title + '.png')
    plt.show()
