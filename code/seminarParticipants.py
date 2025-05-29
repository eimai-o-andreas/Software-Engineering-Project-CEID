class SeminarParticipants:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.participants = []
        self.participation_log = []  # νέα λίστα για καταγραφή συμμετοχών

   
    def updateParticipantList(self, seminar, parent_id):
    
            self.participants.append(parent_id)
            self.participation_log.append({
                'seminar_title': seminar.title,
                'seminar_datetime': seminar.datetime,
                'parent_id': parent_id
            })
            print(f"Προστέθηκε συμμετοχή για τον γονέα {parent_id}.")
            return True
    