
class Label:

    def __init__(self, obj):

        self.obj = obj

        self.max_frequency_elem = 0
        self.max_linkage_elem = 0
        self.length = 0

        self.frequency_vec = []
        self.linkage = []

    def update_frequency_vectors(self):
        self.frequency_vec.append(0)
        self.linkage.append(0)
        self.length += 1

    def update_max_frequency(self):

        max_f = max_l = pos_l = pos_f = 0

        for i in range(self.length):
            if max_f < self.frequency_vec[i]:
                max_f = self.frequency_vec[i]
                pos_f = i

            if max_l < self.linkage[i]:
                max_l = self.linkage[i]
                pos_l = i

        self.max_frequency_elem = pos_f
        self.max_linkage_elem = pos_l

    def update_frequency(self, obj):

        self.frequency_vec[obj] += 1

    def update_linkage(self, obj):

        self.linkage[obj] += 1

    def get_f_replacer(self):

        return self.max_frequency_elem

    def get_l_replacer(self):

        return self.max_linkage_elem


class FrequencyStructure:

    def __init__(self):

        self.alphabet_trans = {}
        self.current_char = 0

        self.frequency_table = []

    def update_alphabet(self, letter):

        self.alphabet_trans[letter] = self.current_char

        label = Label(letter)
        self.frequency_table.append(label)

        for element in self.frequency_table:
            element.update_frequency_vectors()

        self.current_char += 1

    def text_reader(self, text):

        text = list(text)

        for letter in text:
            if self.alphabet_trans[letter] is None:
                self.update_alphabet(letter)

structure = FrequencyStructure()

