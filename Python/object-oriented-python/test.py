class Store:
  open = 9
  close = 5
  def hours(self):
    print("We're open from {} to {}.".format(self.open, self.close))

my_store = Store()
my_store.hours()