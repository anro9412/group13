import os
os.chdir("fonts")
def read_bytes_write_to(filepath: str):
    with open(filepath, "rb") as reader:
        binary = reader.read()

    with open(filepath.replace(".bin", ".txt"), "w") as writer:
        writer.write(repr(binary))

# for filepath in os.listdir():
#     read_bytes_write_to(filepath)

read_bytes_write_to("ui_font_my_figtree_semibold_16.bin")
