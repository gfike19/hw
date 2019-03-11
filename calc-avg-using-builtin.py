# def gtavg(lst, num):
#     avg = sum(lst)/len(lst)
#     if num > avg:
#         return True
#     else:
#         return False


scores = [25, 56, 79, 94, 99]
avg = sum(scores)/len(scores)
above_avg = list(filter(lambda x: x > avg, scores))
print(above_avg)

