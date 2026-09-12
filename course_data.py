from models import Course, Section


def get_forced_backtracking_dataset():
    return [
        Course("C1", "Internet Programming", 3, [
            Section("C1-B1", ("Mon","Wed",), 675, 750),
        ]),
        Course("C2", "Computer Architecture", 3, [
            Section("C1-B1", ("Tue","Thu",), 675, 750),
        ]),
        Course("C3", "Computer Architecture Lab", 1, [
            Section("C2-B1", ("Fri",), 610, 660),
            Section("C2-B2", ("Fri",), 675, 725),
            Section("C2-B3", ("Fri",), 740, 790),
        ]),
        Course("C4", "Software Development Process", 3, [
            Section("C1-B1", ("Tue","Thu",), 585, 660),
        ]),
        Course("C5", "Software Development Process Lab", 1, [
            Section("C1-B1", ("Fri",), 610, 660),
            Section("C1-B2", ("Fri",), 675, 735),
            Section("C1-B3", ("Fri",), 750, 800),
            Section("C1-B4", ("Fri",), 815, 865),

        ]),
        Course("C6", "Introduction to Artificial Intelligence", 3, [
            Section("C1-B1", ("Mon","Wed",), 780, 855),
            Section("C1-B2", ("Mon","Wed",), 960, 1035),
        ]),
        Course("C7", "Introduction to Artificial Intelligence Lab", 1, [
            Section("C1-B1", ("Fri",), 675, 725),
            Section("C1-B2", ("Fri",), 740, 790),
            Section("C1-B3", ("Fri",), 805, 855),
            Section("C1-B4", ("Fri",), 870, 920),
        ]),
        Course("C8", "Human Biology", 3, [
            Section("C1-B1", ("Mon","Wed","Fri"), 740, 790),
            Section("C1-B2", ("Mon","Wed","Fri"), 805, 855),
        ]),
        Course("C9", "Human Biology Lab", 1, [
            Section("C1-B1", ("Thu"), 740, 855),
            Section("C1-B2", ("Thu"), 870, 985),
            Section("C1-B3", ("Thu"), 1000, 1115),
            Section("C1-B4", ("Wed"), 480, 595),
            Section("C1-B5", ("Wed"), 610, 725),
            Section("C1-B6", ("Wed"), 870, 985),
            Section("C1-B7", ("Wed"), 1000, 1115),
        ]),
        Course("C10", "Automata Theory", 3, [
            Section("C1-B1", ("Tue","Thu",), 495, 570),
        ]),
        Course("C11", "Automata Theory Discussion", 1, [
            Section("C2-B1", ("Fri",), 740, 790),
            Section("C2-B2", ("Fri",), 805, 855),
            Section("C2-B3", ("Fri",), 870, 920),
        ]),
        Course("C12", "User Interface Design and Prototyping", 3, [
            Section("C1-B1", ("Mon","Wed",), 585, 660),
        ]),
        Course("C13", "User Interface Design and Prototyping Discussion", 1, [
            Section("C2-B1", ("Thu",), 545, 595),
            Section("C2-B2", ("Thu",), 610, 660),
            Section("C2-B3", ("Thu",), 675, 725),
        ]),
    ]

def get_small_dataset():
    return [
        Course("C1", "Course1", 3, [
            Section("C1-S1", ("Mon", "Wed"), 540, 615),
            Section("C1-S2", ("Tue", "Thu"), 630, 705),
        ]),
        Course("C2", "Course2", 4, [
            Section("C2-S1", ("Mon", "Wed"), 630, 705),
            Section("C2-S2", ("Tue", "Thu"), 540, 615),
        ]),
        Course("C3", "Course3", 3, [
            Section("C3-S1", ("Mon", "Wed"), 750, 825),
            Section("C3-S2", ("Tue", "Thu"), 750, 825),
        ]),
        Course("C4", "Course4", 3, [
            Section("C4-S1", ("Mon", "Wed"), 870, 945),
            Section("C4-S2", ("Tue", "Thu"), 870, 945),
        ]),
        Course("C5", "Course5", 4, [
            Section("C5-S1", ("Tue", "Thu"), 960, 1035),
            Section("C5-S2", ("Mon", "Wed"), 960, 1035),
        ]),
        Course("C6", "Course6", 3, [
            Section("C6-S1", ("Mon", "Wed", "Fri"), 630, 680),
            Section("C6-S2", ("Tue", "Thu"), 1020, 1095),
        ]),
    ]


def get_medium_dataset():
    return [
        Course("C1", "Course1", 3, [
            Section("C1-S1", ("Mon", "Wed"), 540, 615),
            Section("C1-S2", ("Mon", "Wed"), 870, 945),
        ]),
        Course("C2", "Course2", 3, [
            Section("C2-S1", ("Mon", "Wed"), 540, 615),
            Section("C2-S2", ("Tue", "Thu"), 870, 945),
        ]),
        Course("C3", "Course3", 3, [
            Section("C3-S1", ("Mon", "Wed"), 540, 615),
        ]),
        Course("C4", "Course4", 3, [
            Section("C4-S1", ("Mon", "Wed"), 630, 705),
            Section("C4-S2", ("Fri",), 540, 615),
        ]),
        Course("C5", "Course5", 3, [
            Section("C5-S1", ("Mon", "Wed"), 630, 705),
            Section("C5-S2", ("Fri",), 630, 705),
        ]),
        Course("C6", "Course6", 3, [
            Section("C6-S1", ("Mon", "Wed"), 630, 705),
        ]),
        Course("C7", "Course7", 3, [
            Section("C7-S1", ("Tue", "Thu"), 540, 615),
            Section("C7-S2", ("Fri",), 750, 825),
        ]),
        Course("C8", "Course8", 3, [
            Section("C8-S1", ("Tue", "Thu"), 540, 615),
            Section("C8-S2", ("Mon", "Wed"), 750, 825),
        ]),
        Course("C9", "Course9", 3, [
            Section("C9-S1", ("Tue", "Thu"), 540, 615),
        ]),
        Course("C10", "Course10", 3, [
            Section("C10-S1", ("Tue", "Thu"), 630, 705),
            Section("C10-S2", ("Fri",), 870, 945),
        ]),
        Course("C11", "Course11", 3, [
            Section("C11-S1", ("Tue", "Thu"), 630, 705),
            Section("C11-S2", ("Fri",), 960, 1035),
        ]),
        Course("C12", "Course12", 3, [
            Section("C12-S1", ("Tue", "Thu"), 630, 705),
        ]),
        Course("C13", "Course13", 3, [
            Section("C13-S1", ("Tue", "Thu"), 750, 825),
            Section("C13-S2", ("Mon", "Wed"), 540, 615),
        ]),
        Course("C14", "Course14", 3, [
            Section("C14-S1", ("Mon", "Wed"), 960, 1035),
            Section("C14-S2", ("Tue", "Thu"), 540, 615),
        ]),
        Course("C15", "Course15", 3, [
            Section("C15-S1", ("Tue", "Thu"), 960, 1035),
            Section("C15-S2", ("Mon", "Wed"), 630, 705),
        ]),
    ]


def get_large_dataset():
    return [
        Course("C1", "Course1", 3, [
            Section("C1-S1", ("Mon", "Wed"), 540, 615),
            Section("C1-S2", ("Tue", "Thu"), 540, 615),
            Section("C1-S3", ("Mon", "Wed"), 480, 540),
        ]),
        Course("C2", "Course2", 3, [
            Section("C2-S1", ("Mon", "Wed"), 540, 615),
            Section("C2-S2", ("Tue", "Thu"), 630, 705),
            Section("C2-S3", ("Tue", "Thu"), 480, 540),
        ]),
        Course("C3", "Course3", 3, [
            Section("C3-S1", ("Mon", "Wed"), 540, 615),
            Section("C3-S2", ("Mon", "Wed"), 630, 705),
            Section("C3-S3", ("Fri",), 480, 540),
        ]),
        Course("C4", "Course4", 3, [
            Section("C4-S1", ("Mon", "Wed"), 540, 615),
            Section("C4-S2", ("Tue", "Thu"), 540, 615),
            Section("C4-S3", ("Fri",), 600, 660),
        ]),
        Course("C5", "Course5", 3, [
            Section("C5-S1", ("Mon", "Wed"), 540, 615),
        ]),
        Course("C6", "Course6", 3, [
            Section("C6-S1", ("Mon", "Wed"), 630, 705),
            Section("C6-S2", ("Tue", "Thu"), 540, 615),
            Section("C6-S3", ("Mon", "Wed"), 750, 825),
        ]),
        Course("C7", "Course7", 3, [
            Section("C7-S1", ("Mon", "Wed"), 630, 705),
            Section("C7-S2", ("Tue", "Thu"), 630, 705),
            Section("C7-S3", ("Tue", "Thu"), 750, 825),
        ]),
        Course("C8", "Course8", 3, [
            Section("C8-S1", ("Mon", "Wed"), 630, 705),
            Section("C8-S2", ("Mon", "Wed"), 540, 615),
            Section("C8-S3", ("Fri",), 720, 780),
        ]),
        Course("C9", "Course9", 3, [
            Section("C9-S1", ("Mon", "Wed"), 630, 705),
            Section("C9-S2", ("Tue", "Thu"), 540, 615),
            Section("C9-S3", ("Fri",), 840, 900),
        ]),
        Course("C10", "Course10", 3, [
            Section("C10-S1", ("Mon", "Wed"), 630, 705),
        ]),
        Course("C11", "Course11", 3, [
            Section("C11-S1", ("Tue", "Thu"), 540, 615),
            Section("C11-S2", ("Mon", "Wed"), 540, 615),
            Section("C11-S3", ("Mon", "Wed"), 870, 945),
        ]),
        Course("C12", "Course12", 3, [
            Section("C12-S1", ("Tue", "Thu"), 540, 615),
            Section("C12-S2", ("Mon", "Wed"), 630, 705),
            Section("C12-S3", ("Tue", "Thu"), 870, 945),
        ]),
        Course("C13", "Course13", 3, [
            Section("C13-S1", ("Tue", "Thu"), 540, 615),
            Section("C13-S2", ("Tue", "Thu"), 630, 705),
            Section("C13-S3", ("Fri",), 960, 1020),
        ]),
        Course("C14", "Course14", 3, [
            Section("C14-S1", ("Tue", "Thu"), 540, 615),
            Section("C14-S2", ("Mon", "Wed"), 540, 615),
            Section("C14-S3", ("Fri",), 1080, 1140),
        ]),
        Course("C15", "Course15", 3, [
            Section("C15-S1", ("Tue", "Thu"), 540, 615),
        ]),
        Course("C16", "Course16", 3, [
            Section("C16-S1", ("Tue", "Thu"), 630, 705),
            Section("C16-S2", ("Mon", "Wed"), 630, 705),
            Section("C16-S3", ("Mon", "Wed"), 960, 1035),
        ]),
        Course("C17", "Course17", 3, [
            Section("C17-S1", ("Tue", "Thu"), 630, 705),
            Section("C17-S2", ("Tue", "Thu"), 540, 615),
            Section("C17-S3", ("Tue", "Thu"), 960, 1035),
        ]),
        Course("C18", "Course18", 3, [
            Section("C18-S1", ("Tue", "Thu"), 630, 705),
            Section("C18-S2", ("Mon", "Wed"), 540, 615),
            Section("C18-S3", ("Mon", "Wed"), 1080, 1140),
        ]),
        Course("C19", "Course19", 3, [
            Section("C19-S1", ("Tue", "Thu"), 630, 705),
            Section("C19-S2", ("Mon", "Wed"), 630, 705),
            Section("C19-S3", ("Tue", "Thu"), 1080, 1140),
        ]),
        Course("C20", "Course20", 3, [
            Section("C20-S1", ("Tue", "Thu"), 630, 705),
        ]),
    ]