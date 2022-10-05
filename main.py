import argparse
import numpy as np

from utils.patch_extraction import load_images, load_images_openslide, generate_coordinates, save_patches 
from utils.generate_embeddings import load_model, generate_umap


def main(args):
    image, mask = load_images_openslide(args.slide_path, args.mask_path)
    print('Images loaded')
    coords = generate_coordinates(mask.shape, args.patch_shape, args.overlap)
    save_patches(coords, args.mask_th, image, mask, args.save_path)
    backbone = load_model(args.imagenet_weights, args.model_path)
    generate_umap(backbone, args.save_path, args.num_workers)
    

parser = argparse.ArgumentParser(description='Patch and feature extraction configuration')
parser.add_argument('--slide_path', type=str, default=None, 
                    help='slide directory')
parser.add_argument('--mask_path', type=str, default=None, 
                    help='mask directory')
parser.add_argument('--save_path', type=str, default=None, 
                    help='saving directory')
parser.add_argument('--patch_shape', type=int, default=256, 
                    help='desired shape of the patches')
parser.add_argument('--overlap', type=float, default=.5, 
                    help='percentage of overlap between patches (0-1)')
parser.add_argument('--mask_th', type=float, default=.5, 
                    help='minimum percentage of mask to accept a patch (0-1)')
parser.add_argument('--imagenet_weights', type=bool, default=True, 
                    help='whether to use imagenet_weights or other pretrained weights; specify model_path in that case')
parser.add_argument('--model_path', type=str, default=None, 
                    help='path where the pretrained model checkpoints are located')
parser.add_argument('--num_workers', type=int, default=32, 
                    help='Number of workers')

args = parser.parse_args()

if __name__ == "__main__":
    results = main(args)
    print("Finished!")


