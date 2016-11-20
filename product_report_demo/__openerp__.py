# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2009-2016 Trobz (<http://trobz.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Demo Report',
    'version': '1.0',
    'category': '',
    'description': """
    """,
    'author': 'Trobz',
    'website': 'http://www.trobz.com',
    'depends': [
        'product',
    ],
    'data': [
        # ============================================================
        # DATA
        # ============================================================
        # 'data/',

        'reports/product_label.xml',

        # ============================================================
        # SECURITY SETTING - GROUP - PROFILE
        # ============================================================
        # 'security/',

        # ============================================================
        # VIEWS
        # ============================================================
        # 'view/',
        'views/product/product_template_view.xml',

        # ============================================================
        # MENU
        # ============================================================
        # 'menu/',


        # ============================================================
        # FUNCTION USED TO UPDATE DATA LIKE POST OBJECT
        # ============================================================
        # "data/bmg_update_functions_data.xml",

    ],

    "qweb": [

    ],

    'test': [],
    'demo': [],

    'installable': True,
}
