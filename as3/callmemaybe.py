import csv
telephone_dir = {"apple":9,"ball":10}
basic_func = {1:"view",2:"insert",3:"delete",4:"search",5:"store in csv",6:"exit"}
search_dir = {1:"by name",2:"by number"}

def option_selection():
  choice = raw_input("Select the number: ")
  print 
  if (choice == "1"):
    view_op()
  elif (choice == "2"):
    insert_op()
  elif (choice == "3"):
    delete_op()
  elif (choice == "4"):
    search_op()
  elif (choice == "5"):
    write_to_cv()
  elif (choice == "6"):
    quit()

def search_selection():
  choice = raw_input("Select the number: ")
  print
  if (choice=="1"):
    search_name()
  else:
    search_num()

def display_separator():
  print("\n")
  print "*********************"
  print("\n")



def basic_operation():
  for elements in basic_func:
    print elements,basic_func[elements]
  option_selection()
  display_separator()

def search_op():

  for elements in search_dir:
    print elements,search_dir[elements]
  search_selection()

def insert_op():
  name = raw_input("Enter name: ")
  phone_no = raw_input("Enter phone number: ")
  telephone_dir[name] = phone_no
  view_op()
  display_separator()
  basic_operation()

def display_record(no,name):
  display_separator()
  print "Record Found"
  print name,no
  display_separator()

def search_num():
  search_no = raw_input("Number to search: ")
  for name,no in telephone_dir.items():
    if (int(no) == int(search_no)):
      display_record(no,name)
    else:
      print "not found"
  basic_operation()

def delete_op():
  view_available_option()
  name = raw_input("Name to delete: ")
  if name in telephone_dir:
    del telephone_dir[name]
    print "Deleted safely"
    display_separator()
  else:
    print "Not found"
    display_separator()
  view_op()
  
def search_name():
  name = raw_input("Name to search: ")
  if name in telephone_dir:
    display_record(telephone_dir[name],name)
  else:
    print "not found"
  basic_operation()

def view_available_option():
  display_separator()
  final_options = sorted(telephone_dir.items())
  print "Name\tPhone"
  for i in final_options:
    print "%s\t%s" %(i[0],i[1])
  display_separator()

def write_to_cv():
  with open('contacts.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in telephone_dir.items():
       writer.writerow([key, value])
    display_separator()
    basic_operation()
   
def view_op():
  view_available_option()
  basic_operation()

def main():
  basic_operation()

if __name__ == '__main__':
  main()