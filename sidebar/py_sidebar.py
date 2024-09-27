from db_connection import py_connection


def main_menu(decoded):
    try:
        qry = (
            "SELECT menupk, menu_description as 'text', path, icon, sublist_fk "
            "FROM Mobile.SideBar WHERE is_active in (1) AND privilage LIKE '%{role}%' "
            "ORDER BY [order] ASC"
        ).format(role=decoded['role'])

        res, k = py_connection.get_result_col(qry)
        menu_dict = {}

        # Organize menus by sublist_fk
        for row in res:
            menu_item = dict(zip(k, row))
            menu_dict.setdefault(row[k.index('sublist_fk')], []).append(menu_item)

        # Recursive function to build sublist hierarchy
        def build_sublist(menu_fk):
            sublist = []
            if menu_fk in menu_dict:
                for item in menu_dict[menu_fk]:
                    item['items'] = build_sublist(item['menupk'])
                    keys = ['menupk', 'sublist_fk']
                    for key in keys:
                        item.pop(key, None)
                    if item['items'] in ([], '', None):
                        item.pop('items')
                    sublist.append(item)
            return sublist

        # Build main menu
        menu = build_sublist(0)
        return {"main_menu": menu}

    except Exception as e:
        print(str(e))
        return {"main_menu": []}