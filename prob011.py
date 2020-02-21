'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''
all = ['dog', 'deer', 'deal', 'yay']
all_dict = {1: [x[:1] for x in all], 2: [x[:2] for x in all]}


def get_matches(s):
	return [x for x in all if s == x[:len(s)]]


def get_matches2(s):
	return [all[i] for i, x in enumerate(all_dict[len(s)]) if s == x]


# print(get_matches2('de'))

ENDS_HERE = '__ENDS_HERE'

words = ['foo', 'bar', ...]


class Trie(object):
	def __init__(self):
		self._trie = {}

	def insert(self, text):
		trie = self._trie
		for char in text:
			if char not in trie:
				trie[char] = {}
			trie = trie[char]
		trie[ENDS_HERE] = True

	def elements(self, prefix):
		d = self._trie
		for char in prefix:
			if char in d:
				d = d[char]
			else:
				return []
		return self._elements(d)

	def _elements(self, d):
		result = []
		for c, v in d.items():
			if c == ENDS_HERE:
				subresult = ['']
			else:
				subresult = [c + s for s in self._elements(v)]
			result.extend(subresult)
		return result


trie = Trie()
for word in words:
	trie.insert(word)


def autocomplete(s):
	# s is a prefix
	suffixes = trie.elements(s)
	return [s + w for w in suffixes]

