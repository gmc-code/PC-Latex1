from pathlib import Path
import subprocess
from tkinter import filedialog
import time
import magick_pdf_to_png
from math import floor, log10

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "stem_and_leaf_template.tex"


def convert_to_pdf(tex_path, currfile_dir, aux_path):
    result = subprocess.run(
        [
            "pdfLaTeX",
            tex_path,
            "-output-directory",
            currfile_dir,
            "-aux-directory",
            aux_path,
        ],
        stdout=subprocess.PIPE,
    )


def get_list_from_str(data_string):
    if ", " in data_string:
        data_list = data_string.split(", ")
    elif "," in data_string:
        data_list = data_string.split(",")
    else:
        data_list = data_string.split(" ")
    return data_list


def get_list_nums_from_str(num_string_list):
    have_dec = any("." in s for s in num_string_list)
    if have_dec:
        num_list = [float(n) for n in num_string_list]
    else:
        num_list = [int(n) for n in num_string_list]
    return num_list


def stemplotdata(main_title, data, interval, multiplier, max_decimal_places):
    d = []
    for val in sorted(data):
        val = int(floor(val))
        stm, lf = divmod(val, interval)
        d.append((int(stm), int(lf)))
    stems, leafs = list(zip(*d))
    laststemused = min(stems) - 1
    data = ""
    for s, l in d:
        # first time with new stem
        if laststemused < s:
            laststemused += 1
            data += f"\\\\ \n{s} & {l}"
        else:
            # jsut add leaf with same stem
            data += f" {l}"
    data += f"\\\\"
    #
    stem1, leaf1 = d[0]
    key_value = int(str(stem1) + str(leaf1))
    if multiplier == 1:
        real_key_value = key_value
    else:
        real_key_value = round(key_value / multiplier, max_decimal_places)

    title_and_key = (
        f"{main_title} \\\\ Key: {stem1} $\\vert$ {leaf1} = {real_key_value}"
    )
    return title_and_key, data[4:]


def get_file_data(filename):
    # open the text file and read the numbers
    with open(filename) as f:
        # read the first line and store it in a variable
        main_title = f.readline().strip()
        # read the second line and store it in a variable
        numbers_string = f.readline().strip()
        numbers_list = get_list_from_str(numbers_string)
        numbers_list = get_list_nums_from_str(numbers_list)
        # get rid of decimals by * by power of 10
        max_decimal_places = max(
            len(str(x).split(".")[1]) if "." in str(x) else 0 for x in numbers_list
        )
        multiplier = 10**max_decimal_places
        new_numbers_list = [int(x * multiplier) for x in numbers_list]
        # get interval based on no of digits
        interval_multiplier = max(len(str(x)) for x in new_numbers_list) - 1
        interval = 10**interval_multiplier
        # only want 1 in the leaf
        if interval > 10:
            interval = 10
        title_and_key, data = stemplotdata(
            main_title, new_numbers_list, interval, multiplier, max_decimal_places
        )
    return title_and_key, data


def main():
    data_filename = filedialog.askopenfilename(initialdir=Path(currfile_dir))
    if data_filename == "":
        print("Exited, by clicking Cancel")
        return
    title_and_key, data = get_file_data(data_filename)
    # print(plot_title, numbers_string, numbers_labels, numbers_loop_max)

    # Create a Path object from the file path
    path_obj = Path(data_filename)

    # Get the file name from the Path object using the name attribute
    filename = path_obj.stem
    # filename = input("Enter the base filename to be added to the prefix dp_: \n")
    # if not filename:
    #     filename = "dp_1st"
    # set names of files that are made
    tex_output_path = currfile_dir / f"{filename}.tex"
    pdf_path = currfile_dir / f"{filename}.pdf"
    png_path = currfile_dir / f"{filename}.png"
    aux_path = currfile_dir / "temp"
    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()

    # Replace the placeholders in the LaTeX template

    tex_template_txt = tex_template_txt.replace("<<title_and_key>>", title_and_key)
    tex_template_txt = tex_template_txt.replace("<<data>>", data)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # Convert the PDFs to PNGs
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
