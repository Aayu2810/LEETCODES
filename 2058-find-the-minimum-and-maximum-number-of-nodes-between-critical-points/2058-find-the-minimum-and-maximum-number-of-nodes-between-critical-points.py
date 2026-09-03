class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        min_distance = float("inf")
        previous_node = head
        current_node = head.next
        current_index = 1
        previous_critical_index = 0
        first_critical_index = 0
        while current_node.next is not None:
            if (
                current_node.val < previous_node.val
                and current_node.val < current_node.next.val
            ) or (
                current_node.val > previous_node.val
                and current_node.val > current_node.next.val
            ):
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                else:
                    min_distance = min(
                        min_distance, current_index - previous_critical_index
                    )
                    previous_critical_index = current_index
            current_index += 1
            previous_node = current_node
            current_node = current_node.next
        if min_distance != float("inf"):
            max_distance = previous_critical_index - first_critical_index
            result = [min_distance, max_distance]

        return result