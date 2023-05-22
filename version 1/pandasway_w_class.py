import pandas as pd
import numpy as np

studentsFile = 'students.csv'
courseFile = 'course.csv'

'''
# Creating the first Dataframe using dictionary
df1 = df = pd.DataFrame({"a":[1, 2, 3, 4],
                         "b":[5, 6, 7, 8]})

# Creating the Second Dataframe using dictionary
df2 = pd.DataFrame({"a":[1, 2, 3],
                    "b":[5, 6, 7]})
'''
# csvRead = pd.read_csv(studentsFile)


def init_Student():
    studentsCSV = pd.DataFrame(columns=['name', 'id', 'course'])
    studentsCSV.to_csv(studentsFile, mode='w', index=False)
    return studentsCSV


def init_Course():
    courseCSV = pd.DataFrame(columns=['course'])
    courseCSV.to_csv(courseFile, mode='w', index=False)
    return courseCSV


class pandasway_object(object):
    courseCSV = None
    studentsCSV = None
    try:
        courseCSV = pd.read_csv(courseFile)
    except:
        courseCSV = init_Course()
        studentsCSV = init_Student()
    try:
        studentsCSV = pd.read_csv(studentsFile)
    except:
        studentsCSV = init_Student()
    # def __init__(self):

    def studentInCSV(self, newEntry):
        # if len(self.studentsCSV.values) == 0: return False
        for row in self.studentsCSV.values:
            if row[0] == newEntry[0] or row[1] == newEntry[1]:
                return True
        return False

    def courseInCSV2(self, courses, newCourse):
        for course in courses:
            if course == newCourse:
                return True
        return False

    def courseInCSV(self, newCourse):
        self.courseCSV = pd.read_csv(courseFile)
        for course in self.courseCSV.values:
            if course == newCourse:
                return True
        return False

    def addEntry(self, row):
        # csvRead = pd.read_csv(studentsFile)
        # if not inCSV(row):
        # csvRead = pd.read_csv(studentsFile)
        temp = pd.DataFrame({'name': row[0],
                             'id': row[1],
                             'course': row[2]}, index=[0])
        self.studentsCSV = pd.concat(
            [self.studentsCSV, temp], ignore_index=True)
        temp.to_csv(studentsFile, mode='a',
                    index=False, header=False)
        print(self.studentsCSV)
        '''
        self.studentsCSV = self.studentsCSV.append({'name': row[0],
                                                    'id': row[1],
                                                    'course': row[2]}, ignore_index=True)
                                                    '''

        # self.studentsCSV = pd.read_csv(studentsFile)

    def addCourse(self, courseName):
        # [courseName]}, index=[len(courseCSV)]
        print("addCourse is called \n \n")
        print(courseName)
        temp = pd.DataFrame(
            {'course': courseName}, index=[0])
        self.courseCSV = pd.concat(
            [self.courseCSV, temp], ignore_index=True)
        # self.courseCSV = self.courseCSV.append({'course': courseName}, ignore_index=True)
        temp.to_csv(courseFile, mode='a',
                    index=False, header=False)

        # temp = pd.DataFrame({'course': [courseName]})
        # temp.to_csv(courseFile, mode='a', index=False, header=False)
        # self.courseCSV = pd.read_csv(courseFile)
        # print("Course set!")
        return "Course set!"

    def deleteEntry(self, index):
        if len(index) == 1:
            index = index[0]
        # print(index)
        # self.studentsCSV = pd.read_csv(studentsFile)
        # studentsCSV = studentsCSV[studentsCSV.name != nameInEntry]
        self.studentsCSV = self.studentsCSV.drop(index)
        self.studentsCSV = self.studentsCSV.reset_index(drop=True)
        print(self.studentsCSV)
        self.studentsCSV.to_csv(studentsFile, mode='w', index=False)

    def deleteCourse(self, index):
        # if len(index) == 1:index = index[0]
        # self.courseCSV = pd.read_csv(courseFile)
        courseOfEntry = [self.courseCSV.values[i][0]
                         for i in index]
        # if courseInCSV2(courseCSV.values, courseOfEntry):
        self.courseCSV = self.courseCSV.drop(index)
        self.courseCSV = self.courseCSV.reset_index(
            drop=True)
        self.courseCSV.to_csv(courseFile, mode='w', index=False)

        # return arr for deletion of rows in gui's studentTable
        arr = self.studentsCSV[self.studentsCSV['course'].isin(
            courseOfEntry)].index.tolist()
        print("arr is ")
        print(arr)
        self.studentsCSV.drop(self.studentsCSV[self.studentsCSV['course'].isin(
            courseOfEntry)].index, inplace=True)
        self.studentsCSV.to_csv(
            studentsFile, mode='w', index=False)
        return arr

    '''
    # parameter is 'name'
    def deleteCourse(courseOfEntry):
        courseCSV = pd.read_csv(courseFile)
        if courseInCSV2(courseCSV.values, courseOfEntry):
            courseCSV.drop(courseCSV[courseCSV['course']
                                    == courseOfEntry].index, inplace=True)
            courseCSV.to_csv(courseFile, mode='w', index=False)
            studentsCSV = pd.read_csv(studentsFile)
            studentsCSV.drop(studentsCSV[studentsCSV['course']
                                        == courseOfEntry].index, inplace=True)
            studentsCSV.to_csv(studentsFile, mode='w', index=False)
    '''

    def notInCSV(self, newInfo, column, boolTableMode):
        newInfo = str(newInfo)
        self.currentCSV = self.studentsCSV if boolTableMode else self.courseCSV
        self.currentCSV[column] = self.currentCSV[column].astype(str)
        try:
            return len(self.currentCSV[self.currentCSV[column] == newInfo]) == 0
        except:
            print(f"column that pandas received: {column}")
            return True

    def editEntry(self, oldInfo, newInfo, column):
        # studentsCSV = pd.read_csv(studentsFile)
        # studentsCSV.loc[indexNum, column] = newInfo
        # studentsCSV.to_csv(studentsFile, mode='w', index=False)
        # oldInfo = str(oldInfo)
        # newInfo = str(newInfo)
        # print(f"sa gawas nga newInfo: {newInfo}, oldInfo: {oldInfo}")
        # if oldInfo == "nan": oldInfo = ""
        # if self.notInCSV(newInfo, column, 1):
        # print(f"newInfo: {newInfo}")
        self.studentsCSV[column] = self.studentsCSV[column].astype(str)
        self.studentsCSV.loc[self.studentsCSV[self.studentsCSV[column]
                                              == str(oldInfo)].index, column] = str(newInfo)
        print(self.studentsCSV)
        self.studentsCSV.to_csv(studentsFile, mode='w', index=False)
        print("csv modified by pandas")

    def editEntryCourse(self, idNumber, newCourse):
        self.studentsCSV["id"] = self.studentsCSV["id"].astype(str)
        self.studentsCSV.loc[self.studentsCSV[self.studentsCSV['id'] ==
                                              str(idNumber)].index, 'course'] = str(newCourse)
        self.studentsCSV.to_csv(studentsFile, index=False)
        print(
            f"studentsCSV.loc[studentsCSV[studentsCSV['id'] == idNumber].index, 'course']: {self.studentsCSV.loc[self.studentsCSV[self.studentsCSV['id']== idNumber].index, 'course']}")
        # studentsCSV.to_csv(studentsFile, mode='w', index=False)

    def editCourse(self, oldCourse, newCourse):
        print(f"oldCourse is {oldCourse}")
        self.courseCSV.loc[self.courseCSV['course'] == oldCourse] = newCourse
        self.courseCSV.to_csv(courseFile, mode='w', index=False)
        self.editEntry(oldCourse, newCourse, "course")

    def initStudent(self):
        self.studentsCSV = init_Student()

    def initCourse(self):
        self.courseCSV = init_Course()

    def initTables(self):
        self.initStudent()
        self.initCourse()


pd_obj = pandasway_object()


def studentInCSV(newEntry):
    return pd_obj.studentInCSV(newEntry)


def courseInCSV2(courses, newCourse):
    return pd_obj.courseInCSV2(courses, newCourse)


def courseInCSV(newCourse):
    return pd_obj.courseInCSV(newCourse)


def addEntry(row):
    pd_obj.addEntry(row)


def addCourse(courseName):
    return pd_obj.addCourse(courseName)


def deleteEntry(index):
    pd_obj.deleteEntry(index)


def deleteCourse(index):
    return pd_obj.deleteCourse(index)


def notInCSV(newInfo, column, boolTableMode):
    return pd_obj.notInCSV(newInfo, column, boolTableMode)


def editEntry(oldInfo, newInfo, column):
    pd_obj.editEntry(oldInfo, newInfo, column)


def editEntryCourse(idNumber, newCourse):
    pd_obj.editEntryCourse(idNumber, newCourse)


def editCourse(oldCourse, newCourse):
    pd_obj.editCourse(oldCourse, newCourse)


def initStudent():
    pd_obj.initStudent()


def initCourse():
    pd_obj.initCourse()


def initTables():
    initStudent()
    initCourse()


# if __name__ == '__main__':
'''
    courseCSV = pd.read_csv(courseFile)
    index = [1, 2, 3]
    print([courseCSV.values[i][0] for i in index])
    # editEntry(199, 291, 'id')
    # deleteEntry(1)
    # editEntryCourse(123, 'bs psych')
    # print(len(courseCSV.index))
    courseCSV = pd.read_csv(courseFile)
    print(courseCSV.values)
    '''
'''
    editCourse('bs ece', 'bs che')
    editEntry('elizer', 'herardo', 'name')
    deleteEntry('herardo')
    deleteCourse('bs it')
    '''
# deleteCourse('bs ca')
# editCourse('bs cs', 'bs comsci')
# print(studentsCSV.loc[4, 'course'])
# print(studentsCSV.loc[studentsCSV['id'] == 'c'].index)

'''
    addEntry(['e', 555, 'bsca'])
    addEntry(['f', 666, 'bsca'])
    '''
# addEntry(['G', 777, 'asd'])
# print(csvRead)
