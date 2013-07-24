import sys
import math
import string 

def read_file(filename):
    d = {}
    for l in open(filename):
        l = l.translate(string.maketrans("", ""), string.punctuation) # remove punctation
        for w in l.lower().rsplit():
            d[w] = d.get(w, 0) + 1
    return d

doc_A = sys.argv[1]
doc_B = sys.argv[2]

da = read_file(doc_A)
db = read_file(doc_B)
print len(da), 'words in ', doc_A
print len(db), 'words in ', doc_B


def inner_product(da, db):
    words_list = list(set(da.keys() + db.keys()))
    return sum([da.get(w, 0) * db.get(w, 0)
                for w in words_list])


def vector_angle(da, db):
    n = inner_product(da, db)
    d = math.sqrt(inner_product(da, da )* inner_product(db, db))
    return math.acos(n / d)

print 'Inner product ', inner_product(da, db)
print 'Vector angle', vector_angle(da, db)