import abc


class PipelineStepBase(metaclass=abc.ABCMeta):

    def take_pipeline(self, left, right):
        pass

    @abc.abstractmethod
    def has_left(self) -> bool:
        raise NotImplementedError("Abstract method not implemented!")

    @abc.abstractmethod
    def has_right(self) -> bool:
        raise NotImplementedError("Abstract method not implemented!")

    @abc.abstractmethod
    def pop_left(self):
        raise NotImplementedError("Abstract method not implemented!")

    @abc.abstractmethod
    def pop_right(self):
        raise NotImplementedError("Abstract method not implemented!")


class SymmetricPipelineStepBase(metaclass=abc.ABCMeta):

    def take_pipeline(self, value):
        pass

    @abc.abstractmethod
    def has_value(self) -> bool:
        raise NotImplementedError("Abstract method not implemented!")

    @abc.abstractmethod
    def pop(self):
        raise NotImplementedError("Abstract method not implemented!")


class SymmetryAdapter(PipelineStepBase):
    def take_pipeline(self, left, right):
        self.left_handler.take_pipeline(left)
        self.right_handler.take_pipeline(right)

    def has_left(self) -> bool:
        return self.left_handler.has_value()

    def has_right(self) -> bool:
        return self.right_handler.has_value()

    def pop_left(self):
        return self.left_handler.pop()

    def pop_right(self):
        return self.right_handler.pop()

    def __init__(self, left_handler: SymmetricPipelineStepBase, right_handler: SymmetricPipelineStepBase):
        self.left_handler = left_handler
        self.right_handler = right_handler
