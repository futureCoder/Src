# -*-coding:utf-8-*-
"""Class blah"""


class Item(object):
    """Class to represent an item"""

    def __init__(self, rune_id, pos, rune_type, star_row, main_prop, evil_prop, prop_type_val):
        """Init"""
        self.rune_id = rune_id
        self.pos = pos
        self.rune_type = rune_type
        self.star_row = star_row
        self.main_prop = main_prop
        self.evil_prop = evil_prop
        self.prop_type_val = prop_type_val

    def get_id(self):
        return self.rune_id

    def get_pos(self):
        return self.pos

    def get_type(self):
        return self.rune_type

    def get_star_row(self):
        return self.star_row

    def get_main_prop(self):
        return self.main_prop

    def get_evil_prop(self):
        return self.evil_prop

    def get_prop_type_val(self):
        return self.prop_type_val

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(self.rune_id, self.pos, self.rune_type, self.star_row,
                                                          self.main_prop, self.evil_prop, self.prop_type_val)
