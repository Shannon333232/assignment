from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = input("type your input prompt here")

image = pipe(prompt + "red circle").images[0]

image.save("image.png")