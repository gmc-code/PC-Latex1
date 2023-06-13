====================================================
Decimals diagram - manual
====================================================

| The LaTeX in this section is for a diagram for addition or subtraction of decimals.
| The values in the diagram can be entered manually into the LaTeX code.
| The snippet below from the LaTeX file shows a block in the preamble of the .tex file where the values for the backtacking diagram can be manually edited.

| The values in the braces, {}, can be manually set with up to 2 digits before the decimal point and up to 3 after it.
| The processes, ``\addsub`` can be ``+`` or ``-``.

.. code-block:: LaTeX

   % modify values 
   \def\addsub{-} 
   \def\deca{70.256}
   \def\decb{16.362}
   \def\answer{53.894}

| The line ``\begin{tabular}{d{2.3}}`` sets the spacing for up to 2 digits before and 3 digits after the decimal point.
| If more digits are required then the ``2`` and the ``3`` can be changed to suit.
| It uses the macro: ``\newcolumntype{d}[1]{D{.}{.}{#1}}`` which sets the decimal alignment and spacing.

----

A decimals diagram with answers
--------------------------------------------

.. grid:: 2
   :gutter: 0
   :margin: 0
   :padding: 0

   .. grid-item-card::  

      question
      ^^^
      :download:`png<manual/decimal_mq.png>`
      :download:`pdf<manual/decimal_mq.pdf>`
      :download:`tex<manual/decimal_mq.tex>`


      .. figure:: manual/decimal_mq.png
         :width: 300
         :alt: decimal_mq
         :figclass: align-center

   .. grid-item-card::  
      
      answer
      ^^^
      :download:`png<manual/decimal_mans.png>`
      :download:`pdf<manual/decimal_mans.pdf>`
      :download:`tex<manual/decimal_mans.tex>`

      .. figure:: manual/decimal_mans.png
         :width: 300
         :alt: decimal_mans
         :figclass: align-center

----

A decimals diagram LaTeX
------------------------------

| The manual question:

.. literalinclude:: manual/decimal_mq.tex
   :linenos:

| The manual answer:

.. literalinclude:: manual/decimal_mans.tex
   :linenos:


