from models.department import Department

class department_operation():
    def __init__(self):
        self.__fields__ = ['department_id', 'department_name','notice','clock_in_start','clock_in_end','clock_out_start','clock_out_end']

    def _all(self):
        department_list = Department.query.all()
        return department_list

    def _query_attendance_time(self,department_id,morning_flag):
        data =  Department.query.filter_by(department_id=department_id).first()
        if(morning_flag):
            return data.clock_in_start,data.clock_in_end
        else:
            return data.clock_out_start, data.clock_out_end

    def _query_departmentid_from_name(self,department_name):
        data = Department.query.filter_by(department_name=department_name).first()
        return data.department_id

    def _query_attendance_time2(self, department_id):
        data = Department.query.filter_by(department_id=department_id).first()
        return data.clock_in_start, data.clock_in_end, data.clock_out_start, data.clock_out_end

    def _query_notice(self, department_id):
        data = Department.query.filter_by(department_id=department_id).first()
        return data.notice
    def _query_location(self, department_id):
        data = Department.query.filter_by(department_id=department_id).first()
        return data.longitude, data.latitude