from abc import ABC, abstractmethod


class IResult(ABC):
    @property
    @abstractmethod
    def is_failure(self):
        pass

    @property
    @abstractmethod
    def is_success(self):
        pass


class IValue(ABC):
    @property
    @abstractmethod
    def value(self):
        pass


class IError(ABC):
    @property
    @abstractmethod
    def error(self):
        pass


class IResultBase(IResult, IValue, IError, ABC):
    pass
