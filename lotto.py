import random

# Method: draw 6 numbers from 1 to 45
def draw_numbers():
    """
    Draw 6 unique random numbers from 1 to 45.
    Uses an efficient swap method to avoid duplicates.
    Returns:
        list[int]: List of 6 drawn numbers.
    """
    numbers = list(range(1, 46))  # possible numbers from 1 to 45
    result = []
    n = 45  # number of available choices

    # Pick 6 numbers
    for i in range(6):
        index = random.randint(0, n - 1)  # pick random index
        result.append(numbers[index])     # add number to result
        numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]  # swap chosen with last
        n -= 1  # reduce available numbers

    return result


def print_draw(result: list):
    """
    Print the drawn numbers sorted in ascending order.
    Args:
        result (list[int]): List of drawn numbers.
    """
    print("Drawn Numbers:", sorted(result))


def statistics(rounds: int):
    """
    Perform multiple draws and count the frequency of each number.
    Args:
        rounds (int): How many times to draw numbers.
    Returns:
        dict[int, int]: Dictionary with number as key and frequency as value.
    """
    counter = {i: 0 for i in range(1, 46)}  # initialize counts

    # Repeat the drawing 'rounds' times
    for _ in range(rounds):
        result = draw_numbers()
        for number in result:
            counter[number] += 1

    return counter


def main():
    """
    Main program:
    - Perform one draw
    - Ask the user how many rounds to simulate
    - Show statistics with counts and percentages
    """
    # One draw
    result = draw_numbers()
    print_draw(result)

    # Ask user for number of rounds
    rounds = int(input("\nEnter how many rounds to simulate: "))

    # Calculate statistics
    counts = statistics(rounds)
    print(f"\nStatistics after {rounds} draws:")

    # Print count and percentage
    for number in range(1, 46):
        percent = (counts[number] / (rounds * 6)) * 100  # probability percentage
        print(f"Number {number:2}: {counts[number]:7} times ({percent:5.2f}%)")


if __name__ == '__main__':
    main()
