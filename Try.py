from PIL import Image

try: 
    im = Image.open ("args.input_file")
except FileNotFoundError: 
    print ("Archivo de entrada no encontrado, introduce el nombre del archivo correcto")

    