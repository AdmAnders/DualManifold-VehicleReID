import torch

class Config:
    # ── Paths ──────────────────────────────────────────
    TRAIN_TXT   = "/.…/VeRi-776/train_list.txt"
    TRAIN_DIR   = "/..../image_train"
    QUERY_TXT   = "/.…/VeRi-776/query_list.txt"
    QUERY_DIR   = "/.../image_query"
    GALLERY_TXT = "/.…./VeRi-776/test_list.txt"
    GALLERY_DIR = "/..../image_test"
    SAVE_DIR    = "/content/VeRiOHN_PyTorch/"

    # ── Görüntü ─────────────────────────────────────────
    IMG_SIZE    = 384
    MEAN        = [0.485, 0.456, 0.406]
    STD         = [0.229, 0.224, 0.225]

    # ── ONN ─────────────────────────────────────────────
    TAYLOR_Q    = 3
    CLIP_VAL    = 3.0

    # ── Eğitim ──────────────────────────────────────────
    EPOCHS      = 150
    BATCH_SIZE  = 64
    LR          = 2e-4
    WEIGHT_DECAY= 5e-4
    MARGIN      = 0.3
    EMBED_DIM   = 512
    WARMUP_EP   = 10

    # ── Circle Loss ─────────────────────────────────────
    CIRCLE_M    = 0.25
    CIRCLE_GAMMA= 64

    # ── Donanım ─────────────────────────────────────────
    DEVICE      = "cuda" if torch.cuda.is_available() else "cpu"
    NUM_WORKERS = 2
    PIN_MEMORY  = True

cfg = Config()