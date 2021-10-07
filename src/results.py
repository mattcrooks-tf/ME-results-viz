import numpy as np

from layout import get_main_box_dimensions, get_inner_box_dimensions
from visualisation import NUMBER_INNER_BOXES


def calculate_uplift(df):
    control = df.loc[df['variant_label'] == 'Control', 'Conversion-rate'].values[0]
    variant = df.loc[df['variant_label'] == 'Variant', 'Conversion-rate'].values[0]
    return np.round(100 * (variant - control) / control, 2)


def calculate_significance(_df, alpha_level):
    p = _df['Conversion-rate'].values / 100
    q = 1 - p
    n = _df['Audience'].values
    sig = np.sqrt(p * q / n)

    samplesA = np.random.normal(loc=p[0], scale=sig[0], size=100000)
    samplesB = np.random.normal(loc=p[1], scale=sig[1], size=100000)

    significance = np.mean(samplesB > samplesA)
    return significance >= 1 - alpha_level


def add_a_set_of_metrics(ax, metric_id, unit, metrics, variant_colours, number_of_variants):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)
    inner_box_width, inner_box_padding, inner_box_height = get_inner_box_dimensions(
        number_of_variants, NUMBER_INNER_BOXES)

    variant_colours_reversed = [variant_colours[-1 - i] for i in range(len(variant_colours))]
    for variant_id, variant_colour in enumerate(variant_colours_reversed):
        if variant_colour == 'silver':
            text_color = 'black'
        else:
            text_color = 'white'

        ax.text(x=(1 + metric_id) * inner_box_padding + (metric_id + 0.5) * inner_box_width,
                y=(variant_id + 0.5) * main_box_height + variant_id * main_box_spacing,
                s=f"{metrics[-1 - variant_id]}{unit}",
                horizontalalignment='center',
                verticalalignment='center',
                color=text_color)
    return ax


def add_metric_values(ax, df, variant_colours):
    number_of_variants = len(df.index)

    metric_id = 0
    unit = ''
    metrics = list(df['Audience'])
    ax = add_a_set_of_metrics(ax, metric_id, unit, metrics, variant_colours, number_of_variants)

    metric_id = 1
    unit = ''
    metrics = list(df['Conversions'])
    ax = add_a_set_of_metrics(ax, metric_id, unit, metrics, variant_colours, number_of_variants)

    metric_id = 3
    unit = '%'
    metrics = list(df['Conversion-rate'])
    ax = add_a_set_of_metrics(ax, metric_id, unit, metrics, variant_colours, number_of_variants)

    return ax


def get_variant_labels(number_of_variants):
    if number_of_variants == 2:
        return ['Control', 'Variant']
    if number_of_variants == 3:
        return ['Control', 'Variant A', 'Variant B']


def get_result_color(is_significant, pc_uplift):
    if not is_significant:
        return 'steelblue'
    elif pc_uplift >= 0:
        return 'forestgreen'
    elif pc_uplift < 0:
        return 'firebrick'
