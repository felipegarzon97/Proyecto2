import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    header = next(reader)
    data = []
    #print (header)
    #print (list(reader))
    for row in reader:
      iterable = zip(header, row)
      
      country_dict = {key: value for key, value in iterable}
      #print(list(iterable))
      #print(country_dict)
      data.append(country_dict)
    return data
      
    '''print('***' * 5)
    print(row)'''

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  
  print(data)