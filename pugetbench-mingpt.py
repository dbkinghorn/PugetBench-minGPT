#!/usr/bin/env python

"""
pugetbench-mingpt.py is the setup user interface for a  simple GPU performance benchmark using Andrej Karpathy's minGPT code.
It will,
- Print some kind of message about usage and such
- Run micromamba to create the env needed to run minGPT
- Do a specified number of iterations for a training run on a GPT-2 124 Mil parameter model using tiny-shakespear (1.1MB of data)
- The benchmark is chargpt from the projects in minGPT it trains a character-level language model.
- The benchmark performance measure is the time needed to run 1000 training iterations. (This is a hardware benchmark, not a software benchmark)
- The number of iterations, and batch size can be adjusted to accommodate different NVIDIA GPUs. Number of iterations should be fixed for a given hardware comparison, but the batch size can be adjusted to allow for different amounts of GPU memory. (Performance will be biased toward lager mem GPUs -- just like the real world)
"""

import os
import sys
import subprocess
from pathlib import Path
import platform
from datetime import datetime
import argparse
import time


# ******************************************************************************
# Initialize the runtime constants
# ******************************************************************************
os_in_use = platform.system()

MAMBA_DIR = Path("mm")  # micromamba install directory
MAMBA_EXE = MAMBA_DIR / f'{"micromamba" if os_in_use == "Linux" else "micromamba.exe"}'
MAMBA_ENVS = MAMBA_DIR / "envs"
BENCH_PATH = Path.cwd() / "chargpt.py"
ENV_NAME = "pytorch"

if os_in_use == "Windows":
    PY_PATH = f"""{MAMBA_ENVS / ENV_NAME / 'python'}"""
else:
    PY_PATH = f"""{MAMBA_ENVS / ENV_NAME / 'bin' / 'python'}"""


sys_env = os.environ.copy()

# ******************************************************************************
# Utility functions
# ******************************************************************************
def set_py_environment(py_env_dir):
    """A hack to workaround lame windows conda setup
    The main run_cmd function has this as an optional arg with default None"""
    if os_in_use == "Windows":
        sys_env = os.environ.copy()
        sys_env["PATH"] = str(py_env_dir) + "\\Library\\bin" + ";" + sys_env["PATH"]
        sys_env["PATH"] = (
            str(py_env_dir) + "\\Library\\usr\\bin" + ";" + sys_env["PATH"]
        )
        sys_env["PATH"] = (
            str(py_env_dir) + "\\Library\\mingw-w64\\bin" + ";" + sys_env["PATH"]
        )
        sys_env["PATH"] = str(py_env_dir) + "\\Scripts" + ";" + sys_env["PATH"]
        sys_env["PATH"] = str(py_env_dir) + ";" + sys_env["PATH"]
    else:
        sys_env = os.environ.copy()
    return sys_env


def run_cmd(cmd, sys_env=None):
    """Run command cmd in a subprocess with output polling
    capturing stdout and stderr without waiting for the output buffer to flush
    so the user knows something is happening for longer running commands"""

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=sys_env
    )

    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            print(output.strip())
    return process.poll()


mamba_cmd = f"""{MAMBA_EXE } 
                create -p {ENV_NAME} 
                -r {MAMBA_DIR} --yes -c pytorch -c conda-forge -c huggingface pytorch cudatoolkit=11.6 huggingface_hub transformers """


def mk_bench_env(env_name=ENV_NAME, env_cmd=mamba_cmd):
    """Create the benchmark python env using micromamba"""
    bench_env = MAMBA_ENVS / env_name
    if not bench_env.exists():
        run_cmd(env_cmd.split(), sys_env)


# def run_benchmark(env_name, job_args, sys_env):
#     """Make the commandline args for running the benchmark jobs with the
#     correct API's python env. This is passed to subprocess.run via run_cmd()"""
#     if os_in_use == "Windows":  # Windows doesn't use a /bin
#         # spliting the arg string fails on Win even with relative paths!?
#         # benchmark_cmd = f"""{MAMBA_ENVS / env_name / 'python'} {JOB_RUNNER} {job_args} { jobs} """
#         benchmark_cmd = [MAMBA_ENVS / env_name / "python", JOB_RUNNER]
#         benchmark_cmd.extend(job_args.split())
#         # benchmark_cmd.split()
#     else:
#         benchmark_cmd = (
#             f"""{MAMBA_ENVS / env_name / 'bin' / 'python'} {JOB_RUNNER} {job_args}  """
#         )
#         benchmark_cmd.split()
#     run_cmd(benchmark_cmd, sys_env)


def run_chargpt(iterations, batchsize, sys_env):
    CHARGPT_CMD = f"""{BENCH_PATH} --trainer.max_iters={iterations} --model.model_type='gpt2' --trainer.batch_size={batchsize} """
    commandline = f"""{PY_PATH} -u {CHARGPT_CMD}"""
    print(f"Running {commandline}")
    starttime = time.time()
    run_cmd(commandline.split(), sys_env)
    endtime = time.time()
    print("****************************************************************")
    print(
        f"* Time = {endtime-starttime:.2f} seconds for {iterations} iterations, batchsize {batchsize} "
    )
    print("****************************************************************")


# ******************************************************************************
# Main Command Line Interface
# ******************************************************************************
def main():
    def get_args():
        parser = argparse.ArgumentParser(
            description="pugetbench-mingpt.py is the setup user interface for a  simple GPU performance benchmark using Andrej Karpathy's minGPT code."
        )
        parser.add_argument(
            "-i",
            "--iterations",
            type=int,
            default=1000,
            help="Number of iterations to run the benchmark",
        )
        parser.add_argument(
            "-b",
            "--batchsize",
            type=int,
            default=32,
            help="Batch size to use for the benchmark",
        )
        return parser.parse_args()

    args = get_args()

    iterations = args.iterations
    batchsize = args.batchsize

    # ******************************************************************************
    # Print some kind of message about usage and such
    # ******************************************************************************
    # print(
    #     "pugetbench-mingpt.py is the setup-and-run user interface for a  simple GPU performance benchmark using Andrej Karpathy's minGPT code."
    # )

    # ******************************************************************************
    # Run micromamba to create the env needed to run minGPT
    # ******************************************************************************
    mk_bench_env()

    # ******************************************************************************
    # Run the benchmark
    # ******************************************************************************
    sys_env = set_py_environment(MAMBA_ENVS / ENV_NAME)
    run_chargpt(iterations, batchsize, sys_env)


if __name__ == "__main__":
    main()
