def solve(A, B, C, P):
    alpha = ((B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])) / ((B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1]))
    beta = ((C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])) / ((B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1]))
    gamma = 1 - alpha - beta
    if alpha > 0 and beta > 0 and gamma > 0:
        return True
    else:
        return False
A = list(map(float, input("Nhập tọa độ điểm A (x, y): ").split(', ')))
B = list(map(float, input("Nhập tọa độ điểm B (x, y): ").split(', ')))
C = list(map(float, input("Nhập tọa độ điểm C (x, y): ").split(', ')))
P = list(map(float, input("Nhập tọa độ điểm P (x, y): ").split(', ')))
if __name__ == "__main__":
    if solve(A, B, C, P):
        print("Điểm P nằm trong tam giác ABC")
    else:
        print("Điểm P nằm ngoài tam giác ABC")