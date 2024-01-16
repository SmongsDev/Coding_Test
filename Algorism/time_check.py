# 순수 연산 시간의 측정 (코드의 성능을 확인): process_time()을 사용
import time
start_time = time.process_time()

# 실행 시간을 측정할 코드

end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")

# 전체 실행시간의 측정 (코드의 실제 실행 시간을 확인): perf_counter()를 사용
import time
start_time = time.perf_counter()

# 실행 시간을 측정할 코드

end_time = time.perf_counter()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")