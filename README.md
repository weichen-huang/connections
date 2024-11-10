# connections

## NYT Connections solver with small LMs

### Uses:

- [This repo](https://github.com/Eyefyre/NYT-Connections-Answers) to get the latest puzzles
- [Qwen2-0.5B](https://huggingface.co/Qwen/Qwen2-0.5B) to generate correlation scores

### How it works: (TODO)

### Repo description:

```markdown
cluster_solve.py - Solver using constrained k-means
iteration_solve.py - Solver which iterates through groups of 4 words
inference.py - Iteration solver but with your own input words
```

### Todo:

- Add algorithm description
- Implement feedback handler