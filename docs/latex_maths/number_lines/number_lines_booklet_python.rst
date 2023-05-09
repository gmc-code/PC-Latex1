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

| The Python to create a 2 page booklet of number lines worksheets, with 10 number line diagrams on one page, is below.
| The key line is: ``for i in range(1,21):``. The `21` can be replaced to produce different amount of pages. e.g. 41 for 4 pages, 101 for 10 pages.

:download:`2 page booklet python<makers/number_lines_booklet_maker.py>`

.. literalinclude:: makers/number_lines_booklet_maker.py
   :linenos:

