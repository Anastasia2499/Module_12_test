import unittest
from Module_12 import runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = runner.Runner('Усэйн', 10)
        self.runner2 = runner.Runner('Андрей', 9)
        self.runner3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'{test_key} : {test_value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1_run(self):
        tourney = runner.Tournament(90, self.runner1, self.runner3)
        result = tourney.start()
        self.assertTrue((result[list(result.keys())[-1]]) == 'Ник')
        self.all_results = result
        print(self.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2_run(self):
        tourney = runner.Tournament(90, self.runner2, self.runner3)
        result = tourney.start()
        self.assertTrue((result[list(result.keys())[-1]]) == 'Ник')
        self.all_results = result
        print(self.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3_run(self):
        tourney = runner.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tourney.start()
        self.assertTrue((result[list(result.keys())[-1]]) == 'Ник')
        self.all_results = result
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()
