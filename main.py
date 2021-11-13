import time


def test_function():
    pass


if __name__ == "__main__":

    # Number of Iterations
    n = 994000000   # 8999994000000
    print("[+] Number of Iterations: " + str(n))

    for k in range(3):
        print("[+] Test Number: " + str(k+1))

        # Test1
        time1_no_function = time.time_ns()
        for i in range(n):
            pass
        time2_no_function = time.time_ns()

        # Test2
        time1_with_function = time.time_ns()
        for i in range(n):
            test_function()
        time2_with_function = time.time_ns()

        # Echo
        print("[->] Time without Function: " + str(time2_no_function - time1_no_function) + "ns")
        print("[->] Time with a  Function: " + str(time2_with_function - time1_with_function) + "ns")
