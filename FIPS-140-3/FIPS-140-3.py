import random
import math
import itertools
import time

class ShakPy():
    def __init__(self):
        self.options = {}

    def generate_random_sequence(self, length):
        print("generate...")
        time.sleep(0.5)
        return ''.join(random.choice('01') for _ in range(length))

    def monobit_test(self, sequence):
        time.sleep(0.5)
        print("monobit testing...")
        ones_count = sequence.count('1')
        result = 9654 < ones_count < 10346
        print(f"Тест {'пройдено' if result else 'не пройдено'}\ncount 9654<{result}<10346")
        return result

    def poker_test(self, sequence):
        time.sleep(0.5)
        print("poket testing...")
        subsequence_length = 4
        subsequence_count = len(sequence) // subsequence_length
        subsequence_frequencies = {}

        for i in range(subsequence_count):
            subsequence = sequence[i * subsequence_length: (i + 1) * subsequence_length]
            subsequence_frequencies[subsequence] = subsequence_frequencies.get(subsequence, 0) + 1

        sum_squared_frequencies = sum(freq ** 2 for freq in subsequence_frequencies.values())
        poker_chi_square = (16 / 5000) * sum_squared_frequencies - 5000
        result = 1.03 < poker_chi_square < 57.4
        print(f"Тест {'пройдено' if result else 'не пройдено'}\ncount 1.03<{result}<57.4")
        return result

    def runs_test(self, sequence):
        time.sleep(0.5)
        print("runs testing...")
        runs = [list(g) for k, g in itertools.groupby(sequence)]
        run_count = len(runs)
        pi = 1.0 / 2.0  # Очікувана ймовірність того, що біг буде '1'
        tau = 2.0 / 3.0  # Критичне значення для тесту бігів
        vobs = sum(len(run) for run in runs)
        vexp = 2.0 * len(sequence) / run_count
        runs_test_statistic = abs(vobs - vexp) / math.sqrt(2.0 * len(sequence) * (2.0 * len(sequence) - 1.0) / run_count)
        result = runs_test_statistic <= tau
        print(f"Тест {'пройдено' if result else 'не пройдено'}\ncount {runs_test_statistic}<={tau}")
        return result

    def long_run_test(self, sequence):
        time.sleep(0.5)
        print("long testing...")
        max_run_length = max(len(list(g)) for k, g in itertools.groupby(sequence))
        result = max_run_length <= 26
        print(f"Тест {'пройдено' if result else 'не пройдено'}\ncount {max_run_length} <= 26")
        return result

    def fips_140_test(self, sequence):
        print("starting")
        monobit_result = self.monobit_test(sequence)
        poker_result = self.poker_test(sequence)
        runs_result = self.runs_test(sequence)
        long_run_result = self.long_run_test(sequence)

        if monobit_result and poker_result and runs_result and long_run_result:
            print("Усі тести пройдено успішно!")
            return True
        else:
            print("Є проблеми у наступних тестах:")
            if not monobit_result:
                print("- Тест монобіта")
            if not poker_result:
                print("- Тест покера")
            if not runs_result:
                print("- Тест на послідовність бітів")
            if not long_run_result:
                print("- Тест на довгі біги")
            return False

    def random(self):
        while True:
            time.sleep(0.5)
            # Перетворення в рядок
            bit_sequence = self.generate_random_sequence(20000)
            print(bit_sequence)

            # Тестування
            result = self.fips_140_test(bit_sequence)
            if result:
                print("Послідовність проходить тест FIPS-140-3: вона є достатньою випадковою.")
                break
            else:
                print("Послідовність не проходить тест FIPS-140-3: вона не є достатньою випадковою.")

if __name__ == "__main__":
    shakpy = ShakPy()
    shakpy.random()
