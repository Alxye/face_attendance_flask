from models.attendance_appeal import AttendanceAppeal


class my_approve_operation():
    def __init__(self):
        self.__fields__ = ['id', 'date', 'staff_id', 'appeal_reason', 'state', 'reject_reason', 'time_state',
                           'category']

    def _submit(self, date, staffID, appeal_reason, time_state, category):
        return AttendanceAppeal(date=date, staff_id=staffID, appeal_reason=appeal_reason, state=0, time_state=time_state,
                       category=category)

    def _get(self, staffID):
        return AttendanceAppeal.query.filter_by(staff_id=staffID).all()

