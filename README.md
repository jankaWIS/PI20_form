# PI20 form

This repo implements the PI20 questionnaire from the following open source publication:

The 20-item prosopagnosia index (PI20): a self-report instrument for identifying developmental prosopagnosia

Punit Shah, Anne Gaule, Sophie Sowden, Geoffrey Bird and Richard Cook

Published: 01 June 2015, 
DOI: https://doi.org/10.1098/rsos.140343, url: https://royalsocietypublishing.org/doi/10.1098/rsos.140343#d3e498

## Code
There is a python code `pi20_create_html.py` which can be used to produce an HTML file (in the current setup it produces the `pi20.html` file which can be previewed from this repo as well) and can be customised. 

There is also a json file `pi20_form.json` which is an implementation of this questionnaire in [lab.js](lab.js) and can be previewed using the https://labjs.felixhenninger.com/ tool (Builder).

## Questions
All questions are taken from the paper (Table 1), the list of them as appears in the paper without the ratings is saved in `pi20_table1.csv`.

#### Updates
Last updated 20. 1. 2022.


#### License
The original paper has the following license:

```
© 2015 The Authors. Published by the Royal Society under the terms of the Creative Commons Attribution License http://creativecommons.org/licenses/by/4.0/, which permits unrestricted use, provided the original author and source are credited.
```

The code follows the BSD 3-Clause License.