from mobile_sam import SamPredictor

class MobileSamPredictor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mobile_sam_model": ("Mobile_SAM_MODEL", ),
                "image": ("IMAGE", ),
            }
        }
    CATEGORY = "MobileSam"
    FUNCTION = "make_predictor"
    RETURN_TYPES = ("Mobile_SAM_Predictor", )

    def make_predictor(self, mobile_sam_model, image):
        predictor = SamPredictor(mobile_sam_model)
        predictor.set_image(image[0].numpy())
        return (predictor, )
