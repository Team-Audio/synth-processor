from tqdm import tqdm
import numpy as np

from pstep_base import SymmetricPipelineStepBase


class Labeler(SymmetricPipelineStepBase):
    def __init__(self, outname='out'):
        self.outname = outname
        self.fnames = []

    def take_pipeline(self, value):
        for i, ((accords, _),) in enumerate(tqdm(value, desc='Creating Labels')):
            np.save(f"{self.outname}{i}.labels", np.array(accords))
            self.fnames += [f"{self.outname}{i}.labels.npy"]

    def has_value(self) -> bool:
        return len(self.fnames) > 0

    def pop(self):
        return self.fnames.pop(0)
