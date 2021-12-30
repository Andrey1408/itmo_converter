import time
import re
import xmlplain
start = time.time()
loops = 10
for i in range(0, loops):
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
                subject.time = nline[1].replace("\n", "") + ":" + nline[2].replace("\n", "") + ":" + nline[3].replace(
                    "\n", "")
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
        result += "\t<subject{}>\n".format(i + 1)
        new_dict = resubjects.subjects[i].__dict__
        for tag in new_dict:
            result += "\t\t<{}>{}</{}>\n".format(tag, new_dict[tag], tag)
        result += "\t</subject{}>\n".format(i + 1)
    result += "</timetable>"
    filex.write(result)

print("Без использования регулярных выражений и библиотек: ", time.time()-start)
for i in range(0, loops):
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
            line = re.sub("\t", "", str(line))
            nline = re.split(":", line)
            key = nline[0]
            mean = re.sub("\n", "", nline[1])
            if key == "day":
                subject.day = mean
            elif key == "time":
                subject.time = re.sub("\n", "", nline[1]) + ":" + re.sub("\n", "", nline[2]) + ":" + re.sub("\n", "",nline[3])

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
                if re.fullmatch("\s*subject\d:", line) is not None:
                    i += 1
                elif re.fullmatch("timetable:", line) is None:
                    subjects[i] = self.parser(line, subjects[i])
            resubjects = Timetable(subjects)
            return resubjects


    file = open("среда.yaml", "r", encoding="utf-8")
    filex = open("среда.xml", "w", encoding="utf-8")
    parser = Pars()
    resubjects = parser.filerun(file)
    result = "<timetable>\n"
    for i in range(len(resubjects.subjects)):
        result += "\t<subject{}>\n".format(i + 1)
        new_dict = resubjects.subjects[i].__dict__
        for tag in new_dict:
            result += "\t\t<{}>{}</{}>\n".format(tag, new_dict[tag], tag)
        result += "\t</subject{}>\n".format(i + 1)
    result += "</timetable>"
    filex.write(result)
print("С регулярными выражениями: ", time.time()-start)

for i in range(0, loops):
    with open("среда.yaml") as inf:
        root = xmlplain.obj_from_yaml(inf)

    with open("среда.xml", "w") as outf:
        xmlplain.xml_from_obj(root, outf, pretty=True)
print("C использованием библиотеки: ", time.time()-start)