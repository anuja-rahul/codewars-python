def zeros(n):
    count = 0
    div = 5
    while n // div >= 1:

        count += n // div
        div *= 5

    return count


print(zeros(1000))
