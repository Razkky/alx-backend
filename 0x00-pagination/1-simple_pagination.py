#!/usr/bin/env python3
"""This script creates and index_range"""
import csv
import math
from typing import Tuple, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Verify both page and page_size are int greater than 0
        use index_range to find the correct indexes to paginate the dataset correctly
        Return the appropraite page of the dataset (correct list or row)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        csv_file = self.dataset()
        start, end = index_range(page, page_size)

        return csv_file[start : end]


def index_range(page: int, page_size: int) -> Tuple:
    """Calculate the start and end index for pagination"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

