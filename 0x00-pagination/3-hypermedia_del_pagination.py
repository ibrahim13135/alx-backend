#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]  # Truncated for faster testing
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination info with deletion resilience.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing pagination information.
        """
        assert index is not None and isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), (
            "index must be a valid integer within the dataset range"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be an integer greater than 0"
        )

        data = []
        next_index = index
        current_size = 0
        indexed_dataset = self.indexed_dataset()

        while current_size < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                current_size += 1
            next_index += 1

        # Adjust next_index to handle deletions
        while next_index < len(indexed_dataset) and next_index not in indexed_dataset:
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": current_size,
            "data": data,
        }
