import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'area-circle': 1,
    'perimeter-circle': 1,
    'area-square': 1,
    'perimeter-square': 1
}


def calc(fig, func, size):
    assert fig in figs, f"Unknown figure. Available figures: {figs}"
    assert func in funcs, f"Unknown function. Available functions: {funcs}"

    if not isinstance(size, list):
        raise TypeError("Size must be a list")
    if not size:
        raise TypeError("Size list cannot be empty")
    if not all(isinstance(x, (int, float)) for x in size):
        raise TypeError("All sizes must be numbers")

    if fig == 'circle':
        if len(size) != 1:
            raise TypeError("Circle requires exactly 1 parameter")
        if func == 'area':
            return circle.area(size[0])
        return circle.perimeter(size[0])

    if fig == 'square':
        if len(size) != 1:
            raise TypeError("Square requires exactly 1 parameter")
        if func == 'area':
            return square.area(size[0])
        return square.perimeter(size[0])


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    params = 1
    while len(size) != params:
        try:
            size = list(map(float, input(f"Input {params} figure size(s) "
                                         "separated by space:\n").split()))
        except ValueError:
            print("Please enter valid numbers")
            continue

    try:
        result = calc(fig, func, size)
        print(f'{func} of {fig} is {result}')
    except (ValueError, TypeError, AssertionError) as e:
        print(f"Error: {e}")
