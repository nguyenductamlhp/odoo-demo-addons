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

from openerp.addons.report_xlsx.report.report_xlsx import ReportXlsx


class ProductXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, products):

        # Prepare Cell Styles
        bold = workbook.add_format({'bold': True})
        bold_itatic = workbook.add_format({'bold': True,
                                           'italic': True})

        header_style = workbook.add_format({'bold': True, 'size': 20})

        row_pos = 0

        # Create a new sheet named Product List
        sheet = workbook.add_worksheet('Product List')

        # Create Report Title
        sheet.write(row_pos, 5, 'Product List', header_style)

        # Create Report Column
        row_pos += 1
        column_title = ['No.', 'Internal Reference',
                        'Product Name', 'Sale Price']

        col_pos = 0
        for title in column_title:
            sheet.write(row_pos, col_pos, title, bold_itatic)
            col_pos += 1

        # Product List
        row_pos +=1

        number = 1
        for prod in products:
            data = [number, prod.default_code or '',
                    prod.name, prod.list_price]
            col_pos = 0
            for item in data:
                sheet.write(row_pos, col_pos, item)
                col_pos += 1
            row_pos += 1


ProductXlsx('report.product.demo.xlsx', 'product.product')
