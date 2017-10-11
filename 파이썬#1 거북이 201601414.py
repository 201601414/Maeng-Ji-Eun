>>> import turtle as t
>>> t.shape("turtle")
>>> t.speed(0)              # 거북이 속도를 가장 빠르게 설정
>>> t.bgcolor("black")      # 배경색을 검은색으로 지정

>>> angle = 100             # 거북이가 회전할 각도를 지정(오른쪽/왼쪽)
 
>>> t.color("red")          # 펜 색을 빨간색으로 지정
>>> for x in range(180):    # x 값을 0에서 179까지 바꾸면서 180번 실행
	t.forward(x)        # x만큼 앞으로 이동
	t.right(angle)      # 거북이가 오른쪽으로 100도 회전

	
>>> t.color("orange")       # 펜 색을 주황색으로 지정
>>> for x in range(140):    # x 값을 0에서 139까지 바꾸면서 140번 실행
	t.forward(x)        # x만큼 앞으로 이동
	t.right(angle)      # 거북이가 오른쪽으로 100도 회전

	
>>> t.color("yellow")       # 펜 색을 노란색으로 지정
>>> for x in range(80):     # x 값을 0에서 79까지 바꾸면서 80번 실행
	t.forward(x)        # x만큼 앞으로 이동
	t.left(angle)       # 거북이가 왼쪽으로 100도 회전
