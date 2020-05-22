# MATHLA
> A robust framework for HLA-peptide binding pre-diction integrating bidirectional LSTM and multiple head attention mechanism.

## Requirements
* Python 3.7
* PyTorch 0.4.1
* Linux

Nvidia GPU and Cuda 9.2 toolkit are recommended for increasing training and testing speed.

## How to predict
>  Run the code from the source code
1.  Clone This Project
    Use Git or checkout with SVN using the web URL, or you can download the zip file in the home page of MATHLA.
    ```
    https://github.com/MATHLAtools/MATHLA.git
    ```
2. Run MATHLA.py
    ```
    python ./MATHLA.py [-m test [-te [the path to test files] -md [the path to model file] -o [the path to prediction results]]
    ```
The example of prediction results are shown in the table below:
| allele | peptide | prediction scores | label |
| --- | --- | --- | --- |
| HLAA0202 | ALFKAWAL | 9.284920692443848 | 1 |
|HLAA0202 | MDACGEANN | 32221.21875 | 50000.0|
| ... | ... | ... | ... |

Prediction scores range from 0 to 50000. Higher scores indicate lower binding affinities. Peptides with scores below 500 can be considered to be strong binders. However, the specific threshold for classification might vary in different experimental setups.

## How to Train a new Model
In order to build your own model using new training data, run MATHLA.py using the following command:

```
python ./MATHLA.py -m train [-tr [the path to training file] -md [the path to model file]]
```
The framework will train a new model by using the Training Data.

## The description of command line parameter 
| short name | full name | help | default |
| --- | --- | --- | --- |
| -m | --mode | Select train or test mode | test |
|-te | --testsetdir | The path to test files | data/TestingData/ |
|-tr | --trainsetdir | The path to training file |  |
|-o | --output | Save prediction results to this folder | Output |
|-md | --modeldir | Save model to this folder | data |
|-h | --help | Show the help message and exit |  |
