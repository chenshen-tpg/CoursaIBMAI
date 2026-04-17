"""
When to Use enumerate() - Practical Examples
"""

# ============================================
# CONDITION 1: You need both INDEX and VALUE
# ============================================

print("=" * 60)
print("CONDITION 1: Need both INDEX and VALUE")
print("=" * 60)

students = ["Alice", "Bob", "Charlie", "Diana"]

# WITHOUT enumerate - verbose and error-prone
print("\nWithout enumerate:")
for i in range(len(students)):
    student = students[i]
    print(f"Position {i}: {student}")

# WITH enumerate - clean and Pythonic
print("\nWith enumerate:")
for i, student in enumerate(students):
    print(f"Position {i}: {student}")


# ============================================
# CONDITION 2: Finding positions of elements
# ============================================

print("\n" + "=" * 60)
print("CONDITION 2: Finding POSITIONS of specific elements")
print("=" * 60)

scores = [85, 92, 78, 92, 88, 92]

# Find all positions where score is 92
print("\nFind all positions of score 92:")
for i, score in enumerate(scores):
    if score == 92:
        print(f"Found 92 at index {i}")


# ============================================
# CONDITION 3: Your code (Mirror Pair Distance)
# ============================================

print("\n" + "=" * 60)
print("CONDITION 3: Your Mirror Pair Problem")
print("=" * 60)

nums = [123, 321, 456, 654]

# We need BOTH index AND value to:
# 1. Check if the reversed number exists (need the value)
# 2. Calculate distance between indices (need the indices)

print("\nFinding mirror pairs:")
for i, num in enumerate(nums):
    reversed_num = int(str(num)[::-1])
    print(f"Index {i}: num={num}, reversed={reversed_num}")


# ============================================
# CONDITION 4: Modifying list with access to index
# ============================================

print("\n" + "=" * 60)
print("CONDITION 4: Modifying elements based on position")
print("=" * 60)

prices = [10, 20, 30, 40, 50]

# Apply different discounts based on position
print("\nApplying discounts based on position:")
discounted = []
for i, price in enumerate(prices):
    if i < 2:
        discount = price * 0.1  # 10% for first 2
    elif i < 4:
        discount = price * 0.2  # 20% for next 2
    else:
        discount = price * 0.3  # 30% for rest
    final_price = price - discount
    discounted.append(final_price)
    print(f"Position {i}: ${price} → ${final_price:.2f}")


# ============================================
# CONDITION 5: Comparing with previous/next elements
# ============================================

print("\n" + "=" * 60)
print("CONDITION 5: Comparing with previous elements")
print("=" * 60)

temps = [20, 25, 23, 28, 26, 30]

print("\nDetect temperature increases:")
for i, temp in enumerate(temps):
    if i > 0:
        if temp > temps[i-1]:
            increase = temp - temps[i-1]
            print(f"Index {i}: {temps[i-1]}°C → {temp}°C (↑ {increase}°C)")


# ============================================
# CONDITION 6: Custom starting index
# ============================================

print("\n" + "=" * 60)
print("CONDITION 6: Starting from a custom index")
print("=" * 60)

items = ["A", "B", "C", "D"]

# Start counting from 1 instead of 0 (useful for line numbers, rankings, etc.)
print("\nWith default start (0):")
for i, item in enumerate(items):
    print(f"{i}: {item}")

print("\nWith custom start (1):")
for i, item in enumerate(items, start=1):
    print(f"{i}: {item}")


# ============================================
# WHEN NOT TO USE enumerate()
# ============================================

print("\n" + "=" * 60)
print("WHEN NOT TO USE enumerate()")
print("=" * 60)

colors = ["Red", "Green", "Blue"]

# DON'T use enumerate if you only need VALUES
print("\nJust iterating over values (DON'T use enumerate):")
for color in colors:
    print(color)

# This is cleaner than:
# for i, color in enumerate(colors):
#     print(color)


print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
USE enumerate() WHEN YOU NEED:
  ✓ Both index and value
  ✓ The position/index of elements
  ✓ To modify elements based on their position
  ✓ To compare current element with previous/next
  ✓ Line numbers or position-based numbering
  ✓ Distance/gap calculations between indices

DON'T USE enumerate() WHEN:
  ✗ You only need the values (just use: for item in list)
  ✗ You're not using the index at all
  
YOUR CODE USES it BECAUSE:
  → You need both the index (i) and the number (num)
  → You calculate distance: i - prev[num]
  → You track positions of numbers to find mirrors
""")

