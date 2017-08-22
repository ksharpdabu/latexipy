#!/usr/bin/env python
from functools import partial
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import latexipy as lp


logging.basicConfig(level=logging.INFO)

DIRECTORY = Path(__file__).parent/'img'

_x = np.linspace(-np.pi, np.pi)


def plot_sin(x=_x):
    plt.plot(x, np.sin(x))
    plt.title('Sine')
    plt.xlabel(r'$\theta$')
    plt.ylabel('Value')


def plot_cos(x=_x):
    plt.plot(x, np.cos(x), color='C1')
    plt.title('Cosine')
    plt.xlabel(r'$\theta$')
    plt.ylabel('Value')


def plot_sin_and_cos(x=_x):
    plt.plot(x, np.sin(x), label='sine')
    plt.plot(x, np.cos(x), label='cosine')
    plt.title('Sine and cosine')
    plt.xlabel(r'$\theta$')
    plt.ylabel('Value')
    plt.legend()


PLOT_TYPES = {
    'sin': plot_sin,
    'cos': plot_cos,
    'sincos': plot_sin_and_cos,
}


def generate_figures(suffix, figure=lp.figure, plot_types=PLOT_TYPES):
    for plot_name, plot_function in plot_types.items():
        with figure(plot_name + suffix):
            plot_function()


if __name__ == '__main__':
    # If you are repeating arguments, you might want to register a partial.
    figure = partial(lp.figure, directory=DIRECTORY)

    # You can generate figures without calling lp.latexify().
    generate_figures('_no_latex', figure)

    # latexify chooses values that go well with publications.
    lp.latexify()
    generate_figures('_with_latex', figure)

    # You can use the partial function just as you would the original.
    with figure('sincos_defaults'):
        plot_sin_and_cos()

    # You can change the size. 0.45\textwidth is useful when using two columns.
    with figure('sincos_small', size=lp.figure_size(0.45)):
        plot_sin_and_cos()

    # A ratio of 1 is great for squares.
    with figure('sincos_square', size=lp.figure_size(ratio=1)):
        plot_sin_and_cos()

    # And we can have a high figure if, for instance, stacking subplots.
    with figure('sincos_tall', size=lp.figure_size(ratio=2)):
        plot_sin_and_cos()

    # It is equivalent to the original function with the right arguments.
    with lp.figure('sincos_defaults_no_partial', directory=DIRECTORY):
        plot_sin_and_cos()

    # You can change the parameters at any time. To increase the font size:
    font_size = 10
    params = lp.PARAMS.copy()
    params.update({param: font_size
                   for param in params
                   if 'size' in param})
    lp.latexify(params)

    with figure('sincos_big_font'):
        plot_sin_and_cos()
