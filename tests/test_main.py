import pytest
import math
import calculate
import circle
import square
import triangle


class TestCircle:
    class TestCircleArea:
        def test_positive_radius(self):
            radius = 1
            expected = math.pi
            result = circle.area(radius)
            assert result == expected

            radius = 2
            expected = math.pi * 4
            result = circle.area(radius)
            assert result == expected

            radius = 1.5
            expected = 7.07
            result = round(circle.area(radius), 2)
            assert result == expected

        def test_zero_radius(self):
            radius = 0
            expected = 0
            result = circle.area(radius)
            assert result == expected

        @pytest.mark.parametrize("test_input,expected", [
            (1, math.pi),
            (2, math.pi * 4),
            (0.5, math.pi * 0.25),
            (10, math.pi * 100)
        ])
        def test_various_radii(self, test_input, expected):
            radius = test_input
            result = circle.area(radius)
            assert result == expected

        @pytest.mark.parametrize("radius", [-1, -2.5, -100])
        def test_negative_radius(self, radius):
            with pytest.raises(ValueError):
                circle.area(radius)

        @pytest.mark.parametrize("invalid_input", ["2", [1], None])
        def test_invalid_types(self, invalid_input):
            with pytest.raises(TypeError):
                circle.area(invalid_input)

    class TestCirclePerimeter:
        def test_positive_radius(self):
            radius = 1
            expected = 2 * math.pi
            result = circle.perimeter(radius)
            assert result == expected

            radius = 2
            expected = 4 * math.pi
            result = circle.perimeter(radius)
            assert result == expected

            radius = 1.5
            expected = 9.42
            result = round(circle.perimeter(radius), 2)
            assert result == expected

        def test_zero_radius(self):
            radius = 0
            expected = 0
            result = circle.perimeter(radius)
            assert result == expected

        @pytest.mark.parametrize("test_input,expected", [
            (1, 2 * math.pi),
            (2, 4 * math.pi),
            (0.5, math.pi),
            (10, 20 * math.pi)
        ])
        def test_various_radii(self, test_input, expected):
            radius = test_input
            result = circle.perimeter(radius)
            assert result == expected

        @pytest.mark.parametrize("radius", [-1, -2.5, -100])
        def test_negative_radius(self, radius):
            with pytest.raises(ValueError):
                circle.perimeter(radius)

        @pytest.mark.parametrize("invalid_input", ["2", [1], None])
        def test_invalid_types(self, invalid_input):
            with pytest.raises(TypeError):
                circle.perimeter(invalid_input)


class TestSquare:
    class TestSquareArea:
        def test_positive_side(self):
            side = 1
            expected = 1
            result = square.area(side)
            assert result == expected

            side = 2
            expected = 4
            result = square.area(side)
            assert result == expected

            side = 1.5
            expected = 2.25
            result = square.area(side)
            assert result == expected

        def test_zero_side(self):
            side = 0
            expected = 0
            result = square.area(side)
            assert result == expected

        @pytest.mark.parametrize("test_input,expected", [
            (1, 1),
            (2, 4),
            (0.5, 0.25),
            (10, 100)
        ])
        def test_various_sides(self, test_input, expected):
            side = test_input
            result = square.area(side)
            assert result == expected

        @pytest.mark.parametrize("side", [-1, -2.5, -100])
        def test_negative_side(self, side):
            with pytest.raises(ValueError):
                square.area(side)

        @pytest.mark.parametrize("invalid_input", ["2", [1], None])
        def test_invalid_types(self, invalid_input):
            with pytest.raises(TypeError):
                square.area(invalid_input)

    class TestSquarePerimeter:
        def test_positive_side(self):
            side = 1
            expected = 4
            result = square.perimeter(side)
            assert result == expected

            side = 2
            expected = 8
            result = square.perimeter(side)
            assert result == expected

            side = 1.5
            expected = 6
            result = square.perimeter(side)
            assert result == expected

        def test_zero_side(self):
            side = 0
            expected = 0
            result = square.perimeter(side)
            assert result == expected

        @pytest.mark.parametrize("test_input,expected", [
            (1, 4),
            (2, 8),
            (0.5, 2),
            (10, 40)
        ])
        def test_various_sides(self, test_input, expected):
            side = test_input
            result = square.perimeter(side)
            assert result == expected

        @pytest.mark.parametrize("side", [-1, -2.5, -100])
        def test_negative_side(self, side):
            with pytest.raises(ValueError):
                square.perimeter(side)

        @pytest.mark.parametrize("invalid_input", ["2", [1], None])
        def test_invalid_types(self, invalid_input):
            with pytest.raises(TypeError):
                square.perimeter(invalid_input)


class TestTriangle:
    class TestTriangleArea:
        def test_positive_sides(self):
            sides = (3, 4, 5)
            expected = 6
            result = triangle.area(*sides)
            assert result == expected

            sides = (5, 12, 13)
            expected = 30
            result = triangle.area(*sides)
            assert result == expected

            sides = (2, 3, 4)
            expected = 2.90
            result = round(triangle.area(*sides), 2)
            assert result == expected

        @pytest.mark.parametrize("sides", [(0, 1, 1), (1, 0, 1), (1, 1, 0)])
        def test_zero_sides(self, sides):
            with pytest.raises(ValueError):
                triangle.area(*sides)

        @pytest.mark.parametrize("test_input,expected", [
            ((3, 4, 5), 6),
            ((5, 12, 13), 30),
            ((6, 8, 10), 24),
            ((9, 12, 15), 54)
        ])
        def test_various_sides(self, test_input, expected):
            sides = test_input
            result = triangle.area(*sides)
            assert result == expected

        @pytest.mark.parametrize("sides", [
            (-1, 2, 2),
            (2, -1, 2),
            (2, 2, -1),
            (-1, -1, -1)
        ])
        def test_negative_sides(self, sides):
            with pytest.raises(ValueError):
                triangle.area(*sides)

        @pytest.mark.parametrize("sides", [(1, 1, 3), (1, 3, 1), (3, 1, 1)])
        def test_invalid_triangle(self, sides):
            with pytest.raises(ValueError):
                triangle.area(*sides)

        @pytest.mark.parametrize("sides", [("2", 2, 2),
                                           (2, [2], 2), (2, 2, None)])
        def test_invalid_types(self, sides):
            with pytest.raises(TypeError):
                triangle.area(*sides)

    class TestTrianglePerimeter:
        def test_positive_sides(self):
            sides = (3, 4, 5)
            expected = 12
            result = triangle.perimeter(*sides)
            assert result == expected

            sides = (5, 12, 13)
            expected = 30
            result = triangle.perimeter(*sides)
            assert result == expected

            sides = (2, 3, 4)
            expected = 9
            result = triangle.perimeter(*sides)
            assert result == expected

        @pytest.mark.parametrize("sides", [(0, 1, 1), (1, 0, 1), (1, 1, 0)])
        def test_zero_sides(self, sides):
            with pytest.raises(ValueError):
                triangle.perimeter(*sides)

        @pytest.mark.parametrize("test_input,expected", [
            ((3, 4, 5), 12),
            ((5, 12, 13), 30),
            ((6, 8, 10), 24),
            ((9, 12, 15), 36)
        ])
        def test_various_sides(self, test_input, expected):
            sides = test_input
            result = triangle.perimeter(*sides)
            assert result == expected

        @pytest.mark.parametrize("sides", [
            (-1, 2, 2),
            (2, -1, 2),
            (2, 2, -1),
            (-1, -1, -1)
        ])
        def test_negative_sides(self, sides):
            with pytest.raises(ValueError):
                triangle.perimeter(*sides)

        @pytest.mark.parametrize("sides", [(1, 1, 3), (1, 3, 1), (3, 1, 1)])
        def test_invalid_triangle(self, sides):
            with pytest.raises(ValueError):
                triangle.perimeter(*sides)

        @pytest.mark.parametrize("sides", [("2", 2, 2), (2, [2], 2),
                                           (2, 2, None)])
        def test_invalid_types(self, sides):
            with pytest.raises(TypeError):
                triangle.perimeter(*sides)


class TestCalculate:
    def test_valid_circle_calculations(self):
        figure = 'circle'
        operation = 'area'
        size = [2]
        expected = math.pi * 4

        result = calculate.calc(figure, operation, size)
        assert result == expected

    def test_valid_square_calculations(self):
        figure = 'square'
        operation = 'area'
        size = [2]
        expected = 4

        result = calculate.calc(figure, operation, size)
        assert result == expected

    def test_invalid_figure(self):
        figure = 'triangle'
        operation = 'area'
        size = [1]

        with pytest.raises(AssertionError):
            calculate.calc(figure, operation, size)

    def test_invalid_operation(self):
        figure = 'circle'
        operation = 'volume'
        size = [1]

        with pytest.raises(AssertionError):
            calculate.calc(figure, operation, size)

    @pytest.mark.parametrize("test_input", [
        {'figure': 'circle', 'operation': 'area', 'size': [-1]},
        {'figure': 'circle', 'operation': 'perimeter', 'size': [-2]},
        {'figure': 'square', 'operation': 'area', 'size': [-3]},
        {'figure': 'square', 'operation': 'perimeter', 'size': [-4]}
    ])
    def test_negative_sizes(self, test_input):
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        with pytest.raises(ValueError):
            calculate.calc(figure, operation, size)

    @pytest.mark.parametrize("test_input", [
        {'figure': 'circle', 'operation': 'area', 'size': ["string"]},
        {'figure': 'square', 'operation': 'perimeter', 'size': [None]}
    ])
    def test_invalid_input_types(self, test_input):
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        with pytest.raises(TypeError):
            calculate.calc(figure, operation, size)

    def test_empty_size_list(self):
        figure = 'circle'
        operation = 'area'
        size = []

        with pytest.raises(TypeError):
            calculate.calc(figure, operation, size)

    def test_main_integration(self, monkeypatch):
        inputs = ['circle', 'area', '2']
        expected = math.pi * 4
        input_mock = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_mock))

        if hasattr(calculate, 'main'):
            result = calculate.main()
        else:
            result = calculate.calc('circle', 'area', [2])

        assert result == expected

    def test_sizes_dict(self):
        assert isinstance(calculate.sizes, dict)
        assert isinstance(calculate.figs, list)
        assert isinstance(calculate.funcs, list)

    def test_available_figures(self):
        expected_figures = ['circle', 'square']
        for figure in expected_figures:
            assert figure in calculate.figs

    def test_available_functions(self):
        expected_functions = ['area', 'perimeter']
        for function in expected_functions:
            assert function in calculate.funcs

    @pytest.mark.parametrize("test_input,expected", [
        (
                {'figure': 'circle', 'operation': 'area', 'size': [1]},
                math.pi
        ),
        (
                {'figure': 'circle', 'operation': 'perimeter', 'size': [1]},
                2 * math.pi
        ),
        (
                {'figure': 'square', 'operation': 'area', 'size': [1]},
                1
        ),
        (
                {'figure': 'square', 'operation': 'perimeter', 'size': [1]},
                4
        )
    ])
    def test_calculations(self, test_input, expected):
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        result = calculate.calc(figure, operation, size)
        assert result == expected
