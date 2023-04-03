def max_rectangle(n, a, b):
    # Split blocks and sort by decreasing height
    blocks = [(max(a[i], b[i]), min(a[i], b[i])) for i in range(n)]
    blocks.sort(reverse=True)

    # Initialize stack and maximum area found so far
    stack = []
    max_area = 0

    # Iterate over blocks
    for i in range(n):
        height, width = blocks[i]
        while stack and height < stack[-1][0]:
            # Pop top block and calculate area of rectangle that can be formed
            h, w = stack.pop()
            max_area = max(max_area, h * (width + (i - w - 1 if stack else i)))

        # Push current block onto stack
        stack.append((height, i))

    # Process any remaining blocks in stack
    while stack:
        h, w = stack.pop()
        max_area = max(max_area, h * (n - w))

    # Calculate maximum width by considering all possible pairs of blocks
    max_width = 0
    for i in range(n):
        for j in range(i+1, n):
            h1, w1 = blocks[i]
            h2, w2 = blocks[j]
            if h1 != h2:
                continue
            width = w1 + w2
            k = j + 1
            while k < n and blocks[k][0] >= h1 and blocks[k][1] <= w2:
                width += blocks[k][1]
                k += 1
            max_width = max(max_width, h1 * width)

    return max_width // blocks[0][0]







print(max_rectangle(1, [3], [14]))  # Expected output: 42 your code still return 1
print(max_rectangle(2, [3, 4], [4, 5]))  # Expected output: 32 your code still return 4
print(max_rectangle(4, [3, 2, 4, 2], [3, 1, 7, 5]))  # Expected output: 36 your code still return 3
