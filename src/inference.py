from diffusers import StableDiffusionPipeline
import torch

class Inference:
    
    def __init__(self, model_name: str="nota-ai/bk-sdm-small")->None:
        self.__model_name: str = model_name
    
    def text2image(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return StableDiffusionPipeline.from_pretrained(self.__model_name, torch_dtype=torch.float16, use_safetensors=True).to(device)