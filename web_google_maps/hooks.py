# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


def uninstall_hook(cr, registry):
    """
    In creating map view often we must overwrite existing action
    This removes reference to available map view on removal of module
    :param cr:
    :param registry:
    :return:
    """
    cr.execute("UPDATE ir_act_window "
               "SET view_mode=replace(view_mode, ',map', '') "
               "WHERE view_mode LIKE '%map%';")
    # In case its the start
    cr.execute("UPDATE ir_act_window "
               "SET view_mode=replace(view_mode, 'map,', '') "
               "WHERE view_mode LIKE '%map%';")
    # In rare case of user defined action of which map is only view
    cr.execute("DELETE FROM ir_act_window "
               "WHERE view_mode = 'map';")
    return True
