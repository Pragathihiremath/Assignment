def get_time(tasks, dependencies):
    # Initialize data structures
    D = {task: duration for task, duration in tasks}
    EST = {task: 0 for task, _ in tasks}
    EFT = {task: 0 for task, _ in tasks}
    LST = {task: float('inf') for task, _ in tasks}
    LFT = {task: float('inf') for task, _ in tasks}

    # create directed graph and in-degree count for topological sorting
    graph = {}
    in_degree = {task: 0 for task, _ in tasks}
    
    for task, deps in dependencies.items():
        if task not in graph:
            graph[task] = []  # Initialize the list if the task has dependencies
        for dep in deps:
            if dep not in graph:
                graph[dep] = []  # Initialize the list for dependencies
            graph[dep].append(task)
            in_degree[task] += 1

    # Perform topological sort
    topo_sort = []
    zero_in_degree = [task for task, count in in_degree.items() if count == 0]
    
    while zero_in_degree:
        current_task = zero_in_degree.pop(0)
        topo_sort.append(current_task)
        for neighbor in graph[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # Compute EST and EFT
    for task in topo_sort:
        for dep in dependencies.get(task, []):
            EST[task] = max(EST[task], EFT[dep])
        EFT[task] = EST[task] + D[task]

    # Compute LFT and LST in reverse topological order
    completion_time = max(EFT.values())
    for task in topo_sort[::-1]:
        if not graph[task]:  # Leaf nodes
            LFT[task] = completion_time
        for neighbor in graph[task]:
            LFT[task] = min(LFT[task], LST[neighbor])
        LST[task] = LFT[task] - D[task]
    return EFT, LFT

# Example 
tasks = [('T1', 4), ('T2', 3), ('T3', 2), ('T4', 1)]
dependencies = {
    'T2': ['T1'],
    'T3': ['T1'],
    'T4': ['T2', 'T3']
}

earliest, latest = get_time(tasks, dependencies)
print(f"Earliest completion time: {earliest}")
print(f"Latest completion time: {latest}")
