"""Base class module for faker-ka package."""

from abc import ABC, abstractmethod
import random


class FakerBase(ABC):
    """Abstract base class for faker-ka"""

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    @abstractmethod
    def generate(self):
        """Abstract method to be implemented by subclasses"""

        pass
