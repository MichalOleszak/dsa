import heapq


class MedianMaintainer:
    def __init__(self):
        self.heap_lo = []
        self.heap_hi = []

    def add_number(self, i):
        if len(self.heap_lo) == 0 or i <= self.heap_lo[0]:
            heapq.heappush_max(self.heap_lo, i)
        elif len(self.heap_hi) == 0 or i > self.heap_hi[0]:
            heapq.heappush(self.heap_hi, i)
        else:
            heapq.heappush_max(self.heap_lo, i)
        if len(self.heap_lo) > len(self.heap_hi) + 1:
            max_from_lo = heapq.heappop_max(self.heap_lo)
            heapq.heappush(self.heap_hi, max_from_lo)
        if len(self.heap_hi) > len(self.heap_lo) + 1:
            min_from_hi = heapq.heappop(self.heap_hi)
            heapq.heappush_max(self.heap_lo, min_from_hi)


    def get_current_median(self):
        total_elements = len(self.heap_hi) + len(self.heap_lo)
        if total_elements % 2 == 0:
            return self.heap_lo[0]
        elif len(self.heap_hi) > len(self.heap_lo):
            return self.heap_hi[0]  # min heap - get min value
        else:
            return self.heap_lo[0]  # max heap - get max value


def read_data(file_path: str) -> list:
    with open(file_path, "r") as f:
        data = f.readlines()
    return [int(d.replace("\n", "")) for d in data]


def main():
    data = read_data("data/median_maintenance.txt")
    mm = MedianMaintainer()
    running_sum = 0
    for i in data:
        mm.add_number(i)
        running_sum += mm.get_current_median()
    print(f"running sum: {running_sum}")
    print(running_sum % 10_000)


if __name__ == "__main__":
    main()