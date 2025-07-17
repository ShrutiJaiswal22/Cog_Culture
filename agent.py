def recommend(row):
    if 'OverTime_Yes' in row and row['OverTime_Yes'] == 1:
        return "Reduce workload"
    elif row['JobSatisfaction'] <= 2:
        return "Assign mentor"
    return "Monitor quarterly"
