from orm_base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from Enrollment import Enrollment

class LetterGrade(Base):
    __tablename__ = "letter_grade"
    minSatisfactory: Mapped[str] = mapped_column("min_satisfactory", String(10), nullable=False)



    def __init__(self, section, student, minSatisfactory: str):
        super().__init__(section, student)
        self.minSatisfactory = minSatisfactory

    def __str__(self):
        return f"Letter grade: {super().__str__}"