from models.attendance import Attendance



class my_attendance_operation():
    def __init__(self):
        self.__fields__ = ['clock_in_time', 'clock_out_time', 'am_type', 'pm_type', 'am_address', 'pm_address',
                           'salary', 'staff_id', 'date']

    def _search_all_record(self, staffID):
        return Attendance.query.filter_by(staff_id=staffID).all()
