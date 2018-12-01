import errorChecks as ec
from aegis import Aegis

class Store(Aegis):
    """
        A class used to represent a storage element

        ...

        Attributes
        ----------
        about_str : str
            a formatted string to print out the store properties
        name : str
            the name of the store
        quantity : float
            the amount in the store
        capcity : float
            the upper bound on quantity
        overflow : float
            amount in excess of capacity after applying inflow and outflow
        outflow : float
            requested outflow until store is empty

        Methods
        -------
        update : float
            update quantity after applying inflows and outflows
        """

    def __init__(self, name="Store", quantity=100.0, capacity=float("inf")):
        """
        Parameters
        ----------
        name : str, optional
            the name of the object (inherited)
        quantity : float, optional
            the amount in the store
        capacity : float, optional
            the upper bound on quantity
        """

        Aegis.__init__(self, name)

        self.quantity = quantity
        self.capacity = capacity

    def update(self, inflow, outflow):
        """Updates the quantity given inflow and outflow being applied

        If quantity ends up out of bounds (upper or lower) then it is
        set to the bound and overflow or outflow is updated

        Parameters
        ----------
        inflow : float
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            Raise if either value is negative
        """

        ec.checkPositive(inflow, "inflow")
        ec.checkPositive(outflow, "outflow")

        self.quantity += inflow - outflow

        if self.quantity > self.capacity:
            self.quantity = self.capacity
        elif self.quantity < 0.0:
            outflow += self.quantity
            self.quantity = 0.0