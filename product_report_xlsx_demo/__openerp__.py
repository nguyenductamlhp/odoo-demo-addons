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
    'name': 'Product XLSX Report Demo',
    'version': '1.0',
    'category': '',
    'description': '''
        Demo XLSX Report using xlsxwriter
    ''',
    'author': 'Trobz',
    'website': 'http://www.trobz.com',
    'depends': [
        'report_xlsx'
    ],
    'data': [
        # Report
        'report/product_xlsx_report.xml',
    ],
    'qweb': [],
    'test': [],
    'demo': [],
    'installable': True,
    'active': False,
    'application': True,
}
