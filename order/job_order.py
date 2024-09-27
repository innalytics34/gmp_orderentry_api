from db_connection import py_connection
from datetime import datetime as dt
from filter.py_filter import FinancialYearM

def insert_job_order(request, decoded):
    try:
        print(request,"111")
        year = FinancialYearM()
        qry = ("insert into Mobile.JobOrderEntry([LogonUser],[BranchID],[LongDocumentNo],[DocumentDate],[Year],"
               "[DocumentTypeID],[Reed],[Pick],[Width],[OrderMeter],"
               "[OrderTypeID],[OrderType],[PininingPercentID],[PinningPercent],[PackingTypeID],"
               "[PackingType],[CustomerID],[CustomerName],[ConstructionBillingDetails],[AgentID],"
               "[AgentName],[PickCharge],[FabricProcessRate],[ConfirmRate],[Remarks],"
               "[Status],[WorkFlowStatus],[CreatedDate],[CreatedBy],[UpdatedDate],"
               "[UpdatedBy],[ADDD1],[ADDD2],[ADDD3],[ADDD4],"
               "[ADDD5],[ADDI1],[ADDI2],[ADDI3],[ADDI4],"
               "[ADDI5],[ADDT1],[ADDT2],[ADDT3],[ADDT4],"
               "[ADDT5],[ADDDT1],[ADDDT2],[ADDDT3],[ADDDT4],"
               "[ADDDT5]) values(?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?,?,?,?,?,"
               "?)")
        params = (decoded['emp_fk'], decoded['branch_id'], '', dt.now(), year['Year'][0]['UID'],
                  0, request['Reed'], request['Pick'], request['Width'], request['OrderMeter'],
                  request['OrderTypeId'], request['OrderType'], request['PininingPercentID'], request['PinningPercent'], request['PackingTypeID'],
                  request['PackingType'], 0, request['CustomerName'], request['ConstructionBillingDetails'], 0,
                  request['AgentName'], request['PickCharge'], request['FabricProcessRate'], request['ConfirmRate'], request['Remarks'],
                  1, 1, dt.now(), decoded['emp_fk'], dt.now(),
                  decoded['emp_fk'], 0.000, 0.000, 0.000, 0.000,
                  0.000, 0, 0, 0, 0,
                  0, '', '', '', '',
                  '', dt.now(), dt.now(), dt.now(), dt.now(),
                  dt.now())
        py_connection.put_result(qry, params)
        return {"message": "Job Order Entry details Added Successfully", "rval": 1}
    except Exception as e:
        print(str(e))
        return {"message": "Insertion of Job Order Entry details Failed", "rval": 0}


def edit_job_order_entry(request, decoded):
    try:
        qry = 'update Mobile.JobOrderEntry set '
    except Exception as e:
        print(str(e))