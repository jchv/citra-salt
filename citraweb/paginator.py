class InvalidPage(Exception):
    pass


class Page(object):
    def __init__(self, object_list, page_size, page_num):
        self.object_list = object_list
        self.page_size = page_size

        try:
            self.page_num = int(page_num)
        except ValueError:
            raise InvalidPage

        if self.page_num < self.first_page or self.page_num > self.last_page:
            raise InvalidPage

    def __len__(self):
        return self.page_size

    def __getitem__(self, item):
        if not(self.first_index <= item + self.first_index <= self.last_index):
            raise IndexError()

        return self.object_list[min(item + self.first_index, self.last_index)]

    @property
    def num_pages(self):
        return int((len(self.object_list) + self.page_size - 1) / self.page_size)

    @property
    def first_page(self):
        return 1

    @property
    def last_page(self):
        return max(self.num_pages, 1)

    @property
    def all_page_numbers(self):
        return range(self.first_page, self.last_page + 1)

    def page_numbers(self):
        # Get some useful ranges.
        start = list(range(self.first_page, self.first_page + 5))
        end = list(range(self.last_page - 5, self.last_page + 1))
        mid = list(range(self.page_num - 2, self.page_num + 3))

        # Knock out invalid and duplicate page numbers.
        valid_pages = list(set(self.all_page_numbers) & set(start + end + mid))

        # Insert some placeholders between discontinuities.
        pages = [valid_pages[0]]
        for n in range(1, len(valid_pages)):
            if valid_pages[n - 1] != valid_pages[n] - 1:
                pages.append('...')
            pages.append(valid_pages[n])

        return pages

    @property
    def first_index(self):
        return (self.page_num - self.first_page) * self.page_size

    @property
    def last_index(self):
        return self.first_index + self.page_size - 1

    @property
    def has_previous_page(self):
        return self.page_num > self.first_page

    @property
    def has_next_page(self):
        return self.page_num < self.last_page

    @property
    def previous_page(self):
        return self.page_num - 1

    @property
    def next_page(self):
        return self.page_num + 1


class Paginator(object):
    def __init__(self, object_list, page_size=10):
        self.object_list = object_list
        self.page_size = page_size

    def page(self, page_num):
        return Page(self.object_list, self.page_size, page_num)
