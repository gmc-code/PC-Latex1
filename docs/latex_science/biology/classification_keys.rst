====================================================
Classification keys
====================================================


Tabular keys
---------------------

| Dichotomous tabular classification keys can be created in LaTeX using the tabular environment.

.. figure:: files/vertebrates_key.png
   :width: 300
   :alt: vertebrates_key.png
   :figclass: align-center


.. literalinclude:: files/vertebrates_key.tex
   :linenos:

| LaTeX usage:

- `\documentclass[12pt, varwidth, border=5mm]{standalone}`: This line specifies the document class and its options. The `standalone` class is used for creating a standalone document with a single page. The `12pt` option sets the font size to 12 points. The `varwidth` option allows the content to determine the width of the page. The `border=5mm` option adds a 5mm border around the content.

- `\begin{tabular}{l@{\hspace{1mm}}p{6cm}@{}r}`: This line begins a `tabular` environment, which is used to create a table. The argument `{l@{\hspace{1mm}}p{6cm}@{}r}` specifies the alignment and spacing of the columns. The `l` means that the first column is left-aligned. The `@{\hspace{1mm}}` syntax adds a 1mm space between the first and second columns. The `p{6cm}` means that the second column is a paragraph column with a fixed width of 6cm. The `@{}` syntax removes the space between the second and third columns. The `r` means that the third column is right-aligned.

- `1A. & Feathers present \dotfill &\dotfill birds \\`: This line represents a row in the table. The `&` symbol separates the columns and the `\\` symbol marks the end of the row. The `\dotfill` command fills the space with dots.


----

.. figure:: files/arthropods_key.png
   :width: 600
   :alt: arthropods_key.png
   :figclass: align-center


.. literalinclude:: files/arthropods_key.tex
   :linenos:

| LaTeX usage:

- `\documentclass[12pt, varwidth, border=5mm]{standalone}`: This line specifies the document class and its options. The `standalone` class is used for creating a standalone document with a single page. The `12pt` option sets the font size to 12 points. The `varwidth` option allows the content to determine the width of the page. The `border=5mm` option adds a 5mm border around the content.

- `\begin{tabular}{l@{\hspace{1mm}}r}`: This line begins a `tabular` environment, which is used to create a table. The argument `{l@{\hspace{1mm}}r}` specifies the alignment and spacing of the columns. The `l` means that the first column is left-aligned. The `@{\hspace{1mm}}` syntax adds a 1mm space between the first and second columns. The `r` means that the second column is right-aligned.

- `1a. & Legs on every segment except head and last segment \dots \dotfill go to 2 \\`: This line represents a row in the table. The `&` symbol separates the columns and the `\\` symbol marks the end of the row. The `\dots` command produces an ellipsis (three dots). The `\dotfill` command fills the space with dots.

----

Branching keys
---------------------

| The qtree package can be used to draw branching diagrams.
| See docs at: https://mirror.cse.unsw.edu.au/pub/CTAN/macros/latex/contrib/qtree/qtreenotes.pdf


.. figure:: files/vertebrates_branching_key.png
   :width: 600
   :alt: vertebrates_branching_key.png
   :figclass: align-center


.. literalinclude:: files/vertebrates_branching_key.tex
   :linenos:

| LaTeX usage:

- `\documentclass[12pt, varwidth, border=5mm]{standalone}`: This line specifies the document class and its options. The `standalone` class is used for creating a standalone document with a single page. The `12pt` option sets the font size to 12 points. The `varwidth` option allows the content to determine the width of the page. The `border=5mm` option adds a 5mm border around the content.

- `\usepackage{qtree}`: This line loads the `qtree` package, which provides macros for drawing tree diagrams.

- `\usepackage{graphicx}`: This line loads the `graphicx` package, which provides scalebox.

- `\scalebox{0.7}{`: This line begins a `scalebox` environment, which scales its content by a specified factor. In this case, the content is scaled by a factor of 0.7 (i.e., it is reduced to 70% of its original size).

- `\Tree [.Vertebrates [.1A [.{Feathers present} birds ] ] [.1B [.{Feathers absent} [.2 [.2A [.{Scales present} [.3 [.3A [.{Breathe with gills} fish ] ] [.3B [.{Breathe with lungs} reptiles ] ] ] ] ] [.2B [.{No scales present} [.4 [.4A [.{Hair or fur present} mammals ] ] [.4B [.{Hair or fur absent} amphibians ] ] ] ] ] ] ] ]`: This line uses the `\Tree` command from the `qtree` package to draw a tree diagram. The tree is specified using bracket notation, where each pair of square brackets encloses a node and its children. Text inside curly braces is typeset as a label on the corresponding node.

- `}`: This line marks the end of the `scalebox` environment.

- Here's an example: ``\Tree [.A [.B C D ] [.E F ] ]``. This code produces a tree with three levels. The root node is labeled `A` and has two children: `B` and `E`. The node labeled `B` has two children: `C` and `D`. The node labeled `E` has one child: `F`. The tree is drawn using the following rules:
- Each level of the tree is drawn on a separate line.
- Sibling nodes are separated by a horizontal space.
- Parent and child nodes are connected by a vertical line.
