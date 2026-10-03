class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        """구매 금액의 5%를 포인트로 적립한다."""
        self.points += int(amount * 0.05)

    def get_discount_rate(self):
        """등급별 할인율을 반환한다."""
        if self.grade == "vip":
            return 0.10
        return 0.03

c1 = Customer("김서강", "vip")
c1.add_points(45000)
print(c1.points)                 # 2250
print(c1.get_discount_rate())    # 0.1

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer     # Customer 인스턴스를 참조
        self.items = items           # [(상품명, 가격), ...] 튜플의 리스트

    def total_price(self):
        """주문 총액 (고객 등급 할인 적용)"""
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

c1 = Customer("김서강", "vip")
order = Order("A-1001", c1, [("라떼", 5500), ("크루아상", 4200)])
print(f"{order.customer.name}님의 결제 금액: {order.total_price():,}원")
# 김서강님의 결제 금액: 8,730원

