# PugetBench-minGPT

A simple GPU performance benchmark using Andrej Karpathy's minGPT code.

The executable is a small standalone Python executable built with PyInstaller. (no python install is needed). Micromamba is used to create an env with,

- Python
- PyTorch
- CUDA
- Huggingface transformers
- huggingface_hub

The pugetbench-mingpt.py does,

- Print some kind of message about usage and such
- Run micromamba to create the env needed to run minGPT
- Do a specified number of iterations for a training run on a GPT-2 124 Mil parameter model using tiny-shakespear (1.1MB of data)
- The benchmark is chargpt from the projects in minGPT it trains a character-level language model.
- The benchmark performance measure is the time needed to run 1000 training iterations. (This is a hardware benchmark, not a software benchmark)
- The number of iterations, and batch size can be adjusted to accommodate different NVIDIA GPUs. Number of iterations should be fixed for a given hardware comparison, but the batch size can be adjusted to allow for different amounts of GPU memory. (Performance will be biased toward lager mem GPUs -- just like the real world)
