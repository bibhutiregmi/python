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
  elif (choice == "6"):
    quit()

def search_selection():
  choice = raw_input("Select the number: ")
  print
  if (choice=="1"):
    search_name()
  else:
    search_num()


def basic_operation():
  print "\n"
  for elements in basic_func:
    print elements,basic_func[elements]
  print "*********************"
  print
  option_selection()

def search_op():

  for elements in search_dir:
    print elements,search_dir[elements]
  search_selection()

def insert_op():
  name = raw_input("Enter name: ")
  phone_no = raw_input("Enter phone number: ")
  telephone_dir[name] = phone_no
  print
  print "*********************"
  view_op()
  print "\n"
  basic_operation()

def display_record(no,name):
  print
  print "*********************"
  print "Record Found"
  print name,no
  print "*********************"

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
    print "\n"
    print "****************"
  else:
    print "Not found"
  view_op()
  
def search_name():
  name = raw_input("Name to search: ")
  if name in telephone_dir:
    display_record(telephone_dir[name],name)
  else:
    print "not found"
  basic_operation()

def view_available_option():
  final_options = sorted(telephone_dir.items())
  print "Name\tPhone"
  for i in final_options:
    print "%s\t%s" %(i[0],i[1])
  print "********************"

def view_op():
  view_available_option()
  basic_operation()

def main():
  basic_operation()

if __name__ == '__main__':
  main()