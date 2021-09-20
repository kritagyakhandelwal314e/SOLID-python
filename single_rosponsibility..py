#Single Responsibility Principle or Seperation of Concerns Principle
class Journal:
  def __init__(self) -> None:
    self.entries = []
    self.count = 0

  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')

  def remove_entry(self, pos):
    del self.entries[pos]

  def __str__(self):
    return '\n'.join(self.entries)

  # def save(self, filename):
  #   with open(file=filename, mode='w') as file:
  #     file.write(str(self))

  # def load(self, filename):
  #   with open(file=filename, mode='r') as file:
  #     return file.readlines()

  # def load_from_web(self, uri):
  #   pass

class PersistenceManager:
  
  @staticmethod
  def save_to_file(data, filename):
    with open(file=filename, mode='w') as file:
      file.write(str(data))

  @staticmethod
  def load_from_file(filename):
    with open(file=filename, mode='r') as file:
      return ''.join(file.readlines())




j = Journal()
j.add_entry('Hi, This is Kritagya')
j.add_entry('I am 22.')
j.add_entry('MALE')
print(f'Journal Entries:\n{j}')
p = PersistenceManager()
filename = 'files/journalfile'
p.save_to_file(j, filename)
print(p.load_from_file(filename))