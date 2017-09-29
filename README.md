# School Timetable Generator
This is a timetable generator that generates timetables randomly for all 8 sections of 12th grade in my school, everytime you run the program. It takes into account the following conditions:
1. All labs - physics, chemistry and electives - must be after recess because before recess labs may be occupied by juniors.
2. It must be ensured that every lab is occupied by one class only so every class must have unique periods chosen.
3. All corresponding sections e.g. 11 Sci D and 12 Sci D have the same electives.
4. Sections E & F both have computer science as their elective. Section G has elective Engineering Graphics.
5. For physics and chemistry I have chosen 4 teachers, each teacher teaching 2 classes.
6. One teacher teaches 11th and one 12th grade class with the same electives. E.g. If a teacher teaches 11 Sci D which has biology, it also teaches 12 Sci D which has biology.
7. If same teacher teaches one 11th grade and one 12th grade class, no class should clash for that teacher and hence periods should not coincide for the same subject.
8. For english and maths teachers are in excess as the same subjects are also in commerce. This is why I haven't taken into account the fact that classes may coincide for the same teacher.

## Requirements
python 2.7

## Contributing
To contribute to this repository, please read [CONTRIBUTING.md](https://github.com/utkarsh23/Graph-Plotter/blob/master/CONTRIBUTING.md)
