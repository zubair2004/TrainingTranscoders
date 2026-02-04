#!/usr/bin/env python3
"""
Helper script to configure WandB settings for train.py

This allows you to set your WandB project and entity names without editing train.py.
You can also disable WandB logging entirely if you prefer.
"""

import sys

def show_help():
    print("""
Usage: python train.py [options]

WandB Configuration Options:
  --wandb_project_name <name>    Set WandB project name (default: "your_project_name")
  --wandb_entity <name>          Set WandB entity/username (default: "your_entity_name")
  
Example with WandB configured:
  python train.py --wandb_project_name "sae-training" --wandb_entity "zubairbashir2004-iit-kharagpur"

Alternative: Disable WandB
  If you don't want to use WandB tracking, you can disable it by setting WANDB_MODE=disabled:
  
  WANDB_MODE=disabled python train.py

Note: The config uses placeholder values by default. Update them with your actual WandB
      credentials, or disable WandB using the environment variable above.
""")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        show_help()
    else:
        print("Run with --help for configuration options")
