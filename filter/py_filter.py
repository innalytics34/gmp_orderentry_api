from db_connection import py_connection

def orderType():  # Order Type Dropdown
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 13"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"orderType": lst}
        else:
            return {"orderType": lst}
    except Exception as e:
        print(str(e))
        return {"orderType": []}

def PinningPercent():  # Pinning Percent Dropdown
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 7"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"PinningPercent": lst}
        else:
            return {"PinningPercent": lst}
    except Exception as e:
        print(str(e))
        return {"PinningPercent": []}

def PackingType():  # Packing Type Dropdown
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 9"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"PackingType": lst}
        else:
            return {"PackingType": lst}
    except Exception as e:
        print(str(e))
        return {"PackingType": []}


def CountType():
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"CountType": lst}
        else:
            return {"CountType": lst}
    except Exception as e:
        print(str(e))
        return {"CountType": []}


def LoomType():
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 6"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"LoomType": lst}
        else:
            return {"LoomType": lst}
    except Exception as e:
        print(str(e))
        return {"LoomType": []}


def PaymentTerms():
    try:
        return {
            "PaymentTerms": [
                {"UID": 1, "Description": 'Advance'},
                {"UID": 2, "Description": 'Days'}
            ]
        }
    except Exception as e:
        print(str(e))
        return {"PaymentTerms": []}

def PurchaseMode():
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 2"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"PurchaseMode": lst}
        else:
            return {"PurchaseMode": lst}
    except Exception as e:
        print(str(e))
        return {"PurchaseMode": []}

def TransportMode():
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 3"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"TransportMode": lst}
        else:
            return {"TransportMode": lst}
    except Exception as e:
        print(str(e))
        return {"TransportMode": []}


def FreightRate():
    try:
        return {
            "FreightRate": [
                {"UID": 1, "Description": 'Included'},
                {"UID": 2, "Description": 'Not Included'}
            ]
        }
    except Exception as e:
        print(str(e))
        return {"FreightRate": []}


def FabricType():
    try:
        qry = "select UID,MasterTypeId,Description from [Mobile].[MasterM] where Status = 1 and MasterTypeId = 8"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"FabricType": lst}
        else:
            return {"FabricType": lst}
    except Exception as e:
        print(str(e))
        return {"FabricType": []}


def FinancialYearM():  # Financial Year
    try:
        qry = "select UID,FinancialYear from dbo.FinancialYearM where Active = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"Year": lst}
        else:
            return {"Year": lst}
    except Exception as e:
        print(str(e))
        return {"Year": []}