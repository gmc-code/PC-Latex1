====================================================
Backtracking 1-step booklet python
====================================================

| The python below requires the following .tex files:
| :download:`backtrack_1step_booklet_template.tex<makers/backtrack_1step_booklet_template.tex>`
| :download:`backtrack_1step_booklet_ans_template.tex<makers/backtrack_1step_booklet_ans_template.tex>`
| :download:`backtrack_1step_worksheet_diagram_template.tex<makers/backtrack_1step_worksheet_diagram_template.tex>`

| The 2 custom python modules required are:
| :download:`backtracking_functions.py<makers/backtracking_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The Python to create a 2 page booklet of 1-step backtracking worksheets, with 10 backtracking diagrams per page, is below.
| :download:`backtracking_1step_booklet_maker.py<makers/backtracking_1step_booklet_maker.py>`

| The key line is: ``for i in range(1,21):``. The `21` can be replaced to produce different amount of pages. e.g. 41 for 4 pages, 101 for 10 pages.

.. literalinclude:: makers/backtracking_1step_booklet_maker.py
   :linenos:

