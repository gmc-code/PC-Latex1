====================================================
Long division
====================================================

| Decimal arithmetic using vertically aligned decimal places is attempted heere for hte production of randomly generated worksheets.

----

Example  diagram
-------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<manual/decimals_mq.png>`
      :download:`pdf<manual/decimals_mq.pdf>`
      :download:`tex<manual/decimals_mq.tex>`


      .. figure:: manual/decimals_mq.png
         :width: 300
         :alt: decimals_q
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<manual/decimals_mans.png>`
      :download:`pdf<manual/decimals_mans.pdf>`
      :download:`tex<manual/decimals_mans.tex>`

      .. figure:: manual/decimals_mans.png
         :width: 300
         :alt: decimals_ans
         :figclass: align-center
    
----

Approach
----------

#. Decimals diagrams for subtraction and addition will be designed in LaTeX.
#. The LaTeX file will be broken into parts and placeholder text wil be inserted.
#. Python will replace the placeholder text in the backtracking LaTeX, allowing random numbers to be used.
#. Python will be used to generate a worksheet with 10 diagrams that are all randomly generated.
#. Both a question sheet and an answer sheet will be built in LaTeX and then converted to a pdf and png of each.
#. Then a 2 page booklet will be made with answers as well.

| For use of python to build LaTeX files see:
| https://tug.org/tug2019/slides/slides-ziegenhagen-python.pdf

