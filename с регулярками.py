import re
class Timetable:
    def __init__(self, subjects):
        self.subjects = subjects
class Objects:
    def __init__(self):
        self.day = None
        self.time = None
        self.room = None
        self.place = None
        self.lesson = None
        self.teacher = None
        self.lessonformat = None
class Pars:
    def parser(self, line, subject):
        line = re.sub(r"\t", "", str(line))
        nline = re.split(r":", line)
        key = nline[0]
        mean = re.sub(r"\n", "", nline[1])
        if key == "day":
            subject.day = mean
        elif key == "time":
            subject.time = re.sub(r"\n", "", nline[1]) + ":" + re.sub(r"\n", "", nline[2]) + ":" + re.sub(r"\n", "", nline[3])
        elif key == "room":
            subject.room = mean
        elif key == "place":
            subject.place = mean
        elif key == "lesson":
            subject.lesson = mean
        elif key == "teacher":
            subject.teacher = mean
        elif key == "lessonformat":
            subject.lessonformat = mean
        return subject
    def filerun(self, file):
        lines = file.readlines()
        subjects = [Objects(), Objects()]
        i = -1
        for line in lines:
            line = re.sub(r"\n", "", line)
            line = re.sub(r"\s\s", "", line)
            if re.fullmatch(r"\s*subject\d:", line) is not None:
                i += 1
            elif re.fullmatch(r"timetable:", line) is None:
                subjects[i] = self.parser(line, subjects[i])
        resubjects = Timetable(subjects)
        return resubjects

file = open("среда.yaml", "r", encoding="utf-8")
filex = open("среда.xml", "w", encoding="utf-8")
parser = Pars()
resubjects = parser.filerun(file)
result = "<timetable>\n"
for i in range(len(resubjects.subjects)):
    result += "\t<subject{}>\n".format(i+1)
    new_dict = resubjects.subjects[i].__dict__
    for tag in new_dict:
        result += "\t\t<{}>{}</{}>\n".format(tag, new_dict[tag], tag)
    result += "\t</subject{}>\n".format(i+1)
result += "</timetable>"
filex.write(result)






























