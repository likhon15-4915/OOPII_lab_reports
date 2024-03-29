n = int(input())
scores = list(map(int, input().split()))
# Remove duplicates and sort the list in descending order
unique_scores = sorted(set(scores), reverse=True)
# Print the runner-up score
print(unique_scores[1])
