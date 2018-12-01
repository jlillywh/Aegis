from itertools import count

class Aegis:
    """
        Base class for all Aegis objects

        ...

        Attributes
        ----------
        about_str : str
            a formatted string to print out the store properties
        name : str
            the name of the store

        Methods
        -------
        getNumInstances : int
            return the number of objects of this class created
        """

    _ids = count(0)

    def __init__(self, name = "Aegis"):
        """
        Parameters
        ----------
        name : str, optional
            the amount in the store
        """

        self.id = next(self._ids)

    def getNumInstances(self):
        """
        Get the count of objects created by this class
        :return:
        """
        return self._ids



