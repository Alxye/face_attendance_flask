from operation.my_approve import my_approve_operation

def my_approve_submit(date, staffID, appeal_reason, time_state, category):
    A_o = my_approve_operation()
    data = A_o._submit(date, staffID, appeal_reason, time_state, category)
    return data

def my_approve_get(staffID):
    A_o = my_approve_operation()
    data = A_o._get(staffID)
    return data