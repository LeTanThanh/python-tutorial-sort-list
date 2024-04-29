if __name__ == "__main__":
  # Introduction to the Python List sort() method

  """
  list.sort()
  list.sort(reverse = True)
  """

  # Using the Python List sort() method to sort a list of strings

  guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
  print(guests)
  guests.sort()
  print(guests)

  guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
  print(guests)
  guests.sort(reverse=True)
  print(guests)

  # Using the Python List sort() method to sort a list of numbers

  scores = [5, 7, 4, 6, 9, 8]
  print(scores)
  scores.sort()
  print(scores)

  scores = [5, 7, 4, 6, 9, 8]
  print(scores)
  scores.sort(reverse = True)
  print(scores)

  # Using the Python List sort() method to sort a list of tuples

  companies = [
    ("Google", 2019, 134.81),
    ("Apple", 2019, 260.2),
    ("Facebook", 2019, 70.7)
  ]
  print(companies)

  def sort_key(company):
    return company[2]

  companies.sort(key = sort_key)
  print(companies)

  companies = [
    ("Google", 2019, 134.81),
    ("Apple", 2019, 260.2),
    ("Facebook", 2019, 70.7)
  ]
  print(companies)

  companies.sort(key = lambda company: company[2], reverse = True)
  print(companies)
