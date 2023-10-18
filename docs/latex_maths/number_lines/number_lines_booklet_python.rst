====================================================
Number Lines booklet python
====================================================

The python below requires 3 .tex files:

#. number_lines_booklet_template.tex
#. number_lines_booklet_ans_template.tex
#. number_lines_worksheet_diagram_template.tex

| :download:`number_lines_booklet_template<makers/number_lines_booklet_template.tex>`
| :download:`number_lines_booklet_ans_template<makers/number_lines_booklet_ans_template.tex>`
| :download:`number_lines_worksheet_diagram_template<makers/number_lines_worksheet_diagram_template.tex>`


Python to create a 2 page booklet of number lines worksheets
------------------------------------------------------------

| The python file, **number_lines_booklet_maker.py**, when run, will ask for these inputs:
| Choose the arithmetic process: ``"Enter 1,2,3,4,5 or 6 for plus,minus_neg,minus,minus_pos,plus_neg,random"``.
| Choose the number of questions from 1 to 100: ``"Enter the number of questions from 1 to 80"``
| Choose the file name base: ``""Enter the base filename to be added to the prefix nlBk:"``.
| The filename will have "_q" added for the question booklet and "_ans" for the answer booklet.


:download:`number_lines_booklet_maker<makers/number_lines_booklet_maker.py>`

.. literalinclude:: makers/number_lines_booklet_maker.py
   :linenos:

