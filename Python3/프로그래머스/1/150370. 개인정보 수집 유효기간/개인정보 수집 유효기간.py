def solution(today, terms, privacies):
    answer = []
    for idx, privacie in enumerate(privacies):
        date, g = privacie.split(" ")
        for term in terms:
            grade, d = term.split(" ")
            if g == grade:
                year, month, day = map(int, date.split("."))
                month += int(d)
                if month >= 12:
                    year += month // 12
                    month %= 12
                    if month == 0:
                        year -= 1
                        month = 12
                if today >= ".".join([str(year),str(month).zfill(2),str(day).zfill(2)]):
                    answer.append(idx+1)
                break
    return answer