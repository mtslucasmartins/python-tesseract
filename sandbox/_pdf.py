from wand.image import Image

input_path = "UNIPRIME.pdf"
output_name = "name_of_outfile_{index}.png"
source = Image(filename=input_path, resolution=300, width=2200)
images = source.sequence
for i in range(len(images)):
    Image(images[0]).save(filename=output_name.format(i))