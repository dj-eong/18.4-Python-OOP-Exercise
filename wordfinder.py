from random import choice


class WordFinder:
    """WordFinder: finds random words from a dictionary.

    >>> wf = WordFinder('wordz.txt')
    1 words read

    >>> wf.random()
    'cat'

    >>> wf.random() in wf.lst
    True

    >>> print(wf.lst)
    ['cat']
    """

    def __init__(self, path):
        self.path = path
        self.lst = self.read_file(path)
        print(f'{len(self.lst)} words read')

    def __repr__(self):
        return f'<WordFinder path={self.path}>'

    def read_file(self, path):
        file = open(path)

        lst = []
        for word in file:
            word = word.strip()
            lst.append(word)
        return lst

    def random(self):
        return choice(self.lst)


class SpecialWordFinder(WordFinder):
    """WordFinder for special files

    >>> swf = SpecialWordFinder('food.txt')
    4 words read

    >>> print(swf.lst)
    ['kale', 'parsnips', 'apple', 'mango']

    >>> swf.random() in swf.lst
    True
    """

    def read_file(self, path):
        lst = super().read_file(path)
        return [word for word in lst if word and not word.startswith('#')]
