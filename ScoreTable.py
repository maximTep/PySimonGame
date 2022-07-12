from PGSettings import *

f = open('log.txt', 'a')

class ScoreTable:
    def __init__(self):
        f.write(str(datetime.datetime.now())[0:19] + '\n   ')
        self.results = []
        self.count = 0

    def add_note(self, score, lvl_num, user_seq, right_seq):
        self.add_result(score)
        f.write('Lvl ' + str(lvl_num) + '\n   ')
        f.write('Right Seqeuence:  ' + str(right_seq) + '\n   ')
        f.write('User Seqeuence:  ' + str(user_seq))

    def add_result(self, score):
        self.results.append(score)
        self.count += 1
        if self.count > 12:
            self.results.pop(0)

    def show(self):
        LabelText = lobster.render('Last tries:', True, BLACK)
        screen.blit(LabelText, [50, 200])
        cnt = 1
        for res in reversed(self.results):
            text = lobster.render(str(res), True, BLACK)
            screen.blit(text, [75, 210 + 35 * cnt])
            cnt += 1
