# from fastai.vision.all import *
from fastai.vision.all import load_learner
import gradio as gr

# nicher 3 ta line deploy er somoy deya jbe na. Only to run in gradio,localhost eta deya lgbe

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

ethnic_group_labels = (
  "Akha people",
  "Bai people",
  "Chakma people",
  "Hani people",
  "Kazakhs",
  "Lisu people",
  "Mon people",
  "Naga people",
  "Qiang people",
  "Tatar people",
  "Tripuri people",
  "Uzbeks"
)

model = load_learner('models/ethnic-group-recognizer-v4.pkl')

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(ethnic_group_labels, map(float, probs)))


image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = [
  "test_images/akha01.png",
  "test_images/akha02.png",
  "test_images/bai01.png",
  "test_images/bai02.png",
  "test_images/bai03.png",
  "test_images/chakma01.png",
  "test_images/chakma02.png",
  "test_images/chakma03.png",
  "test_images/hani01.png",
  "test_images/hani02.png",
  "test_images/hani03.png",
  "test_images/hani04.png",
  "test_images/kazaks01.png",
  "test_images/kazaks02.png",
  "test_images/kazaks03.png",
  "test_images/kazaks04.png",
  "test_images/kazaks05.png",
  "test_images/kazaks06.png",
  "test_images/lisu01.png",
  "test_images/lisu02.png",
  "test_images/lisu03.png",
  "test_images/lisu04.png",
  "test_images/lisu05.png",
  "test_images/lisu06.png",
  "test_images/mon01.png",
  "test_images/mon02.png",
  "test_images/mon03.png",
  "test_images/mon04.png",
  "test_images/naga01.png",
  "test_images/naga02.png",
  "test_images/naga03.png",
  "test_images/naga04.png",
  "test_images/naga05.png",
  "test_images/qiang01.png",
  "test_images/qiang02.png",
  "test_images/qiang03.png",
  "test_images/tatar01.png",
  "test_images/tatar02.png",
  "test_images/tatar03.png",
  "test_images/tatar04.png",
  "test_images/tatar05.png",
  "test_images/tatar06.png",
  "test_images/tripuri01.png",
  "test_images/tripuri02.png",
  "test_images/tripuri03.png",
  "test_images/uzbeks01.png",
  "test_images/uzbeks02.png",
  "test_images/uzbeks03.png",
  "test_images/uzbeks04.png",
  "test_images/uzbeks05.png",
  "test_images/uzbeks06.png"
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
# iface.launch(inline=False, share=True) # huggingface e share=True hbe na
iface.launch(inline=False)