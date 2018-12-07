# atlas resources

WORKFLOW

Create an environment

```
conda create -n atlas_test python=2 anaconda
source activate atlas_test
pip install --upgrade tensorflow-gpu
```

Install

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
source preprocess.bash
```

Do a test of data loading

```




```


dk suggestion
- master is saved for finalized code
- things get merged into develop and must pass tests first before going to master
- new features/code first goes into branches from develop