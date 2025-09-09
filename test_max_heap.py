import pytest
import math
from max_heap import Heap


class TestHeapInsert:
    """Heap의 insert 기능을 테스트하는 클래스"""
    
    def test_insert_single_value(self):
        """단일 값 삽입 테스트"""
        heap = Heap()
        heap.insert(10)
        
        assert heap.last_index == 1
        assert heap.array[1] == 10
        assert heap.array[0] is None  # 인덱스 0은 사용하지 않음
    
    def test_insert_multiple_values_maintain_heap_property(self):
        """여러 값 삽입 시 max heap 속성 유지 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25]
        
        for value in values:
            heap.insert(value)
        
        # heap property 확인: 부모 노드가 자식 노드보다 크거나 같아야 함
        for i in range(1, heap.last_index + 1):
            left_child = 2 * i
            right_child = 2 * i + 1
            
            if left_child <= heap.last_index:
                assert heap.array[i] >= heap.array[left_child], f"Parent {heap.array[i]} should be >= left child {heap.array[left_child]}"
            
            if right_child <= heap.last_index:
                assert heap.array[i] >= heap.array[right_child], f"Parent {heap.array[i]} should be >= right child {heap.array[right_child]}"
    
    def test_insert_ascending_order(self):
        """오름차순으로 값 삽입 테스트"""
        heap = Heap()
        values = [1, 2, 3, 4, 5]
        
        for value in values:
            heap.insert(value)
        
        # 루트는 최대값이어야 함
        assert heap.array[1] == 5
        assert heap.last_index == 5
        
        # heap property 확인
        self._verify_heap_property(heap)
    
    def test_insert_descending_order(self):
        """내림차순으로 값 삽입 테스트"""
        heap = Heap()
        values = [5, 4, 3, 2, 1]
        
        for value in values:
            heap.insert(value)
        
        # 루트는 최대값이어야 함
        assert heap.array[1] == 5
        assert heap.last_index == 5
        
        # heap property 확인
        self._verify_heap_property(heap)
    
    def test_insert_duplicate_values(self):
        """중복 값 삽입 테스트"""
        heap = Heap()
        values = [10, 10, 20, 20, 15, 15]
        
        for value in values:
            heap.insert(value)
        
        assert heap.last_index == 6
        # 중복 값들이 모두 삽입되어야 함
        inserted_values = [heap.array[i] for i in range(1, heap.last_index + 1)]
        for value in values:
            assert value in inserted_values
        
        # heap property 확인
        self._verify_heap_property(heap)
    
    def test_insert_large_numbers(self):
        """큰 수 삽입 테스트"""
        heap = Heap()
        values = [1000000, 999999, 1000001, 500000]
        
        for value in values:
            heap.insert(value)
        
        assert heap.array[1] == 1000001  # 최대값이 루트에 있어야 함
        self._verify_heap_property(heap)
    
    def test_insert_negative_numbers(self):
        """음수 삽입 테스트"""
        heap = Heap()
        values = [-10, -5, -20, -1, -15]
        
        for value in values:
            heap.insert(value)
        
        assert heap.array[1] == -1  # 최대값(가장 큰 음수)이 루트에 있어야 함
        self._verify_heap_property(heap)
    
    def test_insert_mixed_positive_negative(self):
        """양수와 음수 혼합 삽입 테스트"""
        heap = Heap()
        values = [10, -5, 20, -10, 0, 15]
        
        for value in values:
            heap.insert(value)
        
        assert heap.array[1] == 20  # 최대값이 루트에 있어야 함
        self._verify_heap_property(heap)
    
    def test_insert_triggers_array_growth(self):
        """배열 크기 확장 기능 테스트"""
        heap = Heap()
        initial_size = len(heap.array)
        
        # 초기 배열 크기를 초과하는 값들 삽입
        for i in range(initial_size + 10):
            heap.insert(i)
        
        # 배열이 확장되었는지 확인
        assert len(heap.array) > initial_size
        assert heap.last_index == initial_size + 10
        
        # heap property 확인
        self._verify_heap_property(heap)
    
    def test_insert_zero(self):
        """0 삽입 테스트"""
        heap = Heap()
        heap.insert(0)
        
        assert heap.array[1] == 0
        assert heap.last_index == 1
    
    def test_insert_single_then_larger(self):
        """작은 값 삽입 후 큰 값 삽입 테스트"""
        heap = Heap()
        heap.insert(5)
        heap.insert(10)
        
        assert heap.array[1] == 10  # 큰 값이 루트로 이동해야 함
        assert heap.array[2] == 5   # 작은 값이 자식으로 이동해야 함
        assert heap.last_index == 2
    
    def test_insert_maintains_complete_binary_tree(self):
        """완전 이진 트리 구조 유지 테스트"""
        heap = Heap()
        values = [1, 2, 3, 4, 5, 6, 7]
        
        for value in values:
            heap.insert(value)
        
        # 완전 이진 트리는 레벨별로 왼쪽부터 채워져야 함
        assert heap.last_index == 7
        
        # 모든 레벨이 올바르게 채워져 있는지 확인
        for i in range(1, heap.last_index + 1):
            assert heap.array[i] is not None
        
        # heap property 확인
        self._verify_heap_property(heap)
    
    def _verify_heap_property(self, heap):
        """heap property가 유지되는지 확인하는 헬퍼 메서드"""
        for i in range(1, heap.last_index + 1):
            left_child = 2 * i
            right_child = 2 * i + 1
            
            if left_child <= heap.last_index:
                assert heap.array[i] >= heap.array[left_child], \
                    f"Heap property violated: parent {heap.array[i]} < left child {heap.array[left_child]} at index {i}"
            
            if right_child <= heap.last_index:
                assert heap.array[i] >= heap.array[right_child], \
                    f"Heap property violated: parent {heap.array[i]} < right child {heap.array[right_child]} at index {i}"


class TestHeapDelete:
    """Heap의 delete 기능을 테스트하는 클래스"""
    
    def test_delete_invalid_index(self):
        """유효하지 않은 인덱스 삭제 테스트"""
        heap = Heap()
        heap.insert(10)
        heap.insert(20)
        heap.insert(15)
        
        # 범위를 벗어난 인덱스들
        assert heap.delete(0) == False  # 인덱스 0은 사용하지 않음
        assert heap.delete(4) == False  # 존재하지 않는 인덱스
        assert heap.delete(-1) == False  # 음수 인덱스
        
        # 힙 상태가 변하지 않았는지 확인
        assert heap.last_index == 3
        self._verify_heap_property(heap)
    
    def test_delete_last_node(self):
        """마지막 노드 삭제 테스트"""
        heap = Heap()
        values = [30, 20, 15, 10, 5]
        for value in values:
            heap.insert(value)
        
        initial_last_index = heap.last_index
        last_node_index = heap.last_index
        
        # 마지막 노드 삭제
        assert heap.delete(last_node_index) == True
        assert heap.last_index == initial_last_index - 1
        assert heap.array[initial_last_index] is None
        
        # 힙 속성 유지 확인
        self._verify_heap_property(heap)
    
    def test_delete_root_node(self):
        """루트 노드 삭제 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25]
        for value in values:
            heap.insert(value)
        
        original_max = heap.array[1]  # 30이어야 함
        original_size = heap.last_index
        
        # 루트 삭제
        assert heap.delete(1) == True
        assert heap.last_index == original_size - 1
        
        # 새로운 루트가 올바른지 확인 (두 번째로 큰 값이어야 함)
        assert heap.array[1] != original_max
        
        # 힙 속성 유지 확인
        self._verify_heap_property(heap)
    
    def test_delete_middle_node(self):
        """중간 노드 삭제 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25, 12, 8]
        for value in values:
            heap.insert(value)
        
        original_size = heap.last_index
        
        # 중간 노드 삭제 (인덱스 3)
        deleted_value = heap.array[3]
        assert heap.delete(3) == True
        assert heap.last_index == original_size - 1
        
        # 삭제된 값이 힙에 없는지 확인
        heap_values = [heap.array[i] for i in range(1, heap.last_index + 1)]
        assert deleted_value not in heap_values or heap_values.count(deleted_value) < values.count(deleted_value)
        
        # 힙 속성 유지 확인
        self._verify_heap_property(heap)
    
    def test_delete_single_element(self):
        """단일 요소 힙에서 삭제 테스트"""
        heap = Heap()
        heap.insert(42)
        
        assert heap.delete(1) == True
        assert heap.last_index == 0
        assert heap.array[1] is None
    
    def test_delete_empty_heap(self):
        """빈 힙에서 삭제 테스트"""
        heap = Heap()
        
        assert heap.delete(1) == False
        assert heap.last_index == 0
    
    def test_delete_all_elements_sequentially(self):
        """모든 요소를 순차적으로 삭제하는 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25]
        for value in values:
            heap.insert(value)
        
        original_size = heap.last_index
        
        # 루트를 계속 삭제
        for i in range(original_size):
            assert heap.delete(1) == True
            self._verify_heap_property(heap)
        
        assert heap.last_index == 0
    
    def test_delete_root_method(self):
        """delete_root 메서드 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25]
        for value in values:
            heap.insert(value)
        
        # 최대값들을 순서대로 추출
        extracted_values = []
        while heap.last_index > 0:
            max_val = heap.delete_root()
            extracted_values.append(max_val)
            if heap.last_index > 0:
                self._verify_heap_property(heap)
        
        # 내림차순으로 정렬되어야 함
        assert extracted_values == sorted(values, reverse=True)
    
    def test_delete_root_empty_heap(self):
        """빈 힙에서 delete_root 테스트"""
        heap = Heap()
        assert heap.delete_root() is None
    
    def test_peek_method(self):
        """peek 메서드 테스트"""
        heap = Heap()
        
        # 빈 힙
        assert heap.peek() is None
        
        # 값 삽입 후
        heap.insert(10)
        heap.insert(30)
        heap.insert(20)
        
        original_size = heap.last_index
        max_value = heap.peek()
        
        # peek은 값을 제거하지 않아야 함
        assert max_value == 30
        assert heap.last_index == original_size
        assert heap.array[1] == 30
    
    def test_delete_with_duplicates(self):
        """중복값이 있는 힙에서 삭제 테스트"""
        heap = Heap()
        values = [20, 20, 15, 20, 10]
        for value in values:
            heap.insert(value)
        
        # 루트 삭제 (20 중 하나)
        assert heap.delete(1) == True
        
        # 여전히 20이 루트에 있어야 함 (다른 20이 올라와야 함)
        assert heap.array[1] == 20
        self._verify_heap_property(heap)
    
    def test_delete_maintains_complete_binary_tree(self):
        """삭제 후 완전 이진 트리 구조 유지 테스트"""
        heap = Heap()
        values = [10, 20, 15, 30, 25, 12, 8, 35]
        for value in values:
            heap.insert(value)
        
        # 여러 노드 삭제
        heap.delete(1)  # 루트
        heap.delete(2)  # 새로운 구조에서 인덱스 2
        
        # 완전 이진 트리 구조 확인
        for i in range(1, heap.last_index + 1):
            assert heap.array[i] is not None
        
        # 힙 속성 확인
        self._verify_heap_property(heap)
    
    def test_delete_performance_large_heap(self):
        """큰 힙에서의 삭제 성능 테스트"""
        heap = Heap()
        
        # 큰 힙 생성
        import random
        values = list(range(1000))
        random.shuffle(values)
        
        for value in values:
            heap.insert(value)
        
        # 여러 삭제 수행
        for _ in range(100):
            heap.delete(1)  # 루트 삭제
            if heap.last_index > 0:
                self._verify_heap_property(heap)
        
        assert heap.last_index == 900
    
    def _verify_heap_property(self, heap):
        """heap property가 유지되는지 확인하는 헬퍼 메서드"""
        for i in range(1, heap.last_index + 1):
            left_child = 2 * i
            right_child = 2 * i + 1
            
            if left_child <= heap.last_index:
                assert heap.array[i] >= heap.array[left_child], \
                    f"Heap property violated: parent {heap.array[i]} < left child {heap.array[left_child]} at index {i}"
            
            if right_child <= heap.last_index:
                assert heap.array[i] >= heap.array[right_child], \
                    f"Heap property violated: parent {heap.array[i]} < right child {heap.array[right_child]} at index {i}"


if __name__ == "__main__":
    # 직접 실행할 때의 테스트
    print("Heap delete 테스트 실행 중...")
    
    # 기본 삭제 테스트
    heap = Heap()
    test_values = [10, 20, 15, 30, 25]
    
    print(f"삽입할 값들: {test_values}")
    
    for value in test_values:
        heap.insert(value)
    
    print(f"삽입 후 heap 상태: {[heap.array[i] for i in range(1, heap.last_index + 1)]}")
    
    # 루트 삭제 테스트
    print(f"루트 삭제 전 최대값: {heap.peek()}")
    deleted_value = heap.delete_root()
    print(f"삭제된 값: {deleted_value}")
    print(f"삭제 후 heap 상태: {[heap.array[i] for i in range(1, heap.last_index + 1)]}")
    print(f"새로운 최대값: {heap.peek()}")
    
    # 모든 값 삭제하며 정렬된 순서로 출력
    print("모든 값을 삭제하며 정렬된 순서로 출력:")
    sorted_values = []
    while heap.last_index > 0:
        max_val = heap.delete_root()
        sorted_values.append(max_val)
        print(f"삭제된 값: {max_val}, 남은 heap: {[heap.array[i] for i in range(1, heap.last_index + 1)] if heap.last_index > 0 else '빈 힙'}")
    
    print(f"정렬된 결과 (내림차순): {sorted_values}")
    print("테스트 완료!")
