def appearance(intervals: dict) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    if pupil[0] < lesson[0]:
        pupil[0] = lesson[0]
    if pupil[-1] > lesson[-1]:
        pupil[-1] = lesson[-1]
    if tutor[0] < lesson[0]:
        tutor[0] = lesson[0]
    if tutor[-1] > lesson[-1]:
        tutor[-1] = lesson[-1]

    sum_of_times = 0
    for i in range(0, len(tutor), 2):
        tutor_start = tutor[i]
        tutor_end = tutor[i + 1]
        for j in range(0, len(pupil), 2):
            general_start = pupil[j]
            general_end = pupil[j + 1]
            if tutor_start > general_end:
                continue

            if tutor_start > general_start:
                general_start = tutor_start

            if (general_start < tutor_end) and (tutor_end < general_end):
                general_end = tutor_end

            if tutor_end < general_end:
                general_end = tutor_end

            sum_of_times += (general_end - general_start)

    return sum_of_times