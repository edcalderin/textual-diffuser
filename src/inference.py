import time

import torch
from diffusers import StableDiffusionPipeline
from PIL import Image


class Inference:
    def __init__(self, repo_id: str = "nota-ai/bk-sdm-small") -> None:
        self.__repo_id: str = repo_id

    def text2image(self, prompt: str) -> tuple[Image, float]:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        pipe = StableDiffusionPipeline.from_pretrained(
            self.__repo_id, torch_dtype=torch.float16, use_safetensors=True
        ).to(device)
        pipe.enable_attention_slicing()
        start: float = time.time()
        image = pipe(prompt).images[0]
        end: float = time.time()
        duration: float = end - start
        return image, duration
