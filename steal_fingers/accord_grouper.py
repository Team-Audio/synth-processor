from tqdm import tqdm

from pstep_base import SymmetricPipelineStepBase


class GroupAccords(SymmetricPipelineStepBase):
    def __init__(self):
        self.vals = []

    def take_pipeline(self, value):
        current_time = 0
        accord = []

        for msg, f in tqdm(value, desc='Crawling Notes to Group'):
            current_time += msg.time
            if msg.time > 0:
                entry = []
                t = 0
                for (note, finger, timing) in accord:
                    entry += [(note, finger)]
                    t = timing
                self.vals += [(entry, t)]
                accord = [(msg.note, f, current_time)]
            else:
                accord += [(msg.note, f, current_time)]

    def has_value(self) -> bool:
        return len(self.vals) > 0

    def pop(self):
        return self.vals.pop(0)
