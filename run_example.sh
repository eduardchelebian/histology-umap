python main.py \
--slide_path='slides/PANDA_C1_3401.tif' \
--mask_path='masks/PANDA_C1_3401_mask.tif' \
--save_path='results/PANDA_C1_3401' \
--patch_shape=512 \
--overlap=.25 \
--mask_th=.5 \
--imagenet_weights=False \
--model_path='pretrained_resnet18.ckpt' \
--num_workers=4 \
