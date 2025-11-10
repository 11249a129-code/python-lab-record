//Aim: Write a python program to find the best of two test average marks out of three test‘s marks accepted from the user.

//Algorithm:
1: Start
2: Input three test marks — test1, test2, and test3
3: Store the three marks in a list → marks = [test1, test2, test3]
4: Sort the list in descending order (from highest to lowest)
5: Select the first two marks from the sorted list — these are the best two marks
6: Calculate the average of the best two marks
  average = (best_two_marks[0] + best_two_marks[1]) / 2
7: Display the best two marks and their average
8: Stop


test1 = float(input("Enter test 1 marks: "))
test2 = float(input("Enter test 2 marks: "))
test3 = float(input("Enter test 3 marks: "))
if test1 >= test2 and test1 >= test3:
    greatest = test1
elif test2 >= test1 and test2 >= test3:
    greatest = test2
else:
    greatest = test3
    best_two_sum = test1 + test2 + test3 - lowest
average = sum(best_two) / 2
print("\nBest two test marks:", best_two)
print("Average of best two tests: {:.2f}".format(average))
