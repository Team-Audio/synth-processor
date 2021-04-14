import xml.etree.ElementTree as ET

from pstep_base import PipelineStepBase


class SynthesiaMetaDataParser(PipelineStepBase):

    def __init__(self, filename: str):

        with open(filename) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            for item in root.findall('./Songs'):
                for child in item:
                    fingerhints = child.attrib['FingerHints']
                    right, left = fingerhints.split(' t1: ')
                    self.right = right
                    self.left = left

        def parse_string_inline(v):
            arr = []
            for cha in v:
                cha = int(cha)
                if cha > 5:
                    cha -= 5
                elif cha == 0:
                    cha = 5
                arr += [cha]
            return arr

        self.right = parse_string_inline(self.right)
        self.left = parse_string_inline(self.left)

    def has_left(self) -> bool:
        return len(self.left) > 0

    def has_right(self) -> bool:
        return len(self.right) > 0

    def pop_left(self):
        return self.left.pop(0)

    def pop_right(self):
        return self.right.pop(0)
