from typing import List

from mfunction import group_func
from pstep_base import PipelineStepBase


class Pipeline:

    def __init__(self, steps: List[List[PipelineStepBase]]):
        self.steps = steps
        self.left = ()
        self.right = ()

    def run(self):
        for step in self.steps:
            group_func([x.take_pipeline for x in step], (self.left, self.right))

            self.right = []
            while all(group_func([x.has_right for x in step], ())):
                self.right += [group_func([x.pop_right for x in step], ())]

            self.left = []
            while all(group_func([x.has_left for x in step], ())):
                self.left += [group_func([x.pop_left for x in step], ())]

        return self.right, self.left
