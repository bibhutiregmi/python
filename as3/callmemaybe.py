telephone_dir = {"apple":9,"ball":10}

basic_func = {1:"view",2:"insert",3:"delete",4:"search",5:"store in csv",6:"exit"}
search_dir = {1:"by name",2:"by number"}
def option_selection():
  choice = raw_input("Select the number: ")
  print 
  if (choice == "1"):
    view_op()
  if (choice == "2"):
    insert_op()
  if (choice == "4"):
    search_op()
  if (choice == "6"):
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
  search_no = raw_input("Select the number: ")
  for name,no in telephone_dir.items():
    if (int(no) == int(search_no)):
      display_record(no,name)
  basic_operation()


def search_name():
  name = raw_input("Name to search: ")
  if name in telephone_dir:
    display_record(telephone_dir[name],name)
  else:
    print "not found"
  basic_operation()

def view_op():
  final_options = sorted(telephone_dir.items())
  print "Name\tPhone"
  for i in final_options:
    print "%s\t%s" %(i[0],i[1])
  print "*********************"
  basic_operation()

def main():
  basic_operation()

if __name__ == '__main__':
  main()