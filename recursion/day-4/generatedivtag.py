ans = []


def generate(arr, open, close, n):
    if len(arr) == 2*n:
        ans.append(arr.copy())

    # number of open tags
    if open < n:
        arr.append("<div>")
        generate(arr, open+1, close, n)
        arr.pop()

    # close tags must always be less than the open tag
    if close < open:
        arr.append("</div>")
        generate(arr, open, close+1, n)
        arr.pop()


generate(arr=[], open=0, close=0, n=3)
print(ans)
print(len(ans))

