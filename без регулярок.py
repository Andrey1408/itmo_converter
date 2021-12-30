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
        line = str(line).replace("  ", "")
        nline = line.split(":")
        key = nline[0]
        mean = nline[1].replace("\n", "")
        if key == "day":
            subject.day = mean
        elif key == "time":
            subject.time = nline[1].replace("\n", "") + ":" + nline[2].replace("\n", "") + ":" + nline[3].replace("\n", "")
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
            line = line.replace("\n", "")
            line = line.replace("  ", "")
            if line.count("subject") != 0:
                i += 1
            elif line.count("timetable") == 0:
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





























