from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_template.tex"
texans_template_path = currfile_dir / "backtrack_2step_template.tex"

tex_diagram_standard_template_path = (
    currfile_dir / "backtrack_2step_diagram_template.tex"
)
tex_diagram_buildexp_template_path = (
    currfile_dir / "backtrack_2step_diagram_template_1buildexp.tex"
)
tex_diagram_invop_template_path = (
    currfile_dir / "backtrack_2step_diagram_template_1invop.tex"
)
tex_diagram_fromexp_template_path = (
    currfile_dir / "backtrack_2step_diagram_template_1invop.tex"
)
tex_diagram_solvefromexp_template_path = (
    currfile_dir / "backtrack_2step_diagram_template.tex"
)
tex_diagram_blank_template_path = (
    currfile_dir / "backtrack_2step_diagram_template_blank.tex"
)


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


# % end modify values for backtracking
# tex_keys = ['stepAB','stepABrev','stepBC', 'stepBCrev', boxA','boxB', 'boxC', 'boxCrev, 'boxBrev', 'boxArev' ]
# used by standard, build expression, inverse operations
tex_keys_q = ["stepAB", "stepBC", "boxA", "boxCrev"]
# used by from expression
tex_keys_q_fromexp = ["boxC"]
# used by from expression
tex_keys_q_solvefromexp = ["boxC", "boxCrev"]


def make1_diagram(tex_diagram_template_txt, num1, num2, tex_keys_q):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    kv = btf.get_2step_process_dict(num1, num2)
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
                "<<" + key + ">>", ""
            )
    return tex_diagram_template_txt, tex_diagram_template_txt_ans


def main():
    input_str = (
        "Enter 1, 2, 3, 4, 5 or 6 for standard, 1 row build expression, "
        + "1 row inverse operations, 1 row from expression, solve from expression, blank  \n"
    )
    bt_type = input(input_str)
    if bt_type.strip().isdigit():
        bt_type = int(bt_type)
        if not bt_type in [1, 2, 3, 4, 5, 6]:
            bt_type = 1  # standard by default
    else:
        bt_type = 1  # standard by default
    #
    if bt_type in [1, 2, 3, 4, 5]:
        num1 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 1st process \n")
        if num1.strip().isdigit():
            num1 = int(num1)
            if not num1 in [1, 2, 3, 4, 5]:
                num1 = 5  # random by default
        else:
            num1 = 5  # random by default
        #
        num2 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process \n")
        if num2.strip().isdigit():
            num2 = int(num2)
            if not num2 in [1, 2, 3, 4, 5]:
                num2 = 5  # random by default
        else:
            num2 = 5  # random by default
    else:
        # use as placeholders for sake of call below; will end up returning + + dictionary but not used.
        num1, num2 = None, None

    match bt_type:
        case 1:
            tex_diagram_template_path = tex_diagram_standard_template_path
            fileprefix = "bt2"
            q_parts_to_fill = tex_keys_q
        case 2:
            tex_diagram_template_path = tex_diagram_buildexp_template_path
            fileprefix = "bt2_build"
            q_parts_to_fill = tex_keys_q
        case 3:
            tex_diagram_template_path = tex_diagram_invop_template_path
            fileprefix = "bt2_invop"
            q_parts_to_fill = tex_keys_q
        case 4:
            tex_diagram_template_path = tex_diagram_fromexp_template_path
            fileprefix = "bt2_fromexp"
            q_parts_to_fill = tex_keys_q_fromexp
        case 5:
            tex_diagram_template_path = tex_diagram_solvefromexp_template_path
            fileprefix = "bt2_solvefromexp"
            q_parts_to_fill = tex_keys_q_solvefromexp
        case 6:
            tex_diagram_template_path = tex_diagram_blank_template_path
            fileprefix = "bt2_blank"
            q_parts_to_fill = tex_keys_q
    #
    filename = input(
        f"Enter the base filename to be added to the prefix {fileprefix}_: \n"
    )
    if not filename:
        filename = "1"  # "bt2_1_q and bt2_1_ans as default file"
    #
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"{fileprefix}_{filename}_q.tex"
    pdf_path = currfile_dir / f"{fileprefix}_{filename}_q.pdf"
    png_path = currfile_dir / f"{fileprefix}_{filename}_q.png"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"{fileprefix}_{filename}_ans.tex"
    pdf_path_ans = currfile_dir / f"{fileprefix}_{filename}_ans.pdf"
    png_path_ans = currfile_dir / f"{fileprefix}_{filename}_ans.png"

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
    diagram_text, diagram_text_ans = make1_diagram(
        tex_diagram_template_txt, num1, num2, q_parts_to_fill
    )
    # Replace the <<diagram>> placeholder in the LaTeX template
    tex_template_txt = tex_template_txt.replace("<<diagram>>", diagram_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<diagram>>", diagram_text_ans)
    # Write the question diagram tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)
    # Write the answer diagram tex to an output file
    if bt_type in [1, 2, 3, 4, 5]:
        with open(tex_output_path_ans, "w") as outfile:
            outfile.write(tex_template_txt_ans)

    # Wait for the files to be created
    time.sleep(1)
    # convert to pdf
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    if bt_type in [1, 2, 3, 4, 5]:
        convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)

    # Wait for the files to be created
    time.sleep(1)
    # convert to png
    magick_pdf_to_png.convert_pdf_to_png(pdf_path, png_path)
    if bt_type in [1, 2, 3, 4, 5]:
        magick_pdf_to_png.convert_pdf_to_png(pdf_path_ans, png_path_ans)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
