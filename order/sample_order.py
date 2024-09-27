from db_connection import py_connection
from datetime import datetime as dt

def insert_sample_order(request, decoded):
    try:
        Warp = request.get('Wrap', [])
        Weft = request.get('Weft', [])
        qry = ('{call Mobile.insert_sample_order_entry (?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?}')
        params = (request['Warp']['NoOfWarpCount'], request['Weft']['NoOfWeftCount'], request['CustomerName'], request['EPIOnTable'], request['PPIOnTable'],
                  request['Width'], request['Reed'], request['Transport'], request['LoomType'], request['LoomTypeId'],
                  request['PackingType'], request['OrderMeters'], request['ConstructionDetails'], request['PODate'], request['PONo'],
                  request['AgentName'], request['FabricRate'], request['DeliveryAddress'], request['DeliveryDate'], request['PaymentTerms'],
                  request['PaymentTermsId'], request.get('PaymentDays', 0), request['Remarks'], decoded['emp_fk'], decoded['emp_fk'])
        res = py_connection.call_prop_return_pk(qry, params)
        if res:
            insert_sample_order_details(res, Warp, decoded)
            insert_sample_order_details(res, Weft, decoded)

            return {"message": "Sample Order details inserted successfully", "rval": 1}

            # qry = ("insert into Mobile.SampleOrder(SampleOrderId,DocumentTypeId,Count,CountType,CountTypeId,"
            #        "MillName,MillId,PaymentTerms,PaymentTermsId,PaymentDays,"
            #        "Status,CreatedBy,CreatedDate,UpdatedBy,UpdatedDate) values(?,?,?,?,?,"
            #        "?,?,?,?,?,"
            #        "?,?,?,?,?)")
            # params = [(res, i, row['Count'], row['CountType'], row['MillName'],
            #            get_mill_id(row['MillName']), row['PaymentTerms'], row['PaymentTermsId'], row.get('PaymentDays', 0),
            #            1, decoded['emp_fk'], dt.now(), decoded['emp_fk'], dt.now()) for i, row in enumerate(Warp)]
            # py_connection.put_result2(qry, params)
            # qry1 = ("insert into Mobile.SampleOrder(SampleOrderId,DocumentTypeId,Count,CountType,CountTypeId,"
            #         "MillName,MillId,PaymentTerms,PaymentTermsId,PaymentDays,"
            #         "Status,CreatedBy,CreatedDate,UpdatedBy,UpdatedDate) values(?,?,?,?,?,"
            #         "?,?,?,?,?,"
            #         "?,?,?,?,?)")
            # params1 = [(res, i, row['Count'], row['CountType'], row['MillName'],
            #            get_mill_id(row['MillName']), row['PaymentTerms'], row['PaymentTermsId'], row.get('PaymentDays', 0),
            #            1, decoded['emp_fk'], dt.now(), decoded['emp_fk'], dt.now()) for i, row in enumerate(Weft)]
            # py_connection.put_result2(qry1, params1)
            # return {"message": "Sample Order details inserted successfully", "rval": 1}

    except Exception as e:
        print(str(e))
        return {"message": "Insertion of sample Order details failed", "rval": 0}


def insert_sample_order_details(sample_order_id, data, decoded):
    try:
        qry = ("insert into Mobile.SampleOrder(SampleOrderId, DocumentTypeId, Count, CountType, CountTypeId, "
               "MillName, MillId, PaymentTerms, PaymentTermsId, PaymentDays, "
               "Status, CreatedBy, CreatedDate, UpdatedBy, UpdatedDate) "
               "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

        params = [(sample_order_id, i, row['Count'], row['CountType'], get_mill_id(row['MillName']),
                   row['MillName'], row['PaymentTerms'], row['PaymentTermsId'], row.get('PaymentDays', 0),
                   1, decoded['emp_fk'], dt.now(), decoded['emp_fk'], dt.now())
                  for i, row in enumerate(data)]

        py_connection.put_result2(qry, params)

    except Exception as e:
        print(f"Failed to insert sample order details: {str(e)}")


def get_mill_id(MillName):
    try:
        qry = "select * from GMPWeaving.Mobile.Account where Name =" + str(MillName)
        res = py_connection.get_result(qry)
        return res[0][0]
    except Exception as e:
        print(str(e))