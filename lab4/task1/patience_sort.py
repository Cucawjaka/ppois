from bisect import bisect_left

from task1.Comparable import Comparable


def patience_sort[T: Comparable](array: list[T]) -> list[T]:
    def _merge_elements(*stacks: list[T]) -> list[T]:
        result: list[T] = list()
        stacks_list: list[list[T]] = list(stacks)

        while stacks_list:
            min_element_stack_ind: int = 0
            min_element: T = stacks_list[0][-1]

            for index in range(len(stacks_list)):
                if stacks_list[index][-1] < min_element:
                    min_element = stacks_list[index][-1]
                    min_element_stack_ind = index

            result.append(min_element)
            stacks_list[min_element_stack_ind].pop()
            if len(stacks_list[min_element_stack_ind]) == 0:
                stacks_list.pop(min_element_stack_ind)

        return result

    stacks: list[list[T]] = list()

    for element in array:
        insert_postion: int = bisect_left(stacks, element, key=lambda stack: stack[-1])

        if insert_postion != len(stacks):
            stacks[insert_postion].append(element)
        else:
            stacks.append([element])

    return _merge_elements(*stacks)
