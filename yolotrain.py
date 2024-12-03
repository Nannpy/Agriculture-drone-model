{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QCm616v7Nige",
        "outputId": "47f10dbc-233c-437e-8869-bf217d6704bd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: ultralytics in /usr/local/lib/python3.10/dist-packages (8.2.86)\n",
            "Requirement already satisfied: numpy<2.0.0,>=1.23.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (1.26.4)\n",
            "Requirement already satisfied: matplotlib>=3.3.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (3.7.1)\n",
            "Requirement already satisfied: opencv-python>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (4.10.0.84)\n",
            "Requirement already satisfied: pillow>=7.1.2 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (9.4.0)\n",
            "Requirement already satisfied: pyyaml>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (6.0.2)\n",
            "Requirement already satisfied: requests>=2.23.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.32.3)\n",
            "Requirement already satisfied: scipy>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (1.13.1)\n",
            "Requirement already satisfied: torch>=1.8.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.4.0+cu121)\n",
            "Requirement already satisfied: torchvision>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (0.19.0+cu121)\n",
            "Requirement already satisfied: tqdm>=4.64.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (4.66.5)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.10/dist-packages (from ultralytics) (5.9.5)\n",
            "Requirement already satisfied: py-cpuinfo in /usr/local/lib/python3.10/dist-packages (from ultralytics) (9.0.0)\n",
            "Requirement already satisfied: pandas>=1.1.4 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.1.4)\n",
            "Requirement already satisfied: seaborn>=0.11.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (0.13.1)\n",
            "Requirement already satisfied: ultralytics-thop>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.0.6)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (1.2.1)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (4.53.1)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (1.4.5)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (24.1)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (3.1.4)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.4->ultralytics) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.4->ultralytics) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (3.8)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (2024.7.4)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.15.4)\n",
            "Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (4.12.2)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (1.13.2)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.1.4)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (2024.6.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib>=3.3.0->ultralytics) (1.16.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch>=1.8.0->ultralytics) (2.1.5)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch>=1.8.0->ultralytics) (1.3.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install ultralytics"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tJvJKxG3Muy3"
      },
      "outputs": [],
      "source": [
        "from ultralytics import YOLO\n",
        "from PIL import Image\n",
        "import cv2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9atQcgr_OuE1",
        "outputId": "d5640691-d97b-4dd8-8646-f5213257d06d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting roboflow\n",
            "  Downloading roboflow-1.1.44-py3-none-any.whl.metadata (9.7 kB)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from roboflow) (2024.7.4)\n",
            "Collecting idna==3.7 (from roboflow)\n",
            "  Downloading idna-3.7-py3-none-any.whl.metadata (9.9 kB)\n",
            "Requirement already satisfied: cycler in /usr/local/lib/python3.10/dist-packages (from roboflow) (0.12.1)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.4.5)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (from roboflow) (3.7.1)\n",
            "Requirement already satisfied: numpy>=1.18.5 in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.26.4)\n",
            "Requirement already satisfied: opencv-python-headless==4.10.0.84 in /usr/local/lib/python3.10/dist-packages (from roboflow) (4.10.0.84)\n",
            "Requirement already satisfied: Pillow>=7.1.2 in /usr/local/lib/python3.10/dist-packages (from roboflow) (9.4.0)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.8.2)\n",
            "Collecting python-dotenv (from roboflow)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.32.3)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.16.0)\n",
            "Requirement already satisfied: urllib3>=1.26.6 in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.0.7)\n",
            "Requirement already satisfied: tqdm>=4.41.0 in /usr/local/lib/python3.10/dist-packages (from roboflow) (4.66.5)\n",
            "Requirement already satisfied: PyYAML>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from roboflow) (6.0.2)\n",
            "Collecting requests-toolbelt (from roboflow)\n",
            "  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)\n",
            "Collecting filetype (from roboflow)\n",
            "  Downloading filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (1.2.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (4.53.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (24.1)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (3.1.4)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->roboflow) (3.3.2)\n",
            "Downloading roboflow-1.1.44-py3-none-any.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.9/79.9 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading idna-3.7-py3-none-any.whl (66 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m66.8/66.8 kB\u001b[0m \u001b[31m4.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading filetype-1.2.0-py2.py3-none-any.whl (19 kB)\n",
            "Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.5/54.5 kB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: filetype, python-dotenv, idna, requests-toolbelt, roboflow\n",
            "  Attempting uninstall: idna\n",
            "    Found existing installation: idna 3.8\n",
            "    Uninstalling idna-3.8:\n",
            "      Successfully uninstalled idna-3.8\n",
            "Successfully installed filetype-1.2.0 idna-3.7 python-dotenv-1.0.1 requests-toolbelt-1.0.0 roboflow-1.1.44\n",
            "loading Roboflow workspace...\n",
            "loading Roboflow project...\n",
            "Dependency ultralytics==8.0.196 is required but found version=8.2.86, to fix: `pip install ultralytics==8.0.196`\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading Dataset Version Zip in data-depa-1 to yolov8:: 100%|██████████| 27649/27649 [00:01<00:00, 16240.20it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n",
            "Extracting Dataset Version Zip to data-depa-1 in yolov8:: 100%|██████████| 726/726 [00:00<00:00, 1846.35it/s]\n"
          ]
        }
      ],
      "source": [
        "!pip install roboflow\n",
        "\n",
        "from roboflow import Roboflow\n",
        "rf = Roboflow(api_key=\"1A8E6CEAshnFY7hgeJV1\")\n",
        "project = rf.workspace(\"nannam\").project(\"data-depa\")\n",
        "version = project.version(1)\n",
        "dataset = version.download(\"yolov8\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = YOLO('yolov8n.pt')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0zN_VH_CzkyA",
        "outputId": "d3705db8-6a87-4abe-bb45-4d037ac2ba8a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt to 'yolov8n.pt'...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 6.25M/6.25M [00:00<00:00, 77.4MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s02nEVrZNlkq",
        "outputId": "d07eae0b-1bad-4954-aba8-589e95491d1d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt to 'yolov8n.pt'...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 6.25M/6.25M [00:00<00:00, 108MB/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ultralytics YOLOv8.2.86 🚀 Python-3.10.12 torch-2.4.0+cu121 CUDA:0 (Tesla T4, 15102MiB)\n",
            "\u001b[34m\u001b[1mengine/trainer: \u001b[0mtask=detect, mode=train, model=yolov8n.pt, data=/content/data-depa-1/data.yaml, epochs=30, time=None, patience=100, batch=8, imgsz=640, save=True, save_period=-1, cache=False, device=None, workers=8, project=None, name=train, exist_ok=False, pretrained=True, optimizer=auto, verbose=True, seed=0, deterministic=True, single_cls=False, rect=False, cos_lr=False, close_mosaic=10, resume=False, amp=True, fraction=1.0, profile=False, freeze=None, multi_scale=False, overlap_mask=True, mask_ratio=4, dropout=0.0, val=True, split=val, save_json=False, save_hybrid=False, conf=0.4, iou=0.7, max_det=300, half=False, dnn=False, plots=True, source=None, vid_stride=1, stream_buffer=False, visualize=False, augment=False, agnostic_nms=False, classes=None, retina_masks=False, embed=None, show=False, save_frames=False, save_txt=False, save_conf=False, save_crop=False, show_labels=True, show_conf=True, show_boxes=True, line_width=None, format=torchscript, keras=False, optimize=False, int8=False, dynamic=False, simplify=False, opset=None, workspace=4, nms=False, lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=7.5, cls=0.5, dfl=1.5, pose=12.0, kobj=1.0, label_smoothing=0.0, nbs=64, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, bgr=0.0, mosaic=1.0, mixup=0.0, copy_paste=0.0, auto_augment=randaugment, erasing=0.4, crop_fraction=1.0, cfg=None, tracker=botsort.yaml, save_dir=runs/detect/train\n",
            "Downloading https://ultralytics.com/assets/Arial.ttf to '/root/.config/Ultralytics/Arial.ttf'...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 755k/755k [00:00<00:00, 20.5MB/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overriding model.yaml nc=80 with nc=2\n",
            "\n",
            "                   from  n    params  module                                       arguments                     \n",
            "  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 \n",
            "  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                \n",
            "  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             \n",
            "  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                \n",
            "  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             \n",
            "  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               \n",
            "  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           \n",
            "  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              \n",
            "  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           \n",
            "  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 \n",
            " 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          \n",
            " 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           \n",
            " 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 \n",
            " 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          \n",
            " 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           \n",
            " 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  \n",
            " 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                \n",
            " 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           \n",
            " 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 \n",
            " 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              \n",
            " 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           \n",
            " 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 \n",
            " 22        [15, 18, 21]  1    751702  ultralytics.nn.modules.head.Detect           [2, [64, 128, 256]]           \n",
            "Model summary: 225 layers, 3,011,238 parameters, 3,011,222 gradients, 8.2 GFLOPs\n",
            "\n",
            "Transferred 319/355 items from pretrained weights\n",
            "\u001b[34m\u001b[1mTensorBoard: \u001b[0mStart with 'tensorboard --logdir runs/detect/train', view at http://localhost:6006/\n",
            "Freezing layer 'model.22.dfl.conv.weight'\n",
            "\u001b[34m\u001b[1mAMP: \u001b[0mrunning Automatic Mixed Precision (AMP) checks with YOLOv8n...\n",
            "\u001b[34m\u001b[1mAMP: \u001b[0mchecks passed ✅\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "`torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.\n",
            "\u001b[34m\u001b[1mtrain: \u001b[0mScanning /content/data-depa-1/train/labels... 315 images, 0 backgrounds, 0 corrupt: 100%|██████████| 315/315 [00:00<00:00, 2055.43it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[34m\u001b[1mtrain: \u001b[0mNew cache created: /content/data-depa-1/train/labels.cache\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[34m\u001b[1malbumentations: \u001b[0mBlur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01), CLAHE(p=0.01, clip_limit=(1, 4.0), tile_grid_size=(8, 8))\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "os.fork() was called. os.fork() is incompatible with multithreaded code, and JAX is multithreaded, so this will likely lead to a deadlock.\n",
            "\u001b[34m\u001b[1mval: \u001b[0mScanning /content/data-depa-1/valid/labels... 27 images, 0 backgrounds, 0 corrupt: 100%|██████████| 27/27 [00:00<00:00, 1584.35it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[34m\u001b[1mval: \u001b[0mNew cache created: /content/data-depa-1/valid/labels.cache\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Plotting labels to runs/detect/train/labels.jpg... \n",
            "\u001b[34m\u001b[1moptimizer:\u001b[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... \n",
            "\u001b[34m\u001b[1moptimizer:\u001b[0m AdamW(lr=0.001667, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)\n",
            "\u001b[34m\u001b[1mTensorBoard: \u001b[0mmodel graph visualization added ✅\n",
            "Image sizes 640 train, 640 val\n",
            "Using 2 dataloader workers\n",
            "Logging results to \u001b[1mruns/detect/train\u001b[0m\n",
            "Starting training for 30 epochs...\n",
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       1/30      1.26G      1.605      2.823      1.927         10        640: 100%|██████████| 40/40 [00:09<00:00,  4.32it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  6.08it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35          0          0          0          0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       2/30       1.2G       1.62      2.333       1.93         10        640: 100%|██████████| 40/40 [00:10<00:00,  3.95it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:01<00:00,  1.42it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.792      0.274      0.551      0.293\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       3/30       1.2G       1.62      2.213      1.914          5        640: 100%|██████████| 40/40 [00:06<00:00,  6.49it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  4.93it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.498       0.74      0.582      0.219\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       4/30       1.2G      1.629      2.117      1.916          5        640: 100%|██████████| 40/40 [00:08<00:00,  4.52it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.36it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.778      0.231      0.326      0.172\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       5/30       1.2G       1.68       2.14      1.944          7        640: 100%|██████████| 40/40 [00:06<00:00,  6.60it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.22it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.361      0.403      0.287      0.134\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       6/30       1.2G      1.591      2.041       1.87         11        640: 100%|██████████| 40/40 [00:08<00:00,  4.64it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.07it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.326      0.382      0.357      0.182\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       7/30       1.2G      1.562      1.915      1.838         10        640: 100%|██████████| 40/40 [00:06<00:00,  6.49it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.39it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.625     0.0839       0.34      0.148\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       8/30       1.2G       1.58       1.88      1.849         11        640: 100%|██████████| 40/40 [00:09<00:00,  4.38it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.07it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.495      0.594      0.569      0.256\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "       9/30       1.2G      1.507      1.818      1.786         13        640: 100%|██████████| 40/40 [00:06<00:00,  6.64it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.23it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.866      0.542      0.727      0.444\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      10/30       1.2G      1.494      1.704      1.745          6        640: 100%|██████████| 40/40 [00:09<00:00,  4.23it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.87it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35       0.79      0.673      0.764      0.331\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      11/30       1.2G      1.481      1.782      1.763          5        640: 100%|██████████| 40/40 [00:06<00:00,  6.47it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00, 10.74it/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35       0.93      0.399      0.662      0.341\n",
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      12/30       1.2G      1.455      1.655      1.732          9        640: 100%|██████████| 40/40 [00:09<00:00,  4.43it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.25it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.762      0.623      0.725      0.424\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      13/30       1.2G      1.438      1.581      1.742         11        640: 100%|██████████| 40/40 [00:06<00:00,  6.50it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.39it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.943      0.631      0.822      0.408\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      14/30       1.2G      1.395      1.525      1.716          8        640: 100%|██████████| 40/40 [00:08<00:00,  4.47it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.78it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.903      0.595       0.83      0.443\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      15/30       1.2G      1.419      1.545      1.673          6        640: 100%|██████████| 40/40 [00:06<00:00,  6.62it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  9.45it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.816      0.696      0.751      0.349\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      16/30       1.2G      1.388      1.445      1.675          7        640: 100%|██████████| 40/40 [00:08<00:00,  4.50it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  9.73it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.827      0.657      0.744      0.364\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      17/30       1.2G      1.422      1.498      1.682         10        640: 100%|██████████| 40/40 [00:05<00:00,  6.71it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.72it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.812      0.787      0.898      0.454\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      18/30       1.2G      1.377      1.429       1.66         10        640: 100%|██████████| 40/40 [00:08<00:00,  4.48it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.92it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.733      0.818       0.86      0.459\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      19/30       1.2G      1.337      1.358      1.636         11        640: 100%|██████████| 40/40 [00:05<00:00,  6.77it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.37it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.803      0.839      0.896      0.468\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      20/30       1.2G      1.308      1.335      1.614         11        640: 100%|██████████| 40/40 [00:09<00:00,  4.38it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  9.09it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.871      0.871      0.909      0.525\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Closing dataloader mosaic\n",
            "\u001b[34m\u001b[1malbumentations: \u001b[0mBlur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01), CLAHE(p=0.01, clip_limit=(1, 4.0), tile_grid_size=(8, 8))\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "os.fork() was called. os.fork() is incompatible with multithreaded code, and JAX is multithreaded, so this will likely lead to a deadlock.\n",
            "os.fork() was called. os.fork() is incompatible with multithreaded code, and JAX is multithreaded, so this will likely lead to a deadlock.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      21/30       1.2G      1.351      1.424      1.743          6        640: 100%|██████████| 40/40 [00:07<00:00,  5.68it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.62it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35        0.9       0.78      0.883      0.507\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      22/30       1.2G      1.255      1.304      1.755          3        640: 100%|██████████| 40/40 [00:09<00:00,  4.26it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.50it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.852      0.893      0.923      0.505\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      23/30       1.2G       1.25      1.215      1.698          4        640: 100%|██████████| 40/40 [00:05<00:00,  6.90it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.91it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.896      0.867      0.923      0.547\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      24/30       1.2G      1.245      1.195      1.689          6        640: 100%|██████████| 40/40 [00:09<00:00,  4.20it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.76it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.731      0.844      0.921       0.49\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      25/30       1.2G      1.178      1.171       1.63          4        640: 100%|██████████| 40/40 [00:05<00:00,  6.89it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  5.79it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.933       0.82      0.944      0.574\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      26/30       1.2G      1.174      1.076      1.622          3        640: 100%|██████████| 40/40 [00:09<00:00,  4.41it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  7.35it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.864      0.906      0.933      0.557\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      27/30       1.2G      1.123      1.042      1.551          4        640: 100%|██████████| 40/40 [00:05<00:00,  6.81it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  8.21it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.911      0.914      0.952      0.614\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      28/30       1.2G      1.152      1.059      1.592          6        640: 100%|██████████| 40/40 [00:08<00:00,  4.95it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  4.71it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.889      0.934      0.956      0.596\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      29/30       1.2G      1.146      1.022      1.558          6        640: 100%|██████████| 40/40 [00:05<00:00,  6.95it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  9.30it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35       0.88      0.871      0.941      0.627\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "      30/30       1.2G      1.096     0.9692      1.544          4        640: 100%|██████████| 40/40 [00:07<00:00,  5.36it/s]\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  4.49it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.913        0.9      0.933      0.626\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "30 epochs completed in 0.073 hours.\n",
            "Optimizer stripped from runs/detect/train/weights/last.pt, 6.2MB\n",
            "Optimizer stripped from runs/detect/train/weights/best.pt, 6.2MB\n",
            "\n",
            "Validating runs/detect/train/weights/best.pt...\n",
            "Ultralytics YOLOv8.2.86 🚀 Python-3.10.12 torch-2.4.0+cu121 CUDA:0 (Tesla T4, 15102MiB)\n",
            "Model summary (fused): 168 layers, 3,006,038 parameters, 0 gradients, 8.1 GFLOPs\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00:00<00:00,  4.02it/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                   all         27         35      0.878      0.871      0.941      0.626\n",
            "              Hangyeah         15         22      0.889      0.818      0.902      0.517\n",
            "          Not-Hangyeah         12         13      0.867      0.923       0.98      0.735\n",
            "Speed: 0.3ms preprocess, 5.9ms inference, 0.0ms loss, 2.7ms postprocess per image\n",
            "Results saved to \u001b[1mruns/detect/train\u001b[0m\n"
          ]
        }
      ],
      "source": [
        "# set\n",
        "model = YOLO('yolov8n.pt')\n",
        "\n",
        "results = model.train(data = '/content/data-depa-1/data.yaml',imgsz = 640,epochs = 30,batch = 8,conf = 0.4)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VTh9nDDyDp7P",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a885ee3c-27f7-4e59-e196-d27262923c04"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vvkEKtpMfAjL"
      },
      "outputs": [],
      "source": [
        "img = Image.open('/content/Hangyeah(depa)-1/valid/images/DSCF8371-horz2_jpg.rf.9683d81aaf5d027159ef596ebf7f169e.jpg')\n",
        "img"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "AAV6izxuDr0H",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "577facc5-78a3-43ab-a1ed-a88e2e7900e9"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content/drive/My Drive/hangyeahdetect1.zip'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "import shutil\n",
        "import os\n",
        "from google.colab import files\n",
        "\n",
        "# ระบุโฟลเดอร์ที่ต้องการบีบอัดเป็น Zip\n",
        "source_folder = '/content/runs/detect/train'\n",
        "\n",
        "# ชื่อไฟล์ Zip ที่ต้องการสร้าง\n",
        "zip_filename = 'hangyeahdetect1.zip'\n",
        "\n",
        "# สร้าง Zip file\n",
        "shutil.make_archive('/content/' + zip_filename, 'zip', source_folder)\n",
        "\n",
        "# ย้าย Zip file ไปยัง Google Drive\n",
        "shutil.move('/content/' + zip_filename + '.zip', '/content/drive/My Drive/' + zip_filename)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from PIL import Image\n",
        "im = Image.open('/content/image51_jpeg.rf.8e1046506a08906fe1100a6847c4c064.jpg')\n",
        "results = model.predict(source=im, save=True)\n",
        "# display(Image.open('/content/runs/detect/train3/c-139-_bmp_jpg.rf.b8d6e685fc8b5e16b26c16856bf6ff5b.jpg'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G2dEUALmzFfr",
        "outputId": "2a904b01-5440-4e52-8c96-c1b532026a81"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "0: 640x640 (no detections), 255.7ms\n",
            "Speed: 4.6ms preprocess, 255.7ms inference, 1.1ms postprocess per image at shape (1, 3, 640, 640)\n",
            "Results saved to \u001b[1mruns/detect/predict\u001b[0m\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "T4",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}