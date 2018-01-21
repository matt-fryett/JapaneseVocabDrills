import sqlite3
import random

class db():
    def __init__(self,options):
        self.options = options
        self.conn = sqlite3.connect('japanese.db')
        self.cursor = self.conn.cursor()
        self.execptions = ["sentence_structures","verbs_general"]
        self.getTables()

    def getTables(self):
        self.cursor.execute("SELECT * FROM sqlite_sequence ORDER BY name")
        for row in self.cursor.fetchall():
            if row[0] not in self.execptions:
                self.options.categories.append(row[0])
                group = row[0].split("_")[0]
                subgroup = ["_".join(row[0].split("_")[1:])][0]
                if group not in self.options.groups:
                    self.options.groups.append(group)
                    self.options.subgroups[group] = ["<all>"]
                self.options.subgroups[group].append(subgroup)

    def getQuestion(self):
        kanji = None
        kana = None
        romaji = None
        english = None

        table = None
        if self.options.group == "<all>":
            table = random.choice(self.options.categories[1:])
        else:
            if self.options.subGroup == "<all>":
                table = self.options.group + "_" + random.choice(self.options.subgroups[self.options.group][1:])
            else:
                table = self.options.group + "_" + self.options.subGroup

        self.cursor.execute("SELECT * FROM "+table+" ORDER BY RANDOM() LIMIT 1;")
        row = self.cursor.fetchall()[0]
        print(row)

        id = row[0]
        kanji = row[1]
        kana = row[2]
        romaji = row[3]
        english = row[4]
        #+ (" " + table if self.options.group == "<all>" else "")
        if self.options.isKanji:
            return id,kanji,kana,english
        else:
            return id,kana,romaji,english

