import time 

def extend_method_experiment():
    my_list = []
    start_time = time.perf_counter()
    for _ in range(1000000):
        my_list.extend([1, 2, 3])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

def append_method_experiment():
    my_list = []
    start_time = time.perf_counter()
    for _ in range(1000000):
        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

extend_time = extend_method_experiment()
append_time = append_method_experiment()

print("Elapsed Time - extend method:", extend_time)
print("Elapsed Time - append method:", append_time)
