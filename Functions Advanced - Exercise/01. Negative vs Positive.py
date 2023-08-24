def negative_or_positive(numbers):
    negative = 0
    positive = 0
    for i in numbers:
        if int(i) < 0:
            negative += int(i)
        else:
            positive += int(i)
    if abs(negative) > positive:
        return str(negative) + "\n" + str(positive) + "\n" + "The negatives are stronger than the positives"
    else:
        return str(negative) + "\n" + str(positive) + "\n" + "The positives are stronger than the negatives"


print(negative_or_positive(input().split()))