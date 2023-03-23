from operation.my_attendance import my_attendance_operation


def Attendance_search_all(staffID):
    A_o = my_attendance_operation()
    data = A_o._search_all_record(staffID)
    return data