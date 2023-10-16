from pathlib import Path
import subprocess
import time
import decimals_functions as decf
import magick_pdf_to_png


currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "add_sub_decimals_template.tex"
texans_template_path = currfile_dir / "add_sub_decimals_template.tex"
tex_diagram_template_path = currfile_dir / "add_sub_decimals_diagram_template.tex"


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


# tex_keys = ["num1", "num2", "process"]
tex_keys_q = ["answer"]


def make1_diagram(tex_diagram_template_txt, nump, numip, numdp):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = decf.get_add_sub_dec_dict(nump, numip, numdp)

    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )

    for key, value in kv.items():
        if key in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", ""
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )
    tex_diagram_template_txt = tex_diagram_template_txt.replace("<<numip>>", str(numip))
    tex_diagram_template_txt = tex_diagram_template_txt.replace("<<numdp>>", str(numdp))
    tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<numip>>", str(numip))
    tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace("<<numdp>>", str(numdp))
    # return tex_diagram_template_txt
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    nump = input("Enter 1, 2, or 3 for +, -, random for the process \n")
    if nump.strip().isdigit():
        nump = int(nump)
        if not nump in [1, 2, 3]:
            nump = 3  # random by default
    else:
        nump = 3  # random by default
    #
    numip = input("Enter 1, 2, 3, or 4 for the number of places before the decimal point \n")
    if numip.strip().isdigit():
        numip = int(numip)
        if not numip in [1, 2, 3, 4, 5]:
            numip = 1  # 1 by default
    else:
        numip = 1  # 1 by default
    #
    numdp = input("Enter 1, 2, 3, 4, or 5 for the number of decimal places \n")
    if numdp.strip().isdigit():
        numdp = int(numdp)
        if not numdp in [1, 2, 3, 4, 5]:
            numdp = 1  # 1 by default
    else:
        numdp = 1  # 1 by default
    #
    filename = input("Enter the base filename to be added to the prefix asd_: \n")
    if not filename:
        filename = "1"  # "asd_1_q and asd_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"asd_{filename}_q.tex"
    pdf_path = currfile_dir / f"asd_{filename}_q.pdf"
    png_path = currfile_dir / f"asd_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"asd_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"asd_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"asd_{filename}_ans.png"


    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # Generate the <<diagram>> replacement tex
    diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt, nump, numip, numdp)
    # Replace the <<diagram>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagram>>", diagram_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagram>>", diagram_text_ans)
    # Write the question diagram tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)
    # Write the answer diagram tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # convert to pdf
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # convert to png
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
