====================================================
Backtracking 2 step diagrams
====================================================

| The python file to make a 2-step backtracking diagram is below.
| :download:`backtracking_2step_diagram_maker.py<makers/backtracking_2step_diagram_maker.py>`

| The required LaTeX files are below.
| :download:`backtrack_2step_template.tex<makers/backtrack_2step_template.tex>`
| :download:`backtrack_2step_diagram_template.tex<makers/backtrack_2step_diagram_template.tex>`
| :download:`backtrack_2step_diagram_template.tex<makers/backtrack_2step_diagram_template_1buildexp.tex>`
| :download:`backtrack_2step_diagram_template.tex<makers/backtrack_2step_diagram_template_1invop.tex>`
| :download:`backtrack_2step_diagram_template.tex<makers/backtrack_2step_diagram_template_blank.tex>`

| The 2 custom python modules required are:
| :download:`backtracking_functions.py<makers/backtracking_functions.py>`
| :download:`magick_pdf_to_png.py<makers/magick_pdf_to_png.py>`

| The python file, **backtracking_2step_diagram_maker.py**, when run, will ask for 3 inputs:
| Choose the type of diagrams: 
| ``"Enter 1, 2, 3, 4, 5 or 6 for standard, 1 row build expression, 1 row inverse operations, 1 row from expression, solve from expression, blank "``
| Choose the first arithmetic process: 
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 1st process"``
| Choose the second arithmetic process: 
| ``"Enter 1, 2, 3, 4 or 5 for +, -, X, /, random for 2nd process"``
| Choose the file name base: 
| ``"Enter the base filename to be added to the prefix :"``
| The prefix will be "bt2" for standard; "bt2_build" for 1 row build expression; or "bt2_invop" for 1 row inverse operations.
| The prefix will be "bt2_fromexp" for 1 row from expression; "bt2_solvefromexp" for solve from expression; or "bt2_blank" for blank.
| The filename will have "_q" added for the question diagram and "_ans" for the answer diagram.

----

Example 2-step backtracking diagram
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<diagrams/bt2_x+_q.png>`
      :download:`pdf<diagrams/bt2_x+_q.pdf>`
      :download:`tex<diagrams/bt2_x+_q.tex>`


      .. figure:: diagrams/bt2_x+_q.png
         :width: 300
         :alt: bt2_x+_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<diagrams/bt2_x+_ans.png>`
      :download:`pdf<diagrams/bt2_x+_ans.pdf>`
      :download:`tex<diagrams/bt2_x+_ans.tex>`

      .. figure:: diagrams/bt2_x+_ans.png
         :width: 300
         :alt: bt2_x+_ans
         :figclass: align-center

----

Example 2-step backtracking diagram: 1 row; building the expression
----------------------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<diagrams/bt2_build_x+_q.png>`
      :download:`pdf<diagrams/bt2_build_x+_q.pdf>`
      :download:`tex<diagrams/bt2_build_x+_q.tex>`


      .. figure:: diagrams/bt2_build_x+_q.png
         :width: 300
         :alt: bt2_build_x+_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<diagrams/bt2_build_x+_ans.png>`
      :download:`pdf<diagrams/bt2_build_x+_ans.pdf>`
      :download:`tex<diagrams/bt2_build_x+_ans.tex>`

      .. figure:: diagrams/bt2_build_x+_ans.png
         :width: 300
         :alt: bt2_build_x+_ans
         :figclass: align-center

----

Example 2-step backtracking diagram: 1 row; inverse operations
----------------------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<diagrams/bt2_invop_x+_q.png>`
      :download:`pdf<diagrams/bt2_invop_x+_q.pdf>`
      :download:`tex<diagrams/bt2_invop_x+_q.tex>`


      .. figure:: diagrams/bt2_invop_x+_q.png
         :width: 300
         :alt: bt2_invop_x+_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<diagrams/bt2_invop_x+_ans.png>`
      :download:`pdf<diagrams/bt2_invop_x+_ans.pdf>`
      :download:`tex<diagrams/bt2_invop_x+_ans.tex>`

      .. figure:: diagrams/bt2_invop_x+_ans.png
         :width: 300
         :alt: bt2_invop_x+_ans
         :figclass: align-center

----

Example 2-step backtracking diagram: 1 row; from the expression
----------------------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<diagrams/bt2_fromexp_x+_q.png>`
      :download:`pdf<diagrams/bt2_fromexp_x+_q.pdf>`
      :download:`tex<diagrams/bt2_fromexp_x+_q.tex>`


      .. figure:: diagrams/bt2_fromexp_x+_q.png
         :width: 300
         :alt: bt2_fromexp_x+_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<diagrams/bt2_fromexp_x+_ans.png>`
      :download:`pdf<diagrams/bt2_fromexp_x+_ans.pdf>`
      :download:`tex<diagrams/bt2_fromexp_x+_ans.tex>`

      .. figure:: diagrams/bt2_fromexp_x+_ans.png
         :width: 300
         :alt: bt2_fromexp_x+_ans
         :figclass: align-center

----

Example 2-step backtracking diagram: solve from the expression
----------------------------------------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<diagrams/bt2_solvefromexp_x+_q.png>`
      :download:`pdf<diagrams/bt2_solvefromexp_x+_q.pdf>`
      :download:`tex<diagrams/bt2_solvefromexp_x+_q.tex>`


      .. figure:: diagrams/bt2_solvefromexp_x+_q.png
         :width: 300
         :alt: bt2_solvefromexp_x+_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<diagrams/bt2_solvefromexp_x+_ans.png>`
      :download:`pdf<diagrams/bt2_solvefromexp_x+_ans.pdf>`
      :download:`tex<diagrams/bt2_solvefromexp_x+_ans.tex>`

      .. figure:: diagrams/bt2_solvefromexp_x+_ans.png
         :width: 300
         :alt: bt2_solvefromexp_x+_ans
         :figclass: align-center

----

Example 2-step backtracking diagram: blank
----------------------------------------------------------------------------

.. grid:: 1
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      blank
      ^^^
      :download:`png<diagrams/bt2_blank.png>`
      :download:`pdf<diagrams/bt2_blank.pdf>`
      :download:`tex<diagrams/bt2_blank.tex>`


      .. figure:: diagrams/bt2_blank.png
         :width: 300
         :alt: bt2_blank
         :figclass: align-center

