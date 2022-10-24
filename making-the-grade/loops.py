def round_scores(student_scores):
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    return sum((1 for score in student_scores if score <= 40))


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    interval = (highest - 40) // 4
    return [41 + (step * interval) for step in range(4)]


def student_ranking(student_scores, student_names):
    return [str(idx + 1) + ". " + student_names[idx] + ": " + str(student_scores[idx]) for idx in range(len(student_scores))]


def perfect_score(student_info):
    for info in student_info:
        if info[1] == 100:
            return info
    return []
