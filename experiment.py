import time
import csv
from course_data import get_small_dataset, get_medium_dataset, get_large_dataset, get_forced_backtracking_dataset
from solver import Solver


def run_experiments():
    modes = ["basic", "mrv_degree", "mrv_degree_mac"]
    datasets = [
        ("small", get_small_dataset),
        ("medium", get_medium_dataset),
        ("large", get_large_dataset),
        ("unsolvable", get_forced_backtracking_dataset),
    ]

    results = []

    for dataset_name, get_dataset in datasets:
        for mode in modes:
            courses = get_dataset()

            solver = Solver(courses, mode=mode)

            start = time.time()
            solution = solver.solve()
            end = time.time()

            solver.metrics.runtime = end - start

            results.append({
                "dataset": dataset_name,
                "courses": len(courses),
                "mode": mode,
                "runtime": solver.metrics.runtime,
                "nodes_visited": solver.metrics.nodes_visited,
                "backtracks": solver.metrics.backtracks,
                "solution_found": solution is not None
            })

            if solution:
                print(f"[{mode}]")
                for course in courses:
                    sec = solution[course.course_id]
                    print(f"{course.name}: {sec}")

    return results


def save_results(results, filename="results.csv"):
    with open(filename, "w", newline="") as f:
        fieldnames = [
            "dataset",
            "courses",
            "mode",
            "runtime",
            "nodes_visited",
            "backtracks",
            "solution_found"
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    results = run_experiments()

    for row in results:
        print(row)

    save_results(results)