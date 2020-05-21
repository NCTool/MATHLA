import os
import warnings
import torch

from MATHLA import getParm, Mid, getParser

warnings.filterwarnings("ignore")
seed = 1
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.enabled = True
torch.backends.cudnn.deterministic = True


def main(args):
    parms_Net = getParm("./", args)
    model_name = "model_weight"
    parms_Net['model_name'] = model_name
    if parms_Net['isTotalTrain'] is True:
        Mid(parms_Net)
    else:
        files = os.listdir(parms_Net['TESTSET'])
        for file in files:
            print(file)
            model_name = "model_weight"
            parms_Net['model_name'] = model_name
            parms_Net['file_name'] = file
            Mid(parms_Net)


if __name__ == "__main__":
    args = getParser()
    main(args)
