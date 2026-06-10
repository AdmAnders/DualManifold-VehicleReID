# Feature-Based-Vehicle-Re-identification-using-Nonlinear-Methods


Official implementation of Feature-Based Vehicle Re-identification using Nonlinear Methods, a vehicle re-identification framework designed to improve robust visual representation learning under challenging viewpoint, color, body-type, and attribute-level variations.

> **Status:** Manuscript under review
> **Task:** Vehicle Re-Identification
> **Datasets:** VeRi-776, VehicleID, VeRi-Wild
> **Backbone:** EfficientNet / Vision Transformer / CLIP-based encoder
> **Main Contributions:** Attribute-aware representation learning, confusable vehicle mining, part-level pooling, and memory-enhanced metric learning.

---

## Overview

Vehicle re-identification aims to retrieve the same vehicle across non-overlapping cameras under significant changes in viewpoint, illumination, occlusion and intra-class similarity. This repository provides the official code, configuration files, training scripts and evaluation pipeline for our proposed framework.

Our method focuses on three main challenges:

1. **Fine-grained visual similarity:** vehicles with the same color and body type are difficult to distinguish.
2. **Viewpoint variation:** front, rear and side views introduce large appearance changes.
3. **Attribute-level ambiguity:** visually similar vehicles may share color, type, sunroof, tone and camera-view attributes.

To address these issues, we introduce a representation learning pipeline that combines global identity features with attribute-aware and part-aware cues.

---

## Framework

<p align="center">
  <img src="figures/framework_overview.png" width="850">
</p>

The proposed framework contains the following major components:

* **Backbone Encoder:** extracts deep visual representations from vehicle images.
* **Attribute-Aware Branch:** learns semantic cues such as color, body type, viewpoint and additional vehicle attributes.
* **Vehicle Part Pooling Module:** emphasizes discriminative local regions of the vehicle.
* **Confusable Vehicle Mining:** identifies visually similar vehicles and improves inter-class separation.
* **Memory-Based Metric Learning:** stabilizes training by comparing samples with a dynamic feature memory bank.

---

## Key Features

* End-to-end training and evaluation pipeline.
* Support for multiple vehicle re-identification datasets.
* Configurable backbone and loss components.
* Attribute-aware and part-aware feature learning.
* Reproducible experimental setup.
* Ready-to-use scripts for training, testing and feature extraction.
* Paper-friendly figures and qualitative visualization tools.

---

## Repository Structure

```text
.
├── configs/              # Dataset and experiment configuration files
├── datasets/             # Dataset preparation instructions
├── figures/              # Framework and result visualizations
├── paper/                # LaTeX manuscript files
├── results/              # Quantitative and qualitative results
├── scripts/              # Training, testing and visualization scripts
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Installation

```bash
git clone https://github.com/[hidayetergn]/DualManifold-VehicleReID.git
cd DualManifold-VehicleReID

conda create -n vehicle-reid python=3.10
conda activate vehicle-reid

pip install -r requirements.txt
```

Recommended environment:

```text
Python >= 3.10
PyTorch >= 2.0
CUDA >= 11.8
torchvision
timm
numpy
pandas
scikit-learn
Pillow
tqdm
matplotlib
```

---

## Dataset Preparation

This repository supports the following datasets:

| Dataset   | Task                      | Status    |
| --------- | ------------------------- | --------- |
| VeRi-776  | Vehicle Re-ID             | Supported Image|
| VehicleID | Vehicle Re-ID             | Supported Link |
| VRU       | Vehicle Re-ID             | Supported Link |

Expected dataset layout:

```text
data/
├── VeRi/
│   ├── image_train/
│   ├── image_query/
│   ├── image_test/
│   ├── train_list.txt
│   ├── query_list.txt
│   └── test_list.txt
│
├── VehicleID/
│   └── Download Link
│
└── VeRi-Wild/
    └── Download Link
```

Please download the datasets from their official sources and update the corresponding paths in the configuration files under `configs/`.

---

## Training

Example training command for VeRi-776:

```bash
python scripts/train.py \
  --config configs/veri776.yaml \
  --output outputs/veri776_experiment
```

---

## Evaluation

```bash
python scripts/test.py \
  --config configs/veri776.yaml \
  --checkpoint checkpoints/best_model.pth
```

The evaluation script reports standard vehicle re-identification metrics:

* Rank-1 Accuracy
* Rank-5 Accuracy
* Rank-10 Accuracy
* mean Average Precision, mAP

---

## Experimental Results

### VeRi-776

| Method          | Rank-1 | Rank-5 |  mAP |
| --------------- | -----: | -----: | ---: |
| Proposed Method |  97.87 |  99.26 | 90.78|

### VehicleID

| Test Split | Rank-1 | Rank-5 |
| ---------- | -----: | -----: |
| Small      |  98.09 |  99.48 |
| Medium     |  97.21 |  98.76 |
| Large      |  95.72 |  98.20 |

---

## Qualitative Results

<p align="center">
  <img src="figures/qualitative_results.png" width="850">
</p>

The qualitative retrieval examples demonstrate that the proposed model can distinguish visually similar vehicles under challenging camera viewpoints, illumination conditions and attribute-level similarities.

---

## Reproducibility Checklist

* [x] Training and evaluation scripts are provided.
* [x] Dataset preparation instructions are included.
* [x] Configuration files are provided.
* [x] Model components are modularized.
* [x] Evaluation metrics are reported.
* [x] Qualitative examples are included.
* [x] Citation metadata is provided.

---

## Citation

If you find this work useful, please cite:

```bibtex
@article{ergin2026dualmanifold,
  title   = {[Feature-Based Vehicle Re-identification using Nonlinear Methods]},
  author  = {Ergin, Hidayet and KEÇELİ, Ali Seydi},
  journal = {[]},
  year    = {2026}
}
```

## License

This project is released under the terms specified in the `LICENSE` file.

Please note that dataset files are not included in this repository. Users should obtain each dataset from its official source and comply with the corresponding dataset license.
