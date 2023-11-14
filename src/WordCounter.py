class WordCounter:
        def __init__(self, sentence: str):
            self.sentence = sentence
            self.count = 0
            self.shortest = float('inf')
            self.longest = 0
        def count_words(self):
            for i in self.sentence.split(" "):
                self.count += 1
                curr_count = len(i)
                if curr_count > self.longest: self.longest = curr_count
                if curr_count < self.shortest: self.shortest = curr_count
        def get_word_count(self):
            return self.count
        def get_shortest_word(self):
            return self.shortest
        def get_longest_word(self):
            return self.longest