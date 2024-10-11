class Course:
    def __init__(Saif, CourseCode, CourseName):
        Saif.CourseCode = CourseCode
        Saif.CourseName = CourseName

    def DisplayInfo(Saif):
        print(f"Course Code: {Saif.CourseCode}, Course Name: {Saif.CourseName}")


class UndergraduateCourse(Course):
    def __init__(Saif, CourseCode, CourseName, YearLevel):
        super().__init__(CourseCode, CourseName)
        Saif.YearLevel = YearLevel

    def AdditionalInfo(Saif):
        print(f"Year Level: {Saif.YearLevel}")


class GraduateCourse(Course):
    def __init__(Saif, CourseCode, CourseName, ResearchArea):
        super().__init__(CourseCode, CourseName)
        Saif.ResearchArea = ResearchArea

    def AdditionalInfo(Saif):
        print(f"Research Area: {Saif.ResearchArea}")


def RegisterCourse():
    CourseType = input("Enter course type (undergraduate/graduate): ").strip().lower()
    CourseCode = input("Enter course code: ")
    CourseName = input("Enter course name: ")

    if CourseType == "undergraduate":
        YearLevel = input("Enter year level: ")
        Course = UndergraduateCourse(CourseCode, CourseName, YearLevel)
    elif CourseType == "graduate":
        ResearchArea = input("Enter research area: ")
        Course = GraduateCourse(CourseCode, CourseName, ResearchArea)
    else:
        print("Invalid course type.")
        return

    Course.DisplayInfo()
    Course.AdditionalInfo()


RegisterCourse()
