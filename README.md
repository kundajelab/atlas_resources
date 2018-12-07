# atlas resources

---

dk suggestion
- master is saved for finalized code
- things get merged into develop and must pass tests first before going to master
- new features/code first goes into branches from develop

---

Code is pulled from tronn, just the data parts isolated. Example below goes from BED file (assumes bed file is all positives) and generates h5 files ffor use in deep learning workflows.

---

**Example workflow**

Create an environment and install tensorflow

```
conda create -n atlas_test python=2 anaconda
source activate atlas_test
pip install --upgrade tensorflow-gpu
```

Install this repo (use install simply because i'm copying over from tronn and it's set up that way over there)

```
# cd to the atlas resources
python setup.py develop

# confirm it works
tronn --help
tronn preprocess --help
```

Preprocess datasets, requires you have bedtools (and ucsc_tools if any signals to process)

```
git clone https://github.com/kundajelab/dragonn_benchmark_data.git

# cd to examples dir, adjust DATA and WORK dirs, and run the script
# produces a set of h5 files, altogether is ~8GB, takes about 8 min with 24 threads
source preprocess.bash
```

Do a test of data loading

```
# in examples folder
# FYI variety of data loading warnings will pop up if you use latest tensorflow
python load_gpu_test.py
python load_generator_test.py

```
