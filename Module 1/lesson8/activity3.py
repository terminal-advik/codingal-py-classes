mean1 = 38
wrong_number=36
correct_number=56
total_number=40

#calculate mean2
incorrect_sum = mean1*total_number
correct_sum = incorrect_sum - wrong_number + correct_number
mean2=correct_sum / total_number
print("The corrected mean is:", mean2)