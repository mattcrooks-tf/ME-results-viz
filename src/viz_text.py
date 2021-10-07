import numpy as np

from layout import get_main_box_dimensions, get_inner_box_dimensions
from visualisation import NUMBER_INNER_BOXES


def get_significant_title(is_significant):
    if is_significant:
        text = "Significant Result!"
    else:
        text = "Result not significant!"
    return text


def round_confidence(alpha_level):
    if alpha_level == 0.05:
        return 95
    elif alpha_level == 0.025:
        return 97.5


def get_result_text(is_significant, pc_uplift, alpha_level):
    pc_uplift = np.round(pc_uplift, 2)

    if (pc_uplift >= 0) & is_significant:
        text = f"""The Variant's conversion-rate is {pc_uplift}%
higher than the Control. 

There is more than a {round_confidence(alpha_level)}% chance
that the Variant will deliver a higher 
conversion-rate than the Control.
    """
    elif (pc_uplift >= 0) & (not is_significant):
        text = f"""The Variant's conversion-rate is {pc_uplift}%
higher than the Control. 

But, there is more than a {100 - round_confidence(alpha_level)}% chance
that the Variant will deliver a lower 
conversion-rate than the Control.
    """
    elif (pc_uplift < 0) & is_significant:
        text = f"""The Variant's conversion-rate is {-pc_uplift}%
lower than the Control. 

There is more than a {round_confidence(alpha_level)}% chance
that the Variant will deliver a lower 
conversion-rate than the Control.
    """
    elif (pc_uplift < 0) & (not is_significant):
        text = f"""The Variant's conversion-rate is {-pc_uplift}%
lower than the Control. 

But, there is more than a {100 - round_confidence(alpha_level)}% chance
that the Variant will deliver a higher 
conversion-rate than the Control.
    """

    return text


def add_result_text(ax, number_of_variants, is_significant,
                    pc_uplift, result_colour, alpha_level=0.05):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)

    ax.text(x=main_box_width + 2 * main_box_spacing,
            y=number_of_variants * main_box_height + (number_of_variants - 2) * main_box_spacing,
            s=get_significant_title(is_significant),
            horizontalalignment='left',
            verticalalignment='top',
            color=result_colour,
            fontsize=30,
            alpha=0.5)

    ax.text(x=main_box_width + 2 * main_box_spacing,
            y=number_of_variants * main_box_height + (number_of_variants - 4) * main_box_spacing,
            s=get_result_text(is_significant, pc_uplift, alpha_level),
            horizontalalignment='left',
            verticalalignment='top',
            color='silver',
            fontsize=15,
            alpha=1)
    return ax


def add_text_labels(ax, variant_labels):
    number_of_variants = len(variant_labels)
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)
    inner_box_width, inner_box_padding, inner_box_height = get_inner_box_dimensions(
        number_of_variants, NUMBER_INNER_BOXES)

    top_label_ycoord = (main_box_height + main_box_spacing) * number_of_variants
    ax.text(x=inner_box_padding + 0.5 * inner_box_width,
            y=top_label_ycoord,
            s='Visitors',
            color='black',
            fontsize=16,
            horizontalalignment='center')
    ax.text(x=2 * inner_box_padding + 1.5 * inner_box_width,
            y=top_label_ycoord,
            s='Conversions',
            color='black',
            fontsize=16,
            horizontalalignment='center')
    ax.text(x=4 * inner_box_padding + 3.5 * inner_box_width,
            y=top_label_ycoord,
            s='Conversion-rate',
            color='black',
            fontsize=16,
            horizontalalignment='center')

    variant_labels_reversed = [variant_labels[-1 - i] for i in range(len(variant_labels))]
    for variant_id, variant_label in enumerate(variant_labels_reversed):
        ax.text(x=-inner_box_padding,
                y=variant_id * (main_box_height + main_box_spacing) + 0.5 * main_box_height,
                s=variant_label,
                color='black', fontsize=16,
                horizontalalignment='right',
                verticalalignment='center')

    return ax
