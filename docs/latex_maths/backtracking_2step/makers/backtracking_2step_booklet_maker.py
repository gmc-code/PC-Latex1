# 10 to page for standard and solve
# 20 to page for build
# 15 to page for inv and from exp

from pathlib import Path
import subprocess
import time
import random
import magick_pdf_to_png
import backtracking_functions as btf

currfile_dir = Path(__file__).parent
tex_template_path = currfile_dir / "backtrack_2step_booklet_template.tex"
texans_template_path = currfile_dir / "backtrack_2step_booklet_ans_template.tex"

tex_diagram_standard_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template.tex"
)
tex_diagram_buildexp_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template_1buildexp.tex"
)
tex_diagram_invop_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template_1invop.tex"
)
tex_diagram_fromexp_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template_1invop.tex"
)
tex_diagram_solvefromexp_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template.tex"
)
tex_diagram_blank_template_path = (
    currfile_dir / "backtrack_2step_booklet_diagram_template_blank.tex"
)


def convert_to_pdf(tex_path, currfile_dir, aux_path):
    """
    Converts a TeX file to PDF format using pdfLaTeX.

    Args:
        tex_path (str): The path to the TeX file.
        currfile_dir (str): The path to the directory where the TeX file is located.
        aux_path (str): The path to the directory where auxiliary files will be stored.

    Returns:
        subprocess.CompletedProcess: A subprocess.CompletedProcess object containing information about the completed process.

    Raises:
        FileNotFoundError: If the TeX file does not exist.
        subprocess.CalledProcessError: If pdfLaTeX returns a non-zero exit code.
    """
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
tex_keys_q = ["stepAB", "stepBC", "boxA", "boxCrev"]
# used by from expression
tex_keys_q_fromexp = ["boxC"]
# used by from expression
tex_keys_q_solvefromexp = ["boxC", "boxCrev"]


def num_for_type(bt_type):
    """
    1 standard, 10 per page
    2 1 row build expression, 20 to page
    3 1 row inverse operations, 15 per page
    4 1 row from expression, 15 per page
    5 solve from expression, 10 per page
    6 blank, 10 per page
    """
    '''Returns the number of pages for a given bt_type.

    Args:
        bt_type (int): An integer between 1 and 6.

    Returns:
        int: The number of pages for the given bt_type.
    '''
    match bt_type:
        case 1:
            num = 20
        case 2:
            num = 40
        case 3:
            num = 30
        case 4:
            num = 30
        case 5:
            num = 20
        case 6:
            num = 20
    return num


def make1_diagram(tex_diagram_template_txt, num1, num2, tex_keys_q):
    """
    This function takes in a LaTeX template for a diagram, two numbers `num1` and `num2`, and a list of keys `tex_keys_q`.
    
    Args:
    tex_diagram_template_txt (str): A string representing the LaTeX template for the diagram.
    num1 (int): An integer representing the first number.
    num2 (int): An integer representing the second number.
    tex_keys_q (list): A list of strings representing the keys for the diagram.
    
    Returns:
    tuple: A tuple containing two strings. The first string is the LaTeX template with the keys replaced by their corresponding values from `num1` and `num2`. The second string is the same LaTeX template with all keys replaced by their corresponding values from `num1` and `num2`.
    """

    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
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

    # return tex_diagram_template_txt
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


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
            if num1 not in [1, 2, 3, 4, 5]:
                num1 = 5  # random by default
        else:
            num1 = 5  # random by default
        #
        num2 = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process \n")
        if num2.strip().isdigit():
            num2 = int(num2)
            if num2 not in [1, 2, 3, 4, 5]:
                num2 = 5  # random by default
        else:
            num2 = 5  # random by default
        #
    else:
        # use as placeholders for sake of call below; will end up returning + + dictionary but not used.
        num1, num2 = None, None

    numq = input(
        "Enter the number of questions from 1 to 100; default to 2 pages worth \n"
    )
    if numq.strip().isdigit():
        numq = int(numq)
        if numq not in range(1, 101):
            numq = num_for_type(bt_type)
    else:
        numq = num_for_type(bt_type)

    match bt_type:
        case 1:
            tex_diagram_template_path = tex_diagram_standard_template_path
            fileprefix = "bt2Bk"
            q_parts_to_fill = tex_keys_q
        case 2:
            tex_diagram_template_path = tex_diagram_buildexp_template_path
            fileprefix = "bt2Bk_build"
            q_parts_to_fill = tex_keys_q
        case 3:
            tex_diagram_template_path = tex_diagram_invop_template_path
            fileprefix = "bt2Bk_invop"
            q_parts_to_fill = tex_keys_q
        case 4:
            tex_diagram_template_path = tex_diagram_fromexp_template_path
            fileprefix = "bt2Bk_fromexp"
            q_parts_to_fill = tex_keys_q_fromexp
        case 5:
            tex_diagram_template_path = tex_diagram_solvefromexp_template_path
            fileprefix = "bt2Bk_solvefromexp"
            q_parts_to_fill = tex_keys_q_solvefromexp
        case 6:
            tex_diagram_template_path = tex_diagram_blank_template_path
            fileprefix = "bt2Bk_blank"
            q_parts_to_fill = tex_keys_q

    #
    filename = input(
        f"Enter the base filename to be added to the prefix {fileprefix}_: \n"
    )
    if not filename:
        filename = "1"  # "bt2Bk_1_q and bt2Bk_1_ans as default file"
    #
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir / f"{fileprefix}_{filename}_q.tex"
    aux_path = currfile_dir / "temp"
    # answers
    tex_output_path_ans = currfile_dir / f"{fileprefix}_{filename}_ans.tex"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<cols>>
    # generate column text and column text for answers
    col1_text = ""
    col1_text_ans = ""
    rmax = numq + 1
    for _ in range(1, rmax):
        img_tex, img_tex_ans = make1_diagram(
            tex_diagram_template_txt, num1, num2, q_parts_to_fill
        )
        col1_text += img_tex
        col1_text_ans += img_tex_ans

    # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<cols>>", col1_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<cols>>", col1_text_ans)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    if bt_type in [1, 2, 3, 4, 5]:
        with open(tex_output_path_ans, "w") as outfile:
            outfile.write(tex_template_txt_ans)

    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path, currfile_dir, aux_path)
    if bt_type in [1, 2, 3, 4, 5]:
        convert_to_pdf(tex_output_path_ans, currfile_dir, aux_path)


if __name__ == "__main__":
    print("starting")
    main()
    print("finished")
