# 주문 이력: 순서가 중요 → 리스트, 각 주문은 불변 값 (고객ID, 상품, 가격) → 튜플
orders = [
    ("C001", "라떼", 5500),
    ("C002", "아메리카노", 4500),
    ("C001", "크루아상", 4200),
    ("C003", "라떼", 5500),
]

# 고객ID로 즉시 조회해야 하는 누적 매출 → 딕셔너리
revenue_by_customer = {}
for cust_id, item, price in orders:          # 튜플 언패킹
    revenue_by_customer[cust_id] = revenue_by_customer.get(cust_id, 0) + price
print(revenue_by_customer)   # {'C001': 9700, 'C002': 4500, 'C003': 5500}

# 이번 주 구매 고객 집합 (중복 제거) → 셋
buyers = {cust_id for cust_id, _, _ in orders}
print(buyers)                # {'C001', 'C002', 'C003'}

# 지난주 구매 고객과의 교집합 → 재구매 고객
last_week = {"C001", "C009"}
print(buyers & last_week)    # {'C001'}
