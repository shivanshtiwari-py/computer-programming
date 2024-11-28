#Given a dictionary with student names as keys and their scores as values, write a function to return the name of the student with the highest score.
def top_student(scores):
    return max(scores, key=scores.get)

scores = {'Alice': 90, 'Bob': 85, 'Clara': 95}
print(top_student(scores))
