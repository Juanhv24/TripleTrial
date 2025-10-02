from PIL import Image 
import argparse 

parser = argparse.ArgumentParser() 

parser.add_argument ("input_file")
parser.add_argument ("output_file")
parser.add_argument ("angle", type=int)
parser.add_argument ("-i", "--info", action="store_true")
args = parser.parse_args()

angle = args.angle

try: 
    im = Image.open (args.input_file)
except FileNotFoundError: 
    print ("Archivo de entrada no encontrado, introduce el nombre del archivo correcto")

else: 
    rotated = im.rotate (angle)
    im.close ()
    rotated.save (args.output_file)
    print ("Ejecución fluida")

if args.info: 
    print ("Dimensiones de la imagen de entrada:", im.size)
