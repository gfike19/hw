from functools import reduce

scores = [25, 56, 79, 94, 99]
print("Initial scores are: " + str(scores))

total_scores = reduce(lambda x, y: x+y, scores)

average = total_scores/len(scores)
print("Sum of all scores: " + str(total_scores))
print("Average: " + str(average))

above_avg = list(filter(lambda x: x > average, scores))
print("Scores above average:", str(above_avg))

curved_scores = map(lambda x: x+5, scores)

print("Curved scores are: " + str(list(curved_scores)))
