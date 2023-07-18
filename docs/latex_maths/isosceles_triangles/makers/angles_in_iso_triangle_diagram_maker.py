from pathlib import Path
import subprocess
import time
import magick_pdf_to_png
import angles_in_iso_triangle_functions as aitf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "angles_in_iso_triangle_template.tex"
texans_template_path = currfile_dir / "angles_in_iso_triangle_template.tex"
tex_diagram_template_path = currfile_dir / "angles_in_iso_triangle_diagram_template.tex"


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


# % end modify values for angles in triangle 
# tex_keys_q = ['angleCalcAValue', 'angleCalcBValue', 'angleCalcCValue', 'angleCalcBCValue']
tex_keys_q = ['angleAValue', 'angleBValue', 'angleCValue', 'angleABValue', 
              'sideCValue', 'rotationAngleValue', 'angleALabel','angleBLabel', 'angleCLabel']



def make1_diagram(tex_diagram_template_txt,):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = aitf.get_angles_in_iso_triangle_dict()
    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )
    for key, value in kv.items():
        if key in tex_keys_q:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", "\dotuline{~~~~~~~}"  # non breaking spaces for gaps
            )
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    filename = input("Enter the base filename to be added to the prefix angles_in_iso_triangle_: \n")
    if not filename:
        filename = "1"  # "angles_in_iso_triangle_1_q and angles_in_iso_triangle_1_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"angles_in_iso_triangle_{filename}_q.tex"
    pdf_path = currfile_dir / f"angles_in_iso_triangle_{filename}_q.pdf"
    png_path = currfile_dir / f"angles_in_iso_triangle_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"angles_in_iso_triangle_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"angles_in_iso_triangle_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"angles_in_iso_triangle_{filename}_ans.png"

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
    diagram_text, diagram_text_ans = make1_diagram(tex_diagram_template_txt)
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
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    # magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
