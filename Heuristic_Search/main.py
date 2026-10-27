from benchmark import Benchmark

def main():
    """First function that is called on script execution.
    Calls the other functions.
    """

    benchmark = Benchmark()

    print("--- Start of Benchmark ---")

    benchmark.start_test()

    print("--- End of Benchmark ---")

if __name__ == '__main__':
    main()