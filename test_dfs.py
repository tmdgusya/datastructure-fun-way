"""
DFS 알고리즘 테스트 케이스

이 파일은 직접 구현한 Stack을 사용하여 DFS 알고리즘을 테스트하기 위한 케이스들을 제공합니다.
다양한 그래프 구조와 엣지 케이스들을 포함하고 있습니다.

테스트할 DFS 함수 시그니처:
def dfs(graph, start_node):
    # 여기에 Stack을 사용한 DFS 구현
    # return visited_order  # 방문한 노드들의 순서를 리스트로 반환
    pass
"""

from typing import List
from stack import Stack


def dfs(graph: dict, start_node):
  result = []
  visited = set()
  s = Stack(30)
  s.push(start_node)
  
  while s.top > -1:
    ele = s.pop()

    if ele not in visited:
      visited.add(ele)
      result.append(ele)

    for neighbor in graph.get(ele, []):
      if neighbor not in visited:
        s.push(neighbor)
    

  return result


def test_simple_linear_graph():
    """
    간단한 선형 그래프 테스트
    1 -> 2 -> 3 -> 4
    """
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: []
    }
    start_node = 1
    expected_order = [1, 2, 3, 4]
    
    print("=== 테스트 1: 선형 그래프 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()
    
    result = dfs(graph, start_node)
    assert result == expected_order, f"Expected {expected_order}, got {result}"


def test_simple_tree():
    """
    간단한 트리 구조 테스트
        1
       / \
      2   3
     /   / \
    4   5   6
    """
    graph = {
        1: [2, 3],
        2: [4],
        3: [5, 6],
        4: [],
        5: [],
        6: []
    }
    start_node = 1
    # DFS는 스택을 사용하므로 오른쪽부터 방문 (후입선출)
    expected_order = [1, 3, 6, 5, 2, 4]
    
    print("=== 테스트 2: 트리 구조 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_graph_with_cycle():
    """
    사이클이 있는 그래프 테스트
    1 -> 2 -> 3
    ^         |
    |         v
    +-------- 4
    """
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [1]  # 사이클 생성
    }
    start_node = 1
    # 사이클이 있어도 각 노드는 한 번만 방문
    expected_order = [1, 2, 3, 4]
    
    print("=== 테스트 3: 사이클이 있는 그래프 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_disconnected_component():
    """
    연결되지 않은 컴포넌트가 있는 그래프
    1 -> 2    3 -> 4
    """
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    start_node = 1
    expected_order = [1, 2]  # 3, 4는 연결되지 않아서 방문 안됨
    
    print("=== 테스트 4: 연결되지 않은 컴포넌트 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_single_node():
    """
    단일 노드 테스트
    """
    graph = {
        1: []
    }
    start_node = 1
    expected_order = [1]
    
    print("=== 테스트 5: 단일 노드 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_complex_graph():
    """
    복잡한 그래프 구조
        1
       /|\
      2 3 4
     /| |  \
    5 6 7   8
    """
    graph = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [7],
        4: [8],
        5: [],
        6: [],
        7: [],
        8: []
    }
    start_node = 1
    # 스택 특성상 마지막에 추가된 것부터 처리 (4 -> 3 -> 2 순서)
    expected_order = [1, 4, 8, 3, 7, 2, 6, 5]
    
    print("=== 테스트 6: 복잡한 그래프 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_self_loop():
    """
    자기 자신을 가리키는 루프가 있는 경우
    """
    graph = {
        1: [1, 2],  # 자기 자신을 가리킴
        2: [3],
        3: []
    }
    start_node = 1
    expected_order = [1, 2, 3]  # 자기 자신은 이미 방문했으므로 무시
    
    print("=== 테스트 7: 셀프 루프 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_multiple_paths():
    """
    같은 노드로 가는 여러 경로가 있는 경우
    1 -> 2 -> 4
    |         ^
    v         |
    3 --------+
    """
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    start_node = 1
    expected_order = [1, 3, 4, 2]  # 4는 3에서 먼저 방문되므로 2에서는 방문 안함
    
    print("=== 테스트 8: 여러 경로 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def test_empty_graph():
    """
    빈 그래프 테스트
    """
    graph = {}
    start_node = 1
    expected_order = []  # 시작 노드가 그래프에 없으므로 빈 리스트
    
    print("=== 테스트 9: 빈 그래프 ===")
    print(f"그래프: {graph}")
    print(f"시작 노드: {start_node}")
    print(f"예상 방문 순서: {expected_order}")
    print()


def run_all_tests():
    """모든 테스트 케이스 실행"""
    print("DFS 알고리즘 테스트 케이스들")
    print("=" * 50)
    print()
    
    test_simple_linear_graph()
    test_simple_tree()
    test_graph_with_cycle()
    test_disconnected_component()
    test_single_node()
    test_complex_graph()
    test_self_loop()
    test_multiple_paths()
    test_empty_graph()
    
    print("=" * 50)
    print("모든 테스트 케이스 출력 완료!")
    print()
    print("DFS 구현 가이드:")
    print("1. Stack을 사용해서 구현하세요")
    print("2. visited 집합을 사용해서 중복 방문을 방지하세요")
    print("3. 방문한 노드들의 순서를 리스트로 반환하세요")
    print()
    print("예시 함수 시그니처:")
    print("def dfs(graph, start_node):")
    print("    visited = set()")
    print("    visited_order = []")
    print("    stack = Stack(10)  # 적당한 초기 크기")
    print("    # 구현 부분...")
    print("    return visited_order")


if __name__ == "__main__":
    run_all_tests()
