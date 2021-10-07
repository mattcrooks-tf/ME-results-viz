from layout import get_main_box_dimensions, get_inner_box_dimensions
from visualisation import NUMBER_INNER_BOXES


def add_arrows(ax, number_of_variants, NUMBER_INNER_BOXES):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)
    inner_box_width, inner_box_padding, inner_box_height = get_inner_box_dimensions(
        number_of_variants, NUMBER_INNER_BOXES)

    for variant_id in range(number_of_variants):
        box_id = NUMBER_INNER_BOXES - 2
        left_of_box = box_id * (inner_box_padding + inner_box_width) + inner_box_padding
        right_of_box = (1 + box_id) * (inner_box_padding + inner_box_width)
        arrow_center_ycoord = (variant_id + 0.5) * main_box_height + variant_id * main_box_spacing
        arrow_spacing = inner_box_width * 0.4
        arrowhead_size = 0.4 * (inner_box_width - 2 * arrow_spacing)
        arrow_line_width = 2
        # Arrow Line
        ax.plot([left_of_box + arrow_spacing,
                 right_of_box - arrow_spacing * 1.05],
                [arrow_center_ycoord] * 2,
                color='white',
                linewidth=arrow_line_width)
        #         # Arrow head
        ax.plot([right_of_box - arrow_spacing - arrowhead_size,
                 right_of_box - arrow_spacing,
                 right_of_box - arrow_spacing - arrowhead_size],
                [arrow_center_ycoord + arrowhead_size,
                 arrow_center_ycoord,
                 arrow_center_ycoord - arrowhead_size],
                color='white',
                linewidth=arrow_line_width)

    return ax