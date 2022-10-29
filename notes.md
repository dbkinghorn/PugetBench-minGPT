## Notes for PyTorch Transformer Benchmark

Goal is to

- make a local env for pytorch using micromamba
- run a Transform benchmark in that
- do this stand alone
- use pyinstaller to make a minimal exe that will build the env and run the benchmark

### local env with mm

micromamba download to PWD/mm

## Example to use! Karpathy's minGPT

The is a nice project
https://github.com/karpathy/minGPT

I can use the character level language model code chargpt.py

- clone the project dir
- cp projects/chargpt.py to base dir
- get the tiny-shakespear (1.1MB data set) as input.txt
  https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

- in the pytorch env do

```
time python ./chargpt.py --trainer.max_iters=1000 --model.model_type='gpt2' --trainer.batch_size=32
```

- control the run time with max_iters and memory used with batch_size
- clean up rm -rt ./out that has the check point file and current model optimized parameters from training run

## Setup run env with micromamba

```
mm/micromamba create -p mm/envs/pytorch -r mm -c pytorch -c conda-forge -c huggingface pytorch cudatoolkit=11.6 huggingface_hub transformers
```

That did the right thing. The configured python is in

```
./mm/envs/pytorch/bin/python
```

## Test running minGPT benchmark from mm pytorch env

```
time ../mm/envs/pytorch/bin/python ./chargpt.py --trainer.max_iters=1000 --model.model_type='gpt2' --trainer.batch_size=32
```

Works! Here's output on my Titan V

nvidia-smi out during run (8.6GB GPU mem and 100% load)

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.76       Driver Version: 515.76       CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA TITAN V      Off  | 00000000:65:00.0  On |                  N/A |
| 54%   77C    P2   198W / 250W |   8661MiB / 12288MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```

Job output

```
iter_dt 292.46ms; iter 950: train loss 1.64734
iter_dt 289.24ms; iter 960: train loss 1.58010
iter_dt 290.51ms; iter 970: train loss 1.61886
iter_dt 292.74ms; iter 980: train loss 1.63811
iter_dt 292.88ms; iter 990: train loss 1.64176

real	5m0.273s
user	5m15.993s
sys	0m2.465s

```

## Data Parallel

switched to DP modifications made by
Gavia Gray https://github.com/gngdb/minGPT/tree/dataparallel
