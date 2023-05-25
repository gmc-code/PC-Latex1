====================================================
Circuits LaTeX
====================================================

| See https://www.youtube.com/watch?v=WRTELZP1l0Y


.. code-block:: LaTeX

   \documentclass{article}
   \usepackage{tikz}
   \usepackage{circuitikz}

   \begin{document}
   \begin{figure} [h!]
   \begin{center}
   \begin{circuitikz}
   \draw (0,0) to[battery={$12V$}] (0,2) % The voltage source
   to[short] (2,2)
   to[bulb, l=$3\Omega$] (2,0) % The bulb
   to[short] (0,0);
   \end{circuitikz}
   \caption{My first circuit.}
   \end{center}
   \end{figure}
   \end{document}

