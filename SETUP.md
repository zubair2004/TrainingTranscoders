# Quick Setup Guide

## Issues Fixed

1. ✅ **Cache directory permissions** - Fixed in `common/utils.py`
2. ✅ **Checkpoint save directory** - Fixed in `common/utils.py` 
3. ✅ **Missing dependencies** - Installed and pinned in `requirements.txt`

## Running the Training Script

### Option 1: Configure WandB (Recommended for tracking experiments)

Update your WandB credentials when running:

```bash
python train.py --wandb_project_name "your-project" --wandb_entity "your-username"
```

For example, based on your login:
```bash
python train.py --wandb_project_name "sae-experiments" --wandb_entity "zubairbashir2004-iit-kharagpur"
```

### Option 2: Disable WandB (Quickest to test)

If you just want to run the script without experiment tracking:

```bash
WANDB_MODE=disabled python train.py
```

## What Was Changed

### `common/utils.py`
- **Lines 3-4**: Cache directories changed from `/workspace/cache/` to `~/.cache/huggingface/`
- **Line 200**: Checkpoint directory changed from `/workspace/1L-Sparse-Autoencoder/checkpoints` to `./checkpoints`

### `requirements.txt`
- Pinned all package versions to ensure compatibility
- Key version: `transformers == 4.56.2` (compatible with `transformer-lens == 2.16.1`)

## Current Errors Explained

1. **WandB entity error**: The config uses `"your_entity_name"` as a placeholder. Use one of the options above to fix this.
2. **Checkpoint directory error**: Now fixed! Checkpoints will save to `./checkpoints/`
