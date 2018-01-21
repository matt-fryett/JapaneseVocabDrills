class options():
    def __init__(self):
        self.jfbpLevels = [str(x) for x in range(1,30)]
        self.categories = []
        self.groups = ["<all>"]
        self.subgroups = {}
        self.kana = ["kana","kanji"]

        self.group = None
        self.subgroup = None
        self.isKanji = False