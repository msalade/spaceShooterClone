import json
from os import path

score_folder = path.join(path.dirname(__file__), '..', 'assets/score')


class ScoreService:
    def save_best_result(self, score):
        if int(score) != 0:
            result = self.get_best_results()
            if result is not None and int(result) < score:
                with open(path.join(score_folder, 'score.txt'), 'w') as outfile:
                    to_save = {'score': score}
                    json.dump(to_save, outfile)


    def get_best_results(self):
        with open(path.join(score_folder, 'score.txt')) as json_file:
            scores = json.load(json_file)['score']
        if scores is not None:
            return scores
        else:
            return '-'
