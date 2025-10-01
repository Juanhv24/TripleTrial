from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument ("input_file")
parser.add_argument ("width", type=int)
parser.add_argument ("height", type=int)
parser.add_argument ("output_file")
args = parser.parse_args()

im = Image.open (args.input_file)
new_size = (args.width, args.height)
resized = im.resize (new_size)
resized.save (args.outout_file)
im.close ()