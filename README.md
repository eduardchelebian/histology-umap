# Interpreting deep histology features as RGB colors

This repository contains the code for:
1. Extracting latent network representations using the pretrained network of choice
2. Reducing their dimensionality using Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) to 3 components
3. Mapping the three dimensional features to RGB space

`[insert example image]` 

## How to run

Create a conda environment and install all the required packages
```
conda create --name histology-umap --file requirements.txt
```

Run the shell sript `run_example.sh` that calls the main function `main.py`
```
sh run_example.sh
```

It contains all the hyperparameters you might want to tune:
```
slide_path (str): location of the slide to analyze
mask_path (str): location of the correspnding mask
save_path (str): desired location for saving the extracted patches and the RGB UMAP space
patch_shape (tuple): desired shape of the patches
overlap (float): percentage of overlap between patches (0-1) 
mask_th (float): tissue mask of the regions of interest (0-1)
imagenet_weights (bool): whether to use ImageNet pretrained network for feature extraction
model_path (str): if imagenet_weights=False, specify your own .ckpt file
num_workers (int): how many subprocesses to use for data loading. 0 means that the data will be loaded in the main process
```

## Visualization

We provide the `visualize_results.ipynb` notebook to visualize the overlay of the UMAP colors and the reduced dimensionality space. But we recommend using TissUUmaps for visualization, as it allows interactive selection of regions between the histology and the UMAP spaces. You can download it visiting [the official website](https://tissuumaps.github.io/download/) and make sure to active the `Feature_Space` plugin.

`[insert example image]` 

## Applications

This approach is inspired by the spatial-omics field, where one already has coordinates representing gene expression and thus can directly extract features from the coordinates. If you are interested in such approaches, you can watch the (https://tissuumaps.github.io/tutorials/#cnn)[tutorial video] created with that application in mind.

## Citations
These ideas were used in the following papers:

```
@article{chelebian2021morphological,
  title={Morphological Features Extracted by AI Associated with Spatial Transcriptomics in Prostate Cancer},
  author={Chelebian, Eduard and Avenel, Christophe and Kartasalo, Kimmo and Marklund, Maja and Tanoglidi, Anna and Mirtti, Tuomas and Colling, Richard and Erickson, Andrew and Lamb, Alastair D and Lundeberg, Joakim and others},
  journal={Cancers},
  volume={13},
  number={19},
  pages={4837},
  year={2021},
  publisher={MDPI}
}
```
