from visualisation import NUMBER_INNER_BOXES


def add_inner_boxes(ax, number_of_variants, NUMBER_INNER_BOXES):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)
    inner_box_width, inner_box_padding, inner_box_height = get_inner_box_dimensions(
        number_of_variants, NUMBER_INNER_BOXES)

    inner_box_ycoords_default = [
        inner_box_padding,
        inner_box_padding,
        main_box_height - inner_box_padding,
        main_box_height - inner_box_padding]

    for inner_box_row in range(number_of_variants):
        inner_box_ycoords = [
            inner_box_row * (main_box_height + main_box_spacing) + y
            for y in inner_box_ycoords_default]
        ax = add_row_of_inner_boxes(ax, inner_box_ycoords, number_of_variants)

    return ax


def get_inner_box_dimensions(number_of_variants, NUMBER_INNER_BOXES):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)

    NUMBER_INNER_BOXES = 4
    inner_box_padding = main_box_spacing / 2
    inner_box_height = main_box_height - 2 * inner_box_padding

    inner_box_width = (
                              main_box_width - (NUMBER_INNER_BOXES + 1) * inner_box_padding
                      ) / NUMBER_INNER_BOXES

    return inner_box_width, inner_box_padding, inner_box_height


def get_main_box_dimensions(number_of_variants):
    """
    Returns main_box_width, main_box_spacing, main_box_height
    """
    main_box_width = number_of_variants
    main_box_spacing = 0.1 * number_of_variants / 2
    main_box_height = 0.45 * number_of_variants / 2
    return main_box_width, main_box_spacing, main_box_height


def add_main_boxes(ax,
                   number_of_variants,
                   outer_box_color=['silver', 'forestgreen']):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)

    # Outer Boxes
    for outerbox_id in range(number_of_variants):
        box_lower_ycoord = outerbox_id * (main_box_height + main_box_spacing)

        ax.fill([0, main_box_width, main_box_width, 0],
                [box_lower_ycoord, box_lower_ycoord,
                 box_lower_ycoord + main_box_height,
                 box_lower_ycoord + main_box_height],
                color=outer_box_color[-1 - outerbox_id],
                alpha=0.5)

    return ax


def add_row_of_inner_boxes(
        ax, inner_box_ycoords,
        number_of_variants,
        NUMBER_INNER_BOXES=4):
    main_box_width, main_box_spacing, main_box_height = get_main_box_dimensions(
        number_of_variants)

    inner_box_height = 0.3
    inner_box_padding = 0.05
    inner_box_width = (
                              main_box_width - (NUMBER_INNER_BOXES + 1) * inner_box_padding
                      ) / NUMBER_INNER_BOXES

    for inner_box_id in range(NUMBER_INNER_BOXES):
        if inner_box_id != NUMBER_INNER_BOXES - 2:
            if inner_box_id == 0:
                padding = [inner_box_padding, 0.5 * inner_box_padding]
                left_jump_spacing = inner_box_padding
            elif inner_box_id == NUMBER_INNER_BOXES - 1:
                padding = [0.5 * inner_box_padding, inner_box_padding]
                left_jump_spacing = (
                        main_box_width - inner_box_width - inner_box_padding)
            else:
                padding = [0.5 * inner_box_padding, 0.5 * inner_box_padding]
                left_jump_spacing = (
                        inner_box_id * inner_box_width + (1 + inner_box_id) * inner_box_padding)
            ax.fill([left_jump_spacing,
                     left_jump_spacing + inner_box_width,
                     left_jump_spacing + inner_box_width,
                     left_jump_spacing],
                    inner_box_ycoords,
                    color='white', alpha=0.2)

    return ax
