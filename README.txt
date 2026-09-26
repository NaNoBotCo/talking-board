==============================================================================
TALKING BOARD · กระดานวิญญาณ
==============================================================================


A parlour talking board. Up to six other hands rest on the planchette; bots
take the empty seats. A lens rides the planchette, the board reads your grip,
and a notebook writes down what comes through, with a reading of the nearest
words. English and Thai boards. For entertainment.

Live: https://nanobotco.github.io/talking-board/ (GitHub Pages, main /docs)

In the Claude artifact edition, people who have the page open at the same time
sit in, and their fingers pull on each other's planchettes. One seat stays a
bot. The GitHub Pages edition seats bots only.


RUN
------------------------------------------------------------------------------


      python3 tools/build.py          # index.html → docs/
      python3 tools/build.py --card   # also photographs docs/card.png (Chrome)


FILES
------------------------------------------------------------------------------


      index.html     the page (also the artifact source)
      docs/          what GitHub Pages serves
      tools/build.py


LICENCE
------------------------------------------------------------------------------


      Code: MIT (LICENSE-CODE). Page text and card: CC BY 4.0 (LICENSE).
