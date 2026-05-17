import math


def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
    """두 점 (x1, y1), (x2, y2) 사이의 유클리드 거리를 반환합니다."""
    return math.hypot(x2 - x1, y2 - y1)


def main() -> None:
    print("두 점 사이 거리 계산기")
    x1 = float(input("첫 번째 점의 x 좌표: "))
    y1 = float(input("첫 번째 점의 y 좌표: "))
    x2 = float(input("두 번째 점의 x 좌표: "))
    y2 = float(input("두 번째 점의 y 좌표: "))

    distance = distance_between_points(x1, y1, x2, y2)
    print(f"두 점 사이의 거리는 {distance:.6f} 입니다.")


if __name__ == "__main__":
    main()
