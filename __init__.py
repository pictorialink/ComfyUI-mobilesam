import sys
import os

modules_path = os.path.join(os.path.dirname(__file__), "modules")
sys.path.append(modules_path)

from .modules.model import MobileSamModelLoader
from .modules.detector import MobileSamDetector
from .modules.predictor import MobileSamPredictor

NODE_CLASS_MAPPINGS = {
    "MobileSamDetector": MobileSamDetector,
    "MobileSamPredictor": MobileSamPredictor,
    "MobileSamModelLoader": MobileSamModelLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MobileSamDetector": "Mobile SAM Detector",
    "MobileSamPredictor": "Mobile SAM Predictor",
    "MobileSamModelLoader": "Mobile SAM Model Loader",
}