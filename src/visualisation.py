# Databricks notebook source

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


from arrows import *
from layout import *
from results import *
from visualisation import *
from viz_text import *


NUMBER_INNER_BOXES = 4


def plot_results(df, alpha_level):
    number_of_variants = len(df.index)
    

    is_significant = calculate_significance(df, alpha_level)
    pc_uplift = calculate_uplift(df)

    result_colour = get_result_color(is_significant, pc_uplift)

    variant_labels = get_variant_labels(number_of_variants)
    variant_colours = ['silver', result_colour, 'silver'][:number_of_variants]

    f, ax = plt.subplots(figsize=(10, 2.5 * number_of_variants))
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.facecolor = (0.0, 1.0, 0.0, 0.5)

    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)
    inner_box_width, inner_box_padding, inner_box_height = get_inner_box_dimensions(
        number_of_variants, NUMBER_INNER_BOXES)

    #     # Outer Boxes
    ax = add_main_boxes(ax, number_of_variants, outer_box_color=variant_colours)

    #     # Inner boxes
    ax = add_inner_boxes(ax, number_of_variants, NUMBER_INNER_BOXES)

    #     # Add labels
    ax = add_text_labels(ax, variant_labels)

    #     # Add Arrows
    ax = add_arrows(ax, number_of_variants, NUMBER_INNER_BOXES)

    #     # Add result text
    ax = add_result_text(ax, number_of_variants, is_significant, pc_uplift, result_colour, alpha_level=alpha_level)

    #     # Add Data Values
    ax = add_metric_values(ax, df, variant_colours)

    return f, ax