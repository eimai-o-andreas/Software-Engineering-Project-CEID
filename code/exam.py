class Exam:
    available_exams = {
        "Αιματολογική": 25,
        "Ακτινογραφία": 50,
        "Μαγνητική": 200,
        "Τεστ COVID": 30,
        "Ουρολογική": 40
    }

    @staticmethod
    def getExams():
        return Exam.available_exams