import csvdifficulty_point = []point = 0stable_level = [3,5,7]option_dic ={}ques_no = []question = []answer = []option_albhabets = ["a","b","c","d"]def display_final_amount():  print "Thank you for playing"  print "Congratulation!! You won: %d" %point  quit()def display_option(ques_no):  options = option_dic[ques_no]  i = 0  for elements in options:    print option_albhabets[i],". ", elements    i = i+1def calcule_difficulty(ques_no):  return difficulty_point[ques_no]def check_answer(ques_no, user_answer):  if user_answer == answer[ques_no]:    print '\ncorrect\n'    point_calculate(int(calcule_difficulty(ques_no)))  else:    print '\nSorry incorrect\n'    print "correct answer was: %s" %answer[ques_no]    point_calculate(-int(calcule_difficulty(ques_no)))    display_final_amount()      def point_calculate(difficulty_point):  global point  point += difficulty_point  print 'Yo won %d so far'%pointdef show_question():  for i in range(10):    question_number = ques_no[i+1]    print 'Your current amount %d\n' %point    print "Now lets start round %s" %question_number    continue_game = proceed()    if continue_game:      print       print question[i+1]      display_option(question_number)      answer = raw_input("Your answer is: ")      check_answer(i+1, answer)    else:      display_final_amount()    print "********************************\n"      def proceed():  choice = raw_input("Continue game y/n: ")  if choice == 'y':    return 1  return 0def info():  print "\n\tWelcome to KBC\n"  print "********************************\n"  print "Rule: Type a/b/c/d\n"  def main():  with open('kbc.csv','rU') as openfile:    thedata = csv.reader(openfile)    for row in thedata:      ques_no.append(row[0])      question.append(row[1])      answer.append(row[6])      difficulty_point.append(row[7])      option = [row[2],row[3],row[4],row[5]]      option_dic[row[0]] = option  info()  show_question()if __name__ == '__main__':  main()