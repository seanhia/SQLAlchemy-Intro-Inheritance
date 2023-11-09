from orm_base import Base
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from Enrollment import Enrollment

class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"

    letterGrade: Mapped[str] = mapped_column("letter_grade",
                                             ForeignKey("enrollments.enrollment_id", ondelete="CASCADE"),
                                             primary_key=True)
    minSatisfactory: Mapped[str] = mapped_column("min_satisfactory", String(10), nullable=False)

    __mapper_args__ = {"polymorphic_identity":"letter_grade"}

    def __init__(self, section, student, minSatisfactory: str):
        super().__init__(section, student)
        self.minSatisfactory = minSatisfactory

    def __str__(self):
        return f"Letter grade: {super().__str__}"