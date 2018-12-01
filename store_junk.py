class Store(object):

  def __int__(self, initial_quantity=0.0, capacity=float("inf")):
    self.capacity = capacity
    self.quantity = initial_quantity

  # Update the quantity of the store
  # self.param inflow [float]
  # self.param request [float]
  def update(self, inflow, request=0.0):
    inflow = inflow
    outflow = request
    self.quantity += (inflow - outflow)
    if self.quantity > self.capacity:
      self.quantity = self.capacity
    elif self.quantity < 0.0:
      outflow += self.quantity
      self.quantity = 0.0
    return self.quantity

  def overflow(self):
    max(self.quantity - self.capacity, 0.0)