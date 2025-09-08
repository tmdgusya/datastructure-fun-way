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


if __name__ == "__main__":
    # 직접 실행할 때의 간단한 테스트
    print("Heap insert 테스트 실행 중...")
    
    # 기본 테스트
    heap = Heap()
    test_values = [10, 20, 15, 30, 25]
    
    print(f"삽입할 값들: {test_values}")
    
    for value in test_values:
        heap.insert(value)
        print(f"{value} 삽입 후 heap 상태: {[heap.array[i] for i in range(1, heap.last_index + 1)]}")
    
    print(f"최종 heap 배열: {[heap.array[i] for i in range(1, heap.last_index + 1)]}")
    print(f"루트 노드 (최대값): {heap.array[1]}")
    print("테스트 완료!")
