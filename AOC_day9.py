numbers = [[*map(int, line.split())] for line in open('input.txt')]
def predict(nums):
    diffs = [b-a for a,b in zip(nums,nums[1:])]
    return nums[-1] + (predict(diffs) if any(diffs) else 0)

print('part 1:', sum(map(predict,numbers)))
print('part 2:', sum(predict(num[::-1]) for num in numbers)
