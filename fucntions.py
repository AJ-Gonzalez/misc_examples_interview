# 1
# Pretend that an API exists at https://example.com/api/products which returns:
# [{"product": "Shoes", "price": 35, "rating": 4.2},
# {"product": "White Hat", "price": 21, "rating": 4.8},
# ...]
#
# Write a function in Python to consume this API.
# Write another function for business logic to find all products rated 4 and above.
# Write enough unit / integration tests to completely cover the code in both functions.
import requests
import unittest
# Test Data:


data = [{"product": "Shoes", "price": 35, "rating": 4.2},
        {"product": "White Hat", "price": 21, "rating": 4.8}]


def fetcher(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code


def fetcher_err(url):
    try:
        response = requests.get(url, timeout=0.5)
        return response.json()
    except Exception as e:    # This is the correct syntax
        # This would go to system logs or any remote logging
        raise ConnectionError("connection error")


def finder_over_four(list_object):
    filtered = []
    for datum in list_object:
        if datum["rating"] >= 4:
            filtered.append(datum)
    return filtered


def finder_over_four_LC(list_object):
    return [x for x in list_object if x["rating"] >= 4]


def integration(url):
    return finder_over_four_LC(fetcher_err(url))


class TestFinderOverFour(unittest.TestCase):
    def test_finder_over_four_success(self):
        actual = finder_over_four(data)
        expected = [{'product': 'Shoes', 'price': 35, 'rating': 4.2}, {
            'product': 'White Hat', 'price': 21, 'rating': 4.8}]
        self.assertEqual(actual, expected)


class TestFinderOverFourLC(unittest.TestCase):
    def test_finder_over_four__LC_success(self):
        actual = finder_over_four_LC(data)
        expected = [{'product': 'Shoes', 'price': 35, 'rating': 4.2}, {
            'product': 'White Hat', 'price': 21, 'rating': 4.8}]
        self.assertEqual(actual, expected)


class TestFetcher(unittest.TestCase):
    def test_fetcher_success(self):
        actual = fetcher("https://jsonplaceholder.typicode.com/todos/1")
        expected = {'userId': 1, 'id': 1,
                    'title': 'delectus aut autem', 'completed': False}
        self.assertEqual(actual, expected)


class TestFetcherError(unittest.TestCase):
    def test_fetcher_err_success(self):
        actual = fetcher_err("https://jsonplaceholder.typicode.com/todos/1")
        expected = {'userId': 1, 'id': 1,
                    'title': 'delectus aut autem', 'completed': False}
        self.assertEqual(actual, expected)

    def test_fetcher_err_exception(self):
        with self.assertRaises(ConnectionError) as exception_context:
            fetcher_err("https://jsonplaceholder-bad-url.typicode.com/todos/1")
        self.assertEqual(
            str(exception_context.exception),
            "connection error"
        )


class TestIntegration(unittest.TestCase):

    def test_integration_success(self):
        actual = integration("http://127.0.0.1:5000/")
        expected = [{'product': 'Shoes', 'price': 35, 'rating': 4.2},
                    {'product': 'White Hat', 'price': 21, 'rating': 4.8},
                    {'product': 'Pink Hat', 'price': 23, 'rating': 4.5}]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    print(finder_over_four(data))
    print(finder_over_four_LC(data))
    print(fetcher("https://jsonplaceholder.typicode.com/todos/1"))
    print(fetcher_err('https://jsonplaceholder.typicode.com/todos/1'))
    print(integration("http://127.0.0.1:5000/"))
    # print(fetcher_err('https://jsonplaceholderbadurl.typicode.com/todos/1'))
