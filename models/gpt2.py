import itertools

from transformer_lens import HookedTransformer
import torch

torch.set_grad_enabled(False)
device = torch.device("cpu")

if torch.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")

model = HookedTransformer.from_pretrained("Qwen/Qwen2-0.5B", device=device)

def score(arr, connector="and", permute=True):

    sc = 1e9

    if not permute:
        return model(f" {connector} ".join(arr), return_type="loss").item()

    for perm in itertools.permutations(arr):
        text = f" {connector} ".join(perm)
        sc = min(sc, model(text, return_type="loss").item())

    return sc