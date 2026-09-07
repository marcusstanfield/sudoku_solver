import time
from src.generator.generator import Generator
from src.display import format_board

def main():
    generator = Generator(size=9)
    
    start = time.time()
    board = generator.generate(algorithm="backtracking")
    end = time.time()
    print(f"Elapsed: {(end - start) * 1e6:.3f} µs")
    print(format_board(board))

if __name__ == "__main__":
    main()