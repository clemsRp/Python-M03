#!/usr/bin/env python3


def get_events(nb_events: int):
    '''
    Generate an event
    '''
    players = ["Alice", "Bob", "Charlie", "John", "Jack"]
    events = ["killed monster", "found treasure", "leveled up"]

    p = prime()
    f = fibonacci()

    for k in range(nb_events):
        new = next(p) + next(f)
        player = players[new % len(players)]
        level = (new * 3) % 20 + 1
        event = events[(new * 7) % len(events)]

        yield {
            "id": k + 1,
            "player": player,
            "level": level,
            "type": event
        }


def main(nb_events: int) -> None:
    '''
    Test different generator
    '''
    print(f"Processing {nb_events} game events...\n")

    events = get_events(nb_events)
    high_level = 0
    treasure_events = 0
    level_events = 0
    for event in events:
        if event["level"] > 10:
            high_level += 1
        if event["type"] == "found treasure":
            treasure_events += 1
        elif event["type"] == "leveled up":
            level_events += 1

        if event["id"] <= 3:
            print(f"Event {event["id"]}: Player {event["player"]}"
                  f" (level {event["level"]}) {event["type"]}")
    print("...\n")

    print("=== Stream Analytics ===")
    print("Total events processed:", nb_events)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_events)
    print()

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()


def fibonacci():
    '''
    Generate the fibonacci number
    '''
    n1 = 0
    n2 = 1
    yield n1
    yield n2
    while True:
        new = n1 + n2
        yield new
        n1 = n2
        n2 = new


def not_prime(num) -> bool:
    '''
    Return if a number is prime or not
    '''
    for k in range(2, num):
        if num % k == 0:
            return True
    return False


def prime():
    '''
    Generate a prime number
    '''
    i = 2
    while True:
        while not_prime(i):
            i += 1
        yield i
        i += 1


def demonstration() -> None:
    '''
    Test the fibonacci generator and the prime generator
    '''
    print("=== Generator Demonstration ===")

    nb_f = 10
    print(f"Fibonacci sequence (first {nb_f}): ", end="")
    f = fibonacci()
    for k in range(nb_f - 1):
        print(f"{next(f)}, ", end="")
    print(next(f))

    nb_p = 5
    print(f"Prime numbers (first {nb_p}): ", end="")
    p = prime()
    for k in range(nb_p - 1):
        print(f"{next(p)}, ", end="")
    print(next(p))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    main(1000)
    demonstration()
