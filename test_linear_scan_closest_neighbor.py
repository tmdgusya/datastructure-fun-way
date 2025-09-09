from linear_scan_closest_neighbor import linear_scan_closest_neighbor


def test_empty_array():
    """빈 배열에 대한 테스트"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    result = linear_scan_closest_neighbor([], 5, manhattan_distance)
    assert result == -1


def test_single_element():
    """단일 원소 배열 테스트"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    result = linear_scan_closest_neighbor([10], 5, manhattan_distance)
    assert result == 10


def test_target_exists_in_array():
    """타겟이 배열에 존재하는 경우"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [1, 5, 10, 15, 20]
    result = linear_scan_closest_neighbor(array, 10, manhattan_distance)
    assert result == 10


def test_target_not_in_array():
    """타겟이 배열에 없는 경우 - 가장 가까운 값 찾기"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [1, 5, 10, 15, 20]
    result = linear_scan_closest_neighbor(array, 12, manhattan_distance)
    assert result == 10  # 12에서 10까지 거리 2, 15까지 거리 3


def test_multiple_same_distance():
    """같은 거리의 원소가 여러 개인 경우 - 첫 번째 발견한 것 반환"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [5, 15, 25]  # 20에서 각각 거리 15, 5, 5
    result = linear_scan_closest_neighbor(array, 20, manhattan_distance)
    assert result == 15  # 첫 번째로 발견된 가장 가까운 값


def test_negative_numbers():
    """음수가 포함된 배열 테스트"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [-10, -5, 0, 5, 10]
    result = linear_scan_closest_neighbor(array, -3, manhattan_distance)
    assert result == -5  # -3에서 -5까지 거리 2


def test_all_same_values():
    """모든 값이 같은 경우"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [7, 7, 7, 7]
    result = linear_scan_closest_neighbor(array, 5, manhattan_distance)
    assert result == 7


def test_custom_distance_function():
    """사용자 정의 거리 함수 테스트"""
    def squared_distance(a, b):
        return (a - b) ** 2
    
    array = [1, 3, 5, 7, 9]
    result = linear_scan_closest_neighbor(array, 4, squared_distance)
    assert result == 3  # 4에서 3까지 제곱거리 1, 5까지 제곱거리 1 (첫 번째 발견)


def test_large_array():
    """큰 배열 테스트"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = list(range(1, 1001))  # 1부터 1000까지
    result = linear_scan_closest_neighbor(array, 500, manhattan_distance)
    assert result == 500


def test_floating_point_target():
    """부동소수점 타겟 테스트 (정수 배열과)"""
    def manhattan_distance(a, b):
        return abs(a - b)
    
    array = [1, 3, 5, 7, 9]
    result = linear_scan_closest_neighbor(array, 4.7, manhattan_distance)
    assert result == 5  # 4.7에서 5까지 거리 0.3


def test_euclidean_distance():
    """유클리드 거리 함수 테스트"""
    def euclidean_distance(a, b):
        return ((a - b) ** 2) ** 0.5
    
    array = [1, 5, 10, 15]
    result = linear_scan_closest_neighbor(array, 7, euclidean_distance)
    assert result == 5  # 7에서 5까지 거리 2, 10까지 거리 3


if __name__ == "__main__":
    # 모든 테스트 실행
    test_empty_array()
    test_single_element()
    test_target_exists_in_array()
    test_target_not_in_array()
    test_multiple_same_distance()
    test_negative_numbers()
    test_all_same_values()
    test_custom_distance_function()
    test_large_array()
    test_floating_point_target()
    test_euclidean_distance()
    
    print("모든 테스트가 통과했습니다! ✅")
