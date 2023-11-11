from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
from Enrollment import Enrollment

class LetterGrade(Enrollment):
    __tablename__ = "letter_grades"

    letterGradeID: Mapped[str] = mapped_column("letter_grade_id",
                                             ForeignKey("enrollments.enrollment_id", ondelete="CASCADE"),
                                             primary_key=True)
    minSatisfactory: Mapped[str] = mapped_column("min_satisfactory", String,
                                                 CheckConstraint("min_satisfactory IN('A', 'B', 'C', 'D', 'F')",
                                                                 name= "grade_validator"), nullable=False)
    __mapper_args__ = {"polymorphic_identity": "letter_grade"}

    def __init__(self, section, student, min_satisfactory: String):
        super().__init__(section, student)
        self.minSatisfactory = minSatisfactory

    def __str__(self):
        return f"Letter Grade: {super().__str__()}"
