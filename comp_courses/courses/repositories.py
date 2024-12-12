from .models import Course

class CourseRepository:
    @staticmethod
    def get_all_courses():
        return Course.objects.all()

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.get(id=course_id)

    @staticmethod
    def create_course(data):
        return Course.objects.create(**data)

    @staticmethod
    def update_course(course, data):
        for key, value in data.items():
            setattr(course, key, value)
        course.save()
        return course

    @staticmethod
    def delete_course(course):
        course.delete()
