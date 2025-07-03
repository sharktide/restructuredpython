from restructuredpython.predefined.subinterpreter import optimize_loop
print("Running unoptimized loop:")
import time
start = time.perf_counter()
for i in range(10_000_000) :
    temp = str(i) * 10
end = time.perf_counter()
print("Unoptimized loop time:", round(end - start, 4), "seconds")

@optimize_loop(gct=True, profile=True)
def _repy_optimized_loop_0():
    for j in range(10_000_000) :
        temp = str(j) * 10
_repy_optimized_loop_0()