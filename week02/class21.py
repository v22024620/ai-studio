class Customer:
    """카페의 고객 한 명을 표현하는 클래스"""
    def __init__(self, name, grade="basic"):
        self.name = name         # 인스턴스 속성
        self.grade = grade
        self.points = 0

# 인스턴스 생성: 클래스명(인자) 형태로 호출하면 __init__이 자동 실행된다
c1 = Customer("김서강", "vip")
c2 = Customer("이알바")          # grade는 기본값 "basic"

print(c1.name, c1.grade)         # 김서강 vip
print(c2.name, c2.grade)         # 이알바 basic
print(c1 is c2)                  # False — 서로 다른 실체
