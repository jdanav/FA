# -*- coding: utf-8 -*-
#!/usr/bin/env python

from tree import *
from Tkinter import *
import ttk, tkFileDialog, tkSimpleDialog, tkMessageBox
import FileDialog
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
matplotlib.use('TkAgg')

matplotlib.rcParams['figure.facecolor'] = 'white'


def rangeProb(master, title, xlabelticks, xlabel, ylabel, f1, f2):

    ind = xrange(len(xlabelticks))
    fig, ax = plt.subplots()

    f1line = ax.plot(xlabelticks, f1.values()[-2], label = u'ƒ1', lw = 2, color = 'r')
    f2line = ax.plot(xlabelticks, f2.values()[-2], label = u'ƒ2', lw = 2, color = 'y')

    ax.legend(loc = 'best', frameon = False)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title('%s\n' % title)
    ax.axes.set_xlim([f1.values()[0][0],f1.values()[0][-1]])

    plt.figure(1).canvas.set_window_title(title)
    plt.show()


def barProb(master, title, xlabelticks, xlabel, ylabel, f1, f2):

    f1Means, f1Devs = f1.values()[-2], f1.values()[-1]
    f2Means, f2Devs = f2.values()[-2], f2.values()[-1]

    ind = xrange(len(xlabelticks))
    width = 0.25
    fig, ax = plt.subplots()

    f1bars = ax.bar(ind, f1Means, width, color='r', ec = 'none', yerr = f1Devs, label = u'ƒ1', error_kw = dict(ecolor='black', lw=1, capsize=3, capthick=1))
    f2bars = ax.bar([i + width for i in ind], f2Means, width, color='y', ec = 'none', yerr = f2Devs, label = u'ƒ2', error_kw = dict(ecolor='black', lw=1, capsize=3, capthick=1))

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title('%s\n' % title)
    ax.set_xticks([i + width for i in ind])
    ax.set_xticklabels((str(i) for i in xlabelticks))

    ax.legend(loc = 'best', frameon = False, handlelength = 0.7)

    plt.figure(1).canvas.set_window_title('0.7')
    plt.show()


def stackProb(master, title, f1, f2, labels):

    for data, loc, lab in zip((f1,f2), ((1,1),(1,4)), labels):
        ax = plt.subplot2grid((10,7), loc, rowspan = 9, colspan = 2)
        labels = lab if lab else [i for i in data.keys()[1:-3]]
        ind = xrange(len(labels))
        ax.axes.set_xlim([0,1]); ax.axes.set_ylim([-1, len(ind)])
        fdata = [[data[y][M] for y in data.keys()[1:-3]] for M in xrange(len(data.values()[0]))]
        colors = [(.286, .0, .573), (.0, .427, .859), (.714, .427, 1.0),\
                    (.427, .714, 1.0), (.714, .859, 1.0), (.573, .0, .0), \
                    (.573, .286, .0), (.859, .427, .0), (.141, 1.0, .141), \
                    (1.0, 1.0, .427)] * len(ind)
        colors.reverse()
        pos = [0 for i in ind]
        height = [1 for i in ind] if lab else [0.8 for i in ind]

        for i in xrange(len(fdata)):
            ax.barh(ind,fdata[i], align = 'center', height = height, \
                    color = colors[i], label = data.values()[0][i], \
                    left = pos, ec = 'none')
            pos = [pos[j] + fdata[i][j] for j in xrange(len(fdata[i]))]
        ax.set_yticks(ind); ax.set_yticklabels(labels)
        ax.set_xticklabels(['%s%%' % i for i in xrange(0,101,20)])
        for spine in ax.spines: ax.spines[spine].set_color('none')
        ax.tick_params(axis='both', color ='none')

        if data == f1:
            ax.set_title(u'ƒ1\n')
            ax.legend(loc = 'upper center', frameon = False, bbox_to_anchor=(1.32,1), ncol = 1, handlelength = 0.7, fontsize = 12)
        else:
            ax.set_title(u'ƒ2\n')
            ax.yaxis.tick_right()
        ax.invert_yaxis()

    plt.suptitle('\n%s\n' % title, fontsize = 'large')
    plt.figure(1).canvas.set_window_title(title)
    plt.show()
