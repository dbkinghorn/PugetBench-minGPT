# PugetBench-minGPT

### Version 0.1.0

**A simple GPU performance benchmark using Andrej Karpathy's minGPT code. The performance measure is wall-time for a given number of iterations (1000) of training GPT-2 with a give batch_size (32) using "tiny Shakespeare.**
https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

The project is based on the code,

- https://github.com/karpathy/minGPT

With dataparallel modifications made by

- Gavia Gray https://github.com/gngdb/minGPT/tree/dataparallel

The benchmark code is from the character level language model project chargpt.py

The benchmark exe is a small standalone Python executable built with PyInstaller. (no python install is needed). Micromamba is used by this code to create an env with,

- Python
- PyTorch
- CUDA
- Huggingface transformers
- huggingface_hub

Running pugetbench-mingpt does the following;

- Run micromamba to create the env needed to run minGPT (**could take several minutes**)
  - On first run the packages needed for the env will be downloaded into the benchmark directory. mm/pkgs approx. 3GB download
  - The env will be created in the mm/envs full env setup is approx. 8.5GB
- Then runs the benchmark using the created env (**could take several minutes**)

The benchmark will run on multi-GPU (NVIDIA GPUs) however, there is enough communication with the current data-parallel implementation that the scaling will be poor. It's best used as a single GPU benchmark.

### `./pugetbench-mingpt --help`

```
usage: pugetbench-mingpt [-h] [-i ITERATIONS] [-b BATCHSIZE] [-p | --parallel | --no-parallel] [-y | --yes | --no-yes]

pugetbench-mingpt.py is the setup-and-run user interface for a simple GPU performance benchmark using Andrej Karpathy's minGPT code.

options:
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS
                        Number of iterations to run the benchmark
  -b BATCHSIZE, --batchsize BATCHSIZE
                        Batch size to use for the benchmark
  -p, --parallel, --no-parallel
                        -p | --parallel | --no-parallel Run the benchmark in parallel on multiple GPUs, use CUDA_VISIBLE_DEVICES to control
                        which GPUs are used (default: True)
  -y, --yes, --no-yes   -y | --yes Skip the confirmation prompt (default: False)
```

### Note:

The tar.gz or zip file in Releases will decompress to a directory that contains the `pugetbench-mingpt` or `pugetbench-mingpt.exe` executable along with all other assets needed to run. **The env for the job run (8.5GB) will be created locally in this same directory on first run. Nothing is installed outside of this directory.** To remove just delete the directory.

**On Windows:** The .exe will open and execute in CMD when double clicked, however you would not be able to change any options before start. **It is recommended to use PowerShell to run the benchmark.**
