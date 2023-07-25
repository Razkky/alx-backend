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
           use index_range to find the correct indexes to
           paginate the dataset correctly
           Return the appropraite page of the dataset (correct list or row)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        csv_file = self.dataset()
        start, end = index_range(page, page_size)

        return csv_file[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing the following keys
           page_size:
           page:
           data:
           next_page:
           prev_page:
           total_page:
        """
        new_dict: dict = {}
        total_page = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        if page < total_page:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        new_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page
        }
        return new_dict


def index_range(page: int, page_size: int) -> Tuple:
    """Calculate the start and end index for pagination"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
