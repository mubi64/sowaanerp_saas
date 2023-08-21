import json

import frappe
from frappe.utils import add_to_date, today


def before_install():
    
    data = {
        'valid_till': add_to_date(today(), years=1)
    }
    with open(frappe.get_site_path('quota.json'), 'w') as outfile:
        json.dump(data, outfile, indent=2)

    file_path = frappe.utils.get_bench_path() + '/' + \
        frappe.utils.get_site_name(frappe.local.site) + \
        '/quota.json'

    print('\nfile quota.json created at ', file_path, 'with the following settings:')
    for key in data:
        print("\t{}: {}".format(key, data[key]))
    print('\nChange the values in quota.json to change settings\n')
