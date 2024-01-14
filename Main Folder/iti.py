import base64
import os
import requests

response = requests.post(
    "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer sk-MfFg3aPdFAjOnjkYgbdASZneSuw91GAO1onitYUCkD1G6Lt8"
    },
    files={
        #"init_image": open("./saved_img.jpg", "rb")
        "init_image": "./saved_img.jpeg"
          },
    data={
        "init_image_mode": "IMAGE_STRENGTH",
		"image_strength": 0.75,
		"steps": 40,
		"seed": 0,
		"cfg_scale": 5,
		"samples": 1,
		"text_prompts[0][text]": 'Make the sweater blue',
		"text_prompts[0][weight]": 1,
		"text_prompts[1][text]": 'blurry, bad',
		"text_prompts[1][weight]": -1,
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# make sure the out directory exists
if not os.path.exists("./out"):
    os.makedirs("./out")

for i, image in enumerate(data["artifacts"]):
    with open(f'./out/img2img_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))