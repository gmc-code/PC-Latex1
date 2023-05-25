from pathlib import Path
import magick_pdf_to_png
import wand_pdf_to_png

# paste in windows path to the raw string
raw_string =  r'C:\PC_RTD_GITHUB\PC_latex\docs\latex_science\chemistry\files\bohr.pdf'

forward_slash_string = raw_string.replace('\\', '/')
pdf_file_path = Path(forward_slash_string)
# parent_folder = pdf_file_path.parent
# file_path_without_extension = parent_folder / pdf_file_path.stem

# magick_pdf_to_png.pdf_to_png(pdf_file_path)

wand_pdf_to_png.pdf_to_png(pdf_file_path)