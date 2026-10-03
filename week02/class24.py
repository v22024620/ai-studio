import sys

# 방법 A: 리스트 — 1천만 개를 전부 메모리에 생성
squares_list = [x * x for x in range(10_000_000)]
print(sys.getsizeof(squares_list))   # 약 89,095,160 바이트 (약 85MB)

# 방법 B: Generator — '만드는 방법'만 기억
squares_gen = (x * x for x in range(10_000_000))   # 괄호만 ( )로
print(sys.getsizeof(squares_gen))    # 약 200 바이트

# 둘 다 for문에서는 동일하게 사용 가능
total = sum(squares_gen)
print(total)
print(type(squares_gen))
print(type(squares_list))


