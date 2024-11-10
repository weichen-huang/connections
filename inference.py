from solvers.ckmeans import ck_get_clusters
from utils import create_subsets
from tqdm import tqdm
from models.qwen import score


words = input("Enter comma separated words:").split(",")
slow = False
found = []

while len(found) != 4:
    pairs = create_subsets(words, n=4)
    quad = sorted([[score(pair, connector="and", permute=slow), pair] for pair in tqdm(pairs)])[0][1]
    tmp = []
    for word in words:
        if word not in quad:
            tmp.append(word)

    words = tmp
    found.append(set(quad))

print(found)

if __name__ == '__main__':
    pass

