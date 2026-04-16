class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        from collections import defaultdict, deque

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_routes = set()
        visited_stops = set([source])
        queue = deque([(source, 0)])

        while queue:
            stop, buses = queue.popleft()

            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue
                visited_routes.add(route_idx)

                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))

        return -1