# Mining Search Algorithm

This project is the result of Laboratory 1 of the AI Fundamentals course in the Master in Artificial Intelligence at the Universidade de Vigo. The goal is to apply and compare different search algorithms to solve a practical mining problem and analyze their behavior in terms of efficiency, cost, exploration, and path quality.

## Problem description

The task models a miner moving through a matrix whose cells have associated costs. The state includes:

- current row and column
- current direction of movement
- allowed actions: move forward, turn left, and turn right

The solution is built by expanding states and evaluating paths using classic search strategies, both uninformed and informed.

## Search algorithms implemented

This project compares the following algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search

The core search utilities were adapted and refactored from the classic AIMA search implementations used in artificial intelligence teaching.

## Project structure

- `search_minimal.py`: minimal implementation of the core search structures, including `Problem`, `Node`, `PriorityQueue`, BFS, DFS, and A*.
- `problem_solution.py`: concrete solution for the mining problem.
- `files/`: input maps used to test the search process.
- `LICENSE`: project license.

## Original repository used as reference

This project is based on and refactors components from the original aima-python repository:

https://github.com/aimacode/aima-python

In particular, the search logic in `search_minimal.py` is a reduced and adapted version of the classical AIMA search structures, including:

- `Problem`
- `Node`
- `PriorityQueue`
- BFS, DFS, and A*

This repository does not replace the original project; it reuses and adapts the relevant search logic for a specific educational use case in the context of the AI Fundamentals laboratory.

## Credits

- Original project: aima-python
- Original contributors: aima-python contributors
- Adaptation and refactoring: this project search_minimal class, for the AI Fundamentals laboratory of the Master in Artificial Intelligence at the Universidade de Vigo

## License

This project uses search logic inspired by aima-python, which is distributed under the MIT License. The MIT License allows reuse, modification, distribution, and adaptation of the software, provided that the original copyright notice and license are preserved.

The original license text is as follows:

The MIT License (MIT)

Copyright (c) 2016 aima-python contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This usage is therefore fully compatible with the MIT License and is credited appropriately.

## How to run

From the project directory, run:

```bash
python problem_solution.py
```

The program will ask for the path to the map file to solve, for example:

```bash
files/lab1-AIF-exampleMap.txt
```

---

This repository keeps attribution to the original project and complies with the MIT License that permits reuse and adaptation for educational purposes.
