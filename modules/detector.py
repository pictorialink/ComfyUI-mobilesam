import numpy as np
import torch

class MobileSamDetector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mobile_sam_predictor": ("Mobile_SAM_Predictor", ),
                "start_x": ("INT",{"default": 0, "min": 0, "step": 1}),
                "start_y": ("INT",{"default": 0, "min": 0, "step": 1}),
            },
            "optional": {
                "end_x": ("INT",{"default": 0, "min": 0, "step": 1}),
                "end_y": ("INT",{"default": 0, "min": 0, "step": 1}),
            }
        }
    CATEGORY = "MobileSam"
    FUNCTION = "detect"
    RETURN_TYPES = ("MASK", )

    def detect(self, mobile_sam_predictor, start_x, start_y, end_x, end_y):
        box = np.array([start_x, start_y, end_x, end_y])
        if end_x == 0 and end_y == 0:
            masks, scores, logits = mobile_sam_predictor.predict(
                point_coords=np.array([box[:2]]),
                point_labels=np.array([1]),
                box=None,
                multimask_output=True,
            )
        else:
            masks, scores, logits = mobile_sam_predictor.predict(
                point_coords=None,
                point_labels=None,
                box=box[None, :],
                multimask_output=True,
            )
        mask = torch.from_numpy(masks[np.argmax(scores)])
        mask = mask.unsqueeze(0)
        return (mask,)