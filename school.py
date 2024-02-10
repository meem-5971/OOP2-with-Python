class Student:
    def __init__(self,name,section,id) -> None:
        self.name=name
        self.section=section
        self.id=id

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, section: {self.section}, id: {self.id}'
    
class Teacher:
    def __init__(self,name,subj,id) -> None:
        self.name=name
        self.subj=subj
        self.id=id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subj}'
    
class School:
    def __init__(self,name) -> None:
        self.name=name
        self.teachers=[]
        self.student=[]

    def add_teacher(self,name,subject):
        id=len(self.teachers)+101
        teacher=Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id=len(self.teachers)+1
            student=Student(name,'P',id)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
        
    def __repr__(self) -> str:
        print('Welcome to ',self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for stdt in self.student:
            print(stdt)
        return 'All Done for now'
    
phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)

        
        
    
        